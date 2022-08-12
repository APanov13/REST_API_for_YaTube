# Generated by Django 2.2.16 on 2022-08-11 16:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(on_delete='cascade', related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete='cascade', related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
