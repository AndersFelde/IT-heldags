from django.shortcuts import render
#  from webpage.models import TestModal


def bildeGjetting(request):
    return render(request, "webpage/bildeGjetting.html")
