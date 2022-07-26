from django.urls import path

from webapp.views import WorkView, UpdateWork, CreateWork, DeleteWork
from webapp.views.projects import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('work/<int:pk>/', WorkView.as_view(), name="work_view"),
    path('work/<int:pk>/update/', UpdateWork.as_view(), name="update_work"),
    path('work/add/', CreateWork.as_view(), name="create_work"),
    path('work/<int:pk>/delete/', DeleteWork.as_view(), name="delete_work"),

]
