from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView
from post.forms import postEventForm
from .models  import PostEvent

from .models import PostEvent
# Create your views here.

class postListView(ListView):
    model = PostEvent
    template_name = 'postList.html'

class postDetail(DetailView):
    model = PostEvent
    template_name = 'postDetail.html'

class UserpostDetail(DetailView):
    model = PostEvent
    template_name = 'UserDetailView.html'

class addPostView(CreateView):
    model = PostEvent
    template_name = 'addPost.html'
    form_class = postEventForm

class staffListView(ListView):
    model = PostEvent
    template_name = 'staffPageList.html'
