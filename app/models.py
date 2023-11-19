from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileManager(models.Manager):
    def alive(self):
        self.filter(birthDate='null')


class QuestionManager(models.Manager):
    def match(self, question_id):
        return self.filter(id=question_id)

    def top5(self):
        dicts_of_questions = dict()
        result = []
        for i in Answer.objects.all():
            if (dicts_of_questions.get(i.question, 0) == 0):
                dicts_of_questions[i.question] = 0
            dicts_of_questions[i.question] += 1
        result = [i[0] for i in sorted(dicts_of_questions.items(), key=lambda x: x[1], reverse=True)]
        return result[:5]


    def tag_questions(self, tag):
        t = Tag.objects.filter(label=tag)
        return t


class Question(models.Model):
    topic = models.CharField(max_length=256, default='')
    text = models.TextField()
    author = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', related_name='questions')
    date_written = models.DateField()
    objects = QuestionManager()

    def __str__(self):
        return f'{self.topic}'


class Answer(models.Model):
    text = models.TextField()
    profile = models.ForeignKey('Profile', max_length=256, on_delete=models.PROTECT)
    question = models.ForeignKey('Question', max_length=256, on_delete=models.PROTECT)
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
