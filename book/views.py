from django.views.generic import ListView
from .models import Person
class PersonListView(ListView):
    model = Person
    template_name = 'home.html'