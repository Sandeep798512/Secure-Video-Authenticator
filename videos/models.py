from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    verification_status = models.CharField(max_length=50, default='Pending')
    authenticity_score = models.IntegerField(default=100, help_text="Authenticity Confidence Score (0-100%)")
    file_hash = models.CharField(max_length=64, blank=True, null=True, help_text="SHA-256 Checksum")
    md5_hash = models.CharField(max_length=32, blank=True, null=True, help_text="MD5 Checksum")
    file_size = models.BigIntegerField(blank=True, null=True)
    container_format = models.CharField(max_length=50, blank=True, null=True)
    verification_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def formatted_size(self):
        if not self.file_size:
            return "0 KB"
        kb = self.file_size / 1024
        if kb < 1024:
            return f"{kb:.1f} KB"
        mb = kb / 1024
        return f"{mb:.2f} MB"