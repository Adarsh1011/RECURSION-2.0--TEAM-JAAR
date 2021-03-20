from enum import auto
from django.db import models
from django.utils import timezone
from users.models import NewUser
from django.urls import reverse

class Post(models.Model):

    name = models.CharField(max_length = 100)
    content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=10, default="Mumbai")
    address = models.TextField(default="Maharashtra")
    covid_cap=models.IntegerField(default=0)
    norm_cap = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})