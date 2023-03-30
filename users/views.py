from .models import User
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .forms import RegistrationForm
from django.shortcuts import redirect, render


class UserRegister(TemplateView):
    template_name = "index.html"
    model = User
    
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you subscribing us !! We'll keep you posted on our launch")
        else:
            messages.error(request, form.errors)
        return render(request, "index.html", {"form": form})



class UserData(ListView):
    model = User
    queryset = User.objects.all()
    template_name = "user_list.html"
    context_object_name = "users"