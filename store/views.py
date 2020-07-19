from django.views.generic import ListView, DetailView, CreateView
from .models import Car, Category, Tag
from django.db.models import F
from .forms import CarForm
from django.shortcuts import render


class Home(ListView):
    model = Car
    template_name = 'store/index.html'
    context_object_name = 'cars'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Popular Car'
        return context


class PostsByCategory(ListView):
    template_name = 'store/index.html'
    context_object_name = 'cars'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Car.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    template_name = 'store/index.html'
    context_object_name = 'cars'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Car.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts by tag: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class GetPost(DetailView):
    model = Car
    template_name = 'store/single.html'
    context_object_name = 'car'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class Search(ListView):
    template_name = 'store/search.html'
    context_object_name = 'cars'
    paginate_by = 4

    def get_queryset(self):
        return Car.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

class CreateCars(CreateView):
    form_class = CarForm
    template_name = 'store/add_new_car.html'
    raise_exception = True
