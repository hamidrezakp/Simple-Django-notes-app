from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    text = tinymce_models.HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
