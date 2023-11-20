from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LikeManager(models.Manager):
    def countLikesOfQuestions(self, question_id):
        count = 0
        likes = Like.objects.all()
        dislikes = DisLike.objects.all()
        for i in likes:
            if i.questions.get(question_id, 0):
                count += 1
        for i in dislikes:
            if i.question.get(question_id, 0):
                count -= 1
        return count

    def countLikesOfAnswers(self, answer_id):
        count = 0
        likes = Like.objects.all()
        dislikes = DisLike.objects.all()
        for i in likes:
            if i.answers.get(answer_id, 0):
                count += 1
        for i in dislikes:
            if i.answers.get(answer_id, 0):
                count -= 1
        return count

        return count


class QuestionManager(models.Manager):
    def match(self, question_id):
        return self.filter(id=question_id)

    def top5(self):
        dicts_of_questions = dict()
        for i in Answer.objects.all():
            if (dicts_of_questions.get(i.question, 0) == 0):
                dicts_of_questions[i.question] = 0
            dicts_of_questions[i.question] += 1
        result = [i[0] for i in sorted(dicts_of_questions.items(), key=lambda x: x[1], reverse=True)]
        return result[:5]

    def tag_questions(self, tag):
        t = Tag.objects.filter(label=tag)
        return t

    def get_answers(self, question_id):
        return Answer.objects.filter(question_id=question_id)


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

    def __str__(self):
        return f'{self.nickname}'


class Like(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    answers = models.ManyToManyField('Answer', related_name='like', blank=True, null=True)
    questions = models.ManyToManyField('Question', related_name='like', blank=True, null=True)
    objects = LikeManager()


class DisLike(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    answers = models.ManyToManyField('Answer', related_name='dislike', blank=True, null=True)
    questions = models.ManyToManyField('Question', related_name='dislike', blank=True, null=True)
    objects = LikeManager()
