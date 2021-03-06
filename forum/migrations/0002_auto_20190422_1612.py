# Generated by Django 2.2 on 2019-04-22 16:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 16, 12, 30, 862012)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forum.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 16, 12, 30, 861542)),
        ),
    ]
