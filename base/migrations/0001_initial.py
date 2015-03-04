# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_name', models.CharField(max_length=200, null=True)),
                ('issue_text', models.CharField(max_length=200)),
                ('pub_datetime', models.DateTimeField(verbose_name=b'datetime published')),
                ('upvotes', models.IntegerField(default=0)),
                ('follower_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sector_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solution_text', models.CharField(max_length=20)),
                ('upvotes', models.IntegerField(default=0)),
                ('issue', models.ForeignKey(to='base.Issue')),
                ('skills_required', models.ManyToManyField(to='base.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sublocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sublocation_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=200)),
                ('popularity', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeline_heading', models.CharField(max_length=200)),
                ('timeline_description', models.CharField(max_length=10000)),
                ('date_posted', models.DateTimeField(verbose_name=b'datetime posted')),
                ('date_completed', models.DateTimeField(verbose_name=b'datetime completed')),
                ('location', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='timeline',
            name='creator',
            field=models.ForeignKey(to='base.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeline',
            name='issue',
            field=models.ForeignKey(to='base.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeline',
            name='skills_required',
            field=models.ManyToManyField(to='base.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeline',
            name='tags',
            field=models.ManyToManyField(to='base.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='followers',
            field=models.ManyToManyField(related_name='issue_follower', to='base.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='sector',
            field=models.ForeignKey(to='base.Sector', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='sublocation',
            field=models.ForeignKey(to='base.Sublocation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(to='base.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(to='base.User'),
            preserve_default=True,
        ),
    ]
