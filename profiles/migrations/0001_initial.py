# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=50, null=True, blank=True)),
                ('contact_no', models.CharField(db_index=True, max_length=50, null=True, blank=True)),
                ('skype_id', models.CharField(max_length=50, null=True, blank=True)),
                ('linkedin_id', models.CharField(max_length=50, null=True, blank=True)),
                ('bitbucket_id', models.CharField(max_length=50, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('primary_skills', models.CharField(max_length=255, null=True, blank=True)),
                ('secondary_skills', models.CharField(max_length=255, null=True, blank=True)),
                ('dob', models.DateField(null=True, verbose_name=b'DateOfBirth', blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
