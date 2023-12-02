from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from profiles.forms import ProfileForm
from profiles.models import UserProfile
from django.views.generic import CreateView

# Create your views here.


class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
