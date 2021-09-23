from django.db import models
from django.db.models.deletion import CASCADE

class Tag(models.Model):
    name = models.CharField(max_length=200, default='oi')

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Tag, on_delete=CASCADE)
    
    def __str__(self):
        return '{0}.{1}'.format(self.id, self.title)