from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path, include
app_name='todoapp'


urlpatterns = [
    path('',views.demo,name="demo"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update_task/<int:tid>/',views.update_task,name="update_task"),
    path('home/',views.tasklistview.as_view(),name='home'),
    path('detail/<int:pk>/',views.taskdetailview.as_view(),name='detail'),
    path('update/<int:pk>/',views.taskupdateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.taskdetailview.as_view(),name='delete'),
    ]

