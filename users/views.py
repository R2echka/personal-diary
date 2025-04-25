from django.views.generic import CreateView

from users.forms import RegistrationForm

from .models import User


# Create your views here.
class UserCreate(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "users/registration.html"
    success_url = "/"
