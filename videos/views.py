from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Video
from .forms import VideoForm, SignUpForm
from .utils import verify_video

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('video_list')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to Secure Video Authenticator, {user.username}!")
            return redirect('video_list')
    else:
        form = SignUpForm()
    return render(request, template_name='signup.html', context={'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')

def video_list(request):
    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '').strip()

    videos = Video.objects.all().order_by('-uploaded_at')

    # Dashboard Statistics
    total_count = videos.count()
    authentic_count = videos.filter(verification_status__icontains='Authentic').count()
    suspicious_count = videos.filter(Q(verification_status__icontains='Suspicious') | Q(verification_status__icontains='Fake') | Q(verification_status__icontains='Invalid')).count()
    pending_count = total_count - authentic_count - suspicious_count

    # Filtering & Search
    if query:
        videos = videos.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(file_hash__icontains=query))

    if status_filter == 'authentic':
        videos = videos.filter(verification_status__icontains='Authentic')
    elif status_filter == 'suspicious':
        videos = videos.filter(Q(verification_status__icontains='Suspicious') | Q(verification_status__icontains='Fake') | Q(verification_status__icontains='Invalid'))
    elif status_filter == 'pending':
        videos = videos.exclude(verification_status__icontains='Authentic').exclude(verification_status__icontains='Suspicious')

    context = {
        'videos': videos,
        'query': query,
        'status_filter': status_filter,
        'stats': {
            'total': total_count,
            'authentic': authentic_count,
            'suspicious': suspicious_count,
            'pending': pending_count,
        }
    }
    return render(request, template_name='videos/video_list.html', context=context)

@login_required
def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()

            # Execute Forensic Verification Algorithm
            res = verify_video(video.file.path)
            video.verification_status = res['status']
            video.authenticity_score = res['score']
            video.file_hash = res['sha256']
            video.md5_hash = res['md5']
            video.file_size = res['size']
            video.container_format = res['format']
            video.verification_notes = res['notes']
            video.save()

            messages.success(request, f"Video '{video.title}' uploaded and verified successfully ({res['status']} - {res['score']}% Confidence)!")
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, template_name='videos/video_upload.html', context={'form': form})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, template_name='videos/video_detail.html', context={'video': video})

@login_required
def video_delete(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if video.uploaded_by == request.user or request.user.is_staff:
        video.file.delete()
        video.delete()
        messages.success(request, "Video removed permanently.")
    else:
        messages.error(request, "Permission denied. You can only delete your own videos.")
    return redirect('video_list')