from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import models
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from members.models import members, form_members


# Create your views here.
def view_member(request):
    data = members.objects.all()
    templates = loader.get_template('index.html')
    context = {
        "data": data
    }
    return HttpResponse(templates.render(context, request), )


def view_detail(request, id):
    data = members.objects.get(id=id)
    templates = loader.get_template('detail.html')
    context = {
        "data": data
    }
    print(data)
    return HttpResponse(templates.render(context, request), )


def view_add(request):
    templates = loader.get_template('insert.html')
    return HttpResponse(templates.render({}, request), )


def add_post(request):
    form_model = form_members(request.POST)
    if form_model.is_valid():
        form_model.save()
    return HttpResponseRedirect("/")


def edit_post(request, id):
    data = members.objects.get(id=id)
    form_model = form_members(request.POST, instance=data)
    if form_model.is_valid():
        form_model.save()
    return HttpResponseRedirect("/")


def json(request):
    data = members.objects.all().values()
    return HttpResponse(data)


@api_view(['GET'])
def getuser(request):
    data = members.objects.all().values()
    return Response({"data": data})
