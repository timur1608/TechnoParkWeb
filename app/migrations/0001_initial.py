# Generated by Django 4.2.6 on 2023-11-19 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=256)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='', max_length=256)),
                ('text', models.TextField()),
                ('date_written', models.DateField()),
                ('author', models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.PROTECT, to='app.profile')),
                ('tags', models.ManyToManyField(related_name='questions', to='app.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countOfLikes', models.IntegerField()),
                ('countOfDislikes', models.IntegerField()),
                ('answer', models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.PROTECT, to='app.answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='profile',
            field=models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.PROTECT, to='app.profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.PROTECT, to='app.question'),
        ),
    ]
