from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
app_name='pyp'
urlpatterns = [
    path('', views.index, name='index'),
    path('timeline.html', views.timeline, name='timeline'),
    path('<slug:faculty_code>/module/',views.modules, name = 'modules'),
    path('<slug:faculty_code>/module/<slug:module_code>',views.viewYear, name='viewYear'),
    path('<slug:faculty_code>/module/<slug:module_code>/<int:year_id>',views.viewAnswer ,name='viewAnswer'),
    path('<slug:faculty_code>/module/<slug:module_code>/<int:year_id>/<int:answerf_id> ',views.downloadAnswer,name='downloadAnswer'),
    path('<slug:faculty_code>/module/<slug:module_code>/<int:year_id>/comments/<int:answer_id>',views.viewComment,name='viewComment'),
]   
