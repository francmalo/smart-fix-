from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('adminView', views.admin_dashboard, name='admin_dashboard'),
    path('clientView', views.client_dashboard, name="client_dashboard"),
    path('technicianView', views.technician_dashboard,
         name="technician_dashboard"),
    path('addjob', views.addjob, name="addjob"),
    path('moreinfo/<uuid:id>/',views.more_info_view,name="more_info_view"),
    path('bid/<uuid:id>/',views.bidd,name="bidd"),
    path('allclients',views.get_all_clients,name="get_all_clients"),
    path('alltechnicians',views.get_all_technicians,name="get_all_technicians"),
    path('assignjob/<uuid:id>/<uuid:job_id>/',views.assign_job,name="assign_job"),
    path('closejob/<uuid:id>/',views.close_job,name="close_job"),
]
