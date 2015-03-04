from django import forms
from base.models import Issue, City, Sublocation, Sector, Timeline, Tag, User, Skill, Solution
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['city_name'];



class SectorForm(ModelForm):
    class Meta:
        model = Sector
        fields = ['sector_name'];


class SublocationForm(ModelForm):
    class Meta:
        model = Sublocation
        fields = ['sublocation_name'];



class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name', 'popularity'];


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_email'];



class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name'];



class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['issue', 'solution_text', 'upvotes', 'skills_required'];





class IssueForm(ModelForm):
	pub_datetime = forms.CharField(required=False);
	followers = forms.ModelMultipleChoiceField(User, required=False);
	upvotes = forms.IntegerField(required=False);
	follower_count = forms.IntegerField(required=False);

	class Meta:
		model = Issue
        fields = [ 'issue_name', 'issue_text', 'pub_datetime', 'followers', 'follower_count', 'upvotes', 'sublocation','city', 'tags', 'user', 'sector'  ];

   	def __init__(self, *args, **kwargs):
	    super(IssueForm, self).__init__(*args, **kwargs);
	    for key in self.fields:
	    	self.fields[key].required = False

#TagFormSet = inlineformset_factory( Tag, Issue)
SublocationFormSet = inlineformset_factory( Sublocation, Issue)
UserFormSet = inlineformset_factory( User, Issue)

