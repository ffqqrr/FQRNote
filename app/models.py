from django.db import models

class NoteInfo(models.Model):
    note_id = models.TextField()
    content = models.TextField()