from django.db import models

# Create your models here.
class UploadedPDF(models.Model):
    file = models.FileField(upload_to='uploads/',help_text='PDF file uploaded by the user')
    uploaded_at = models.DateTimeField(auto_now_add=True,help_text='Timestamp when Uploaded')
    name = models.CharField(max_length=255,blank=True,null=True,help_text='Name of the User')

    def __str__(self):
        return self.name if self.name else f"PDF uploaded at {self.uploaded_at}"