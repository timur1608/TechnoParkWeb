from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileManager(models.Manager):
    def alive(self):
        self.filter(birthDate='null')


class Question(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', related_name='questions')
    date_written = models.DateField()

    def __str__(self):
        if (len(self.text) < 40):
            return f'{self.text[0:40]}'
        return f'{self.text[0:40]}...'


class Answer(models.Model):
    text = models.TextField()
    profile = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    is_correct = models.BooleanField(default=False)


class Tag(models.Model):
    label = models.CharField(max_length=256)
    def __str__(self):
        return f'{self.label}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=256)
    birthDate = models.DateField(null=True, blank=True);
    is_deleted = models.BooleanField(default=False)

    objects = ProfileManager()

    def __str__(self):
        return f'{self.nickname}'


class Like(models.Model):
    countOfLikes = models.IntegerField()
    countOfDislikes = models.IntegerField()
    answer = models.ForeignKey('Answer', max_length=256, on_delete=models.PROTECT)
