from django.urls import path
from django.views.generic import TemplateView, RedirectView

from webapp.views import IndexView, WorkView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('work/<int:pk>/', WorkView.as_view(), name="work_view"),

]
