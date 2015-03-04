from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from base.forms import IssueForm, SublocationFormSet, UserFormSet 
from django.views.generic.edit import FormView
from base.models import Issue, Tag, User, Sublocation, City, Sector, Skill, Timeline
import time, datetime
from django.views.generic import CreateView, View



def digitalIndia(request):
    return render(request, 'digitalIndia.html');


def signup(request):
    return render(request, 'signup.html', {"formUrl":'https://docs.google.com/a/stanford.edu/forms/d/1wnZAGL2sxKwnA5wcs5HEZ1X4Qw-CNJEHEg6jBoV8N7I/viewform'});
#	return redirect('https://docs.google.com/a/stanford.edu/forms/d/1wnZAGL2sxKwnA5wcs5HEZ1X4Qw-CNJEHEg6jBoV8N7I/viewform');


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html');



def viewTickets(request):
    issues = Issue.objects.all();
    return render(request, 'viewTickets.html', {"issues", issues});



def createIssue(request):
    IssueFormSet = modelformset_factory(Issue);
    fields = [];
    # TagFormSet = modelformset_factory(Tag);
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST["form-0-pub_datetime"] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
       # issueFormset = IssueFormSet(initial={'pub_datetime': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), 'followers': "null", 'follower_count': '0', 'upvotes': '0' }, data=request.POST, files=request.FILES);
        issueFormset = IssueFormSet(data=request.POST, files=request.FILES)
        print(request.POST["form-0-pub_datetime"]);
        request.POST._mutable = mutable
        # tagFormset = TagFormSet(request.POST, request.FILES)
        # print(tagFormset);
        print("POST")
        # print(request.POST["form-0-upvotes"]);

        if issueFormset.is_valid():
            model_instance = issueFormset.save(commit=False)
            #model_instance.pub_date =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
            #model_instance.save()          
            print("SAVED NEW ISSUE") 
            return redirect('http://google.com')
        else:
            print("NOT VALID")
        # if tagFormset.is_valid():
        #     print "model";
    else:
        print("GET") 
        issueFormset = IssueFormSet();
        #issueFormset = IssueFormSet(initial={'pub_datetime': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), 'followers': "null", 'follower_count': 0, 'upvotes': 0 });
        print(issueFormset);
        # tagFormset = TagFormSet()
    return render_to_response("createIssue.html", {
        "issueFormset": issueFormset }, context_instance=RequestContext(request))




# class IssueCreateView(CreateView):
#     template_name = 'createIssue.html'
#     model = Issue
#     form_class = IssueForm
#     success_url = 'success/'

#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates blank versions of the form
#         and its inline formsets.
#         """
#         self.object = None
#         form_class = self.get_form_class();
#         form = self.get_form(form_class)
#         sublocation_form = SublocationFormSet()
#         user_form = UserFormSet()
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   sublocation_form=sublocation_form,
#                                   user_form=user_form))

#     def post(self, request, *args, **kwargs):
#         """
#         Handles POST requests, instantiating a form instance and its inline
#         formsets with the passed POST variables and then checking them for
#         validity.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         sublocation_form = SublocationFormSet(self.request.POST)
#         user_form = UserFormSet(self.request.POST)
#         if (form.is_valid() and sublocation_form.is_valid() and
#             user_form.is_valid()):
#             return self.form_valid(form, user_form, sublocation_form)
#         else:
#             return self.form_invalid(form, user_form, sublocation_form)

#     def form_valid(self, form, sublocation_form, user_form):
#         """
#         Called if all forms are valid. Creates a Recipe instance along with
#         associated Ingredients and Instructions and then redirects to a
#         success page.
#         """
#         self.object = form.save()
#         sublocation_form.instance = self.object
#         sublocation_form.save()
#         user_form.instance = self.object
#         user_form.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def form_invalid(self, form, ingredient_form, instruction_form):
#         """
#         Called if a form is invalid. Re-renders the context data with the
#         data-filled forms and errors.
#         """
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   sublocation_form=sublocation_form,
#                                   user_form=user_form))




