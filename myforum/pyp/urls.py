
from django.contrib import admin
from django.urls import path,include
from . import views
app_name='pyp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:faculty_id>/module/',views.module, name = 'modules'),
    path('<int:faculty_id>/module/submitModule',views.submitModule, name = 'submitModule'),
    path('<int:faculty_id>/module/<int:module_id>',views.viewYear, name='viewYear'),
    path('<int:faculty_id>/module/<int:module_id>/<int:year_id>',views.viewAnswer ,name='viewAnswer'),
    path('<int:faculty_id>/module/<int:module_id>/<int:year_id>/<int:answerf_id> ',views.downloadAnswer,name='downloadAnswer'),
    path('<int:faculty_id>/module/<int:module_id>/<int:year_id>/comments/<int:answer_id>',views.viewComment,name='viewComment'),
]
