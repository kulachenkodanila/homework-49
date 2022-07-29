from django.urls import path

from webapp.views import WorkView, CreateWork, DeleteWork, UpdateWork
from webapp.views.projects import ProjectView, IndexView_project, UpdateProject, DeleteProject, CreateProject

urlpatterns = [
    path('', IndexView_project.as_view(), name="index"),
    path('project/<int:pk>/', ProjectView.as_view(), name="project_view"),
    path('project/<int:pk>/update/', UpdateProject.as_view(), name="update_project"),
    path('project/<int:pk>/delete/', DeleteProject.as_view(), name="delete_project"),
    path('project/add/', CreateProject.as_view(), name="create_project"),
    path('project/<int:pk>/work/add/', CreateWork.as_view(), name="project_work_create"),
    path('work/<int:pk>/', WorkView.as_view(), name="work_view"),
    path('work/<int:pk>/update/', UpdateWork.as_view(), name="update_work"),

    # path('work/add/', CreateWork.as_view(), name="create_work"),
    path('work/<int:pk>/delete/', DeleteWork.as_view(), name="delete_work"),

]
