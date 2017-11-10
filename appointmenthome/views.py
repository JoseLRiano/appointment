from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User

class IndexView(generic.ListView):
    template_name = 'appointmenthome/index.html'

    def get_queryset(self):
        return User.objects.all()


class InfoView(generic.DetailView):
    model = User
    template_name = 'appointmenthome/info.html'


class UserCreate(CreateView):
    model = User
    fields = ['user_firstname', 'user_lastname','user_phone','user_email','address','city','state']









