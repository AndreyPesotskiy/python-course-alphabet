from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView
from .models import Profile


class ProfileDetailView(DetailView):
    template_name = 'account/profile.html'
    model = Profile
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Create user
        created_user = form.save()
        # Create profile
        profile = Profile.objects.create(user=created_user)
        # Authenticate User
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('profile', profile.id)
