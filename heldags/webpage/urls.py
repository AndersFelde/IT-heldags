from django.urls import path
from .views import index, lonn, bildeGjetting, terningkast

urlpatterns = [
    path("", index.index, name="index"),
    path("lonn", lonn.lonn, name="lonn"),
    path("bildeGjetting", bildeGjetting.bildeGjetting, name="bildeGjetting"),
    path("terningkast", terningkast.terningkast, name="terningkast"),
]
