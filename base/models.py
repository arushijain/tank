from django.db import models
from django.forms import ModelForm


#For all field references go here : https://docs.djangoproject.com/en/1.7/ref/models/fields/

class Sector(models.Model):
    sector_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.sector_name;


class City(models.Model):
    city_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.city_name;


class Sublocation(models.Model):
    sublocation_name = models.CharField(max_length=200)
    #city = models.ForeignKey(City, null=True, blank=True);
    def __unicode__(self):
        return self.sublocation_name;



class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    popularity = models.IntegerField(default=0);
    def __unicode__(self):
        return self.tag_name;



class User(models.Model):
    user_email = models.EmailField();
    def __unicode__(self):
        return self.user_email;


class Issue(models.Model):
    issue_name = models.CharField(max_length=200, null=True);
    issue_text = models.CharField(max_length=200);
    pub_datetime = models.DateTimeField('datetime published');
    upvotes = models.IntegerField(default=0);
    sublocation = models.ForeignKey(Sublocation);
    tags = models.ManyToManyField(Tag);
    user = models.ForeignKey(User);
    sector = models.ForeignKey(Sector, null=True);
    followers = models.ManyToManyField(User, related_name='issue_follower');
    follower_count = models.IntegerField(default=0);
    def __unicode__(self):
        return self.issue_text;


class Skill(models.Model):
    skill_name = models.CharField(max_length=200);
    def __unicode__(self):
        return self.skill_name;


class Solution(models.Model):
    issue = models.ForeignKey(Issue);
    solution_text = models.CharField(max_length=20);
    upvotes = models.IntegerField(default=0);
    skills_required = models.ManyToManyField(Skill);
    def __unicode__(self):
        return self.solution_text;


class Timeline(models.Model):
    timeline_heading = models.CharField(max_length=200);
    timeline_description = models.CharField(max_length=10000);
    date_posted = models.DateTimeField('datetime posted');
    date_completed = models.DateTimeField('datetime completed');
    location = models.CharField(max_length=200);
    skills_required = models.ManyToManyField(Skill);
    tags = models.ManyToManyField(Tag);
    issue = models.ForeignKey(Issue);
    creator = models.ForeignKey(User);
