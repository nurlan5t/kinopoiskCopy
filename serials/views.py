from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import Serial, Comment
from .forms import CommentForm
from serials.models import User
from movies.views import WikipediaView


class SerialsView(generic.ListView):
    template_name = 'serials/list-serials.html'
    queryset = Serial.objects.all()



class SerialDetailView(generic.DetailView):
    model = Serial
    template_name = 'serials/detail-serial.html'
    extra_context = {'form': CommentForm()}


    def post(self, request, pk, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            serial = Serial.objects.get(pk=pk)

            form = CommentForm(request.POST, initial={'serial': serial, 'user': user})
            if form.is_valid():
                form.save()

            return self.get(request, *args, **kwargs)
        else:
            return HttpResponse('No such user!')



class SerialCreateView(generic.CreateView):
    template_name = 'serials/add-serial.html'
    model = Serial
    fields = [
        'title',
        'image',
        'description',
        'duration',
        'age_limit',
    ]
