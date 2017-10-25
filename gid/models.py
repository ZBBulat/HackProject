from django.db import models
from django.utils import timezone

class Ot(models.Model):
    post = models.ForeignKey('gid.Tyr', related_name='ots')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Tyr(models.Model):
   title = models.CharField(max_length=200)
   text = models.TextField()
   published_date = models.DateTimeField(
            blank=True, null=True)
   approved_tyr = models.BooleanField(default=False)

   def publish(self):
       self.approved_comment = True
       self.save()

   def __str__(self):
        return self.title