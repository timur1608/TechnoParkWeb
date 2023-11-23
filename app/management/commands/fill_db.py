from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Question, Like, Answer, Tag
import random


class Command(BaseCommand):
    help = 'Отобразить текст'

    def add_arguments(self, parser):
        parser.add_argument(
            'ratio', type=int
        )

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']
        for i in range(ratio):
            user = User.objects.create_user(f'user{i}')
            profile = Profile(user=user, nickname=f'nickname{i}')
            tag = Tag(label=f'C++{i}')
            tag.save()
            user.save()
            profile.save()

            for j in range(10):
                q = Question(topic=f'what if?...{i * 10 + j}', text=f'What if someone told you to do some programming?{j}',
                             author=profile, date_written=f'2023-{random.randint(1, 12)}-{random.randint(1, 28)}')
                q.save()
                q.tags.add(tag)
                for k in range(9):
                    a = Answer(text=f'hello, world{(i * 10 + j) * 10 + k}', profile=profile, question=q, is_correct=False)
                    a.save()
                    l = Like(profile=profile, question=q, value=random.choice(['1', '-1']))
                    l.save()

                    q.like_count += int(l.value)
                    q.answers_count += 1

                    q.save()
                    l2 = Like(profile=profile, answer=a, value=random.choice(['1', '-1']))
                    l2.save()
                    a.like_count += int(l2.value)
                    a.save()
                a = Answer(text=f'hello, world{10 * i + j}', profile=profile, question=q, is_correct=True)
                a.save()
                l = Like(profile=profile, question=q, value=random.choice(['1', '-1']))
                l.save()
                q.like_count += int(l.value)
                q.answers_count += 1
                q.save()
                l2 = Like(profile=profile, answer=a, value=random.choice(['1', '-1']))
                l2.save()
                a.like_count += int(l2.value)
                a.save()
