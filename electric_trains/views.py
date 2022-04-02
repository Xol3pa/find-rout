from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from electric_trains.forms import TrainForm
from electric_trains.models import Train


__all__ = (
    'home', 'TrainDetailView', 'TrainListView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView',
)


def home(request):
    return render(request, 'electric_trains/home.html', {})


class TrainListView(ListView):
    paginate_by = 4
    model = Train
    template_name = 'electric_trains/electric_trains.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'electric_trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'electric_trains/create.html'
    success_url = reverse_lazy('electric_trains:home_electric_trains')
    success_message = 'Поезд успешно создан'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'electric_trains/update.html'
    success_url = reverse_lazy('electric_trains:home_electric_trains')
    success_message = 'Поезд успешно отредактирован'


class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    success_url = reverse_lazy('electric_trains:home_electric_trains')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Поезд был успешно удален")
        return self.post(request, *args, **kwargs)









