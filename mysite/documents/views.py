from django.shortcuts import render
from .models import Documentations, Groups
from django.views.generic import DetailView


def documents(request):
    return render(request, 'documents/documents.html')


def docs_page(request):
    docs = Documentations.objects.all()
    groups = Groups.objects.all()
    return render(request, 'documents/documents.html', {'docs': docs, 'groups': groups})


def groups_item(request):
    groups = Groups.objects.all()
    return render(request, 'documents/documents.html', {'groups': groups})


class DocsDetailView(DetailView):
    model = Documentations
    template_name = 'documents/documents.html'
    context_object_name = 'docs'
