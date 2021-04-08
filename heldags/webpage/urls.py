from django.urls import path
from .views import index, formPage, lonn, bildeGjetting

urlpatterns = [
    path("", index.index, name="index"),
    path("formPage", formPage.formPage, name="formPage"),
    path("lonn", lonn.lonn, name="lonn"),
    path("bildeGjetting", bildeGjetting.bildeGjetting, name="bildeGjetting"),
]
