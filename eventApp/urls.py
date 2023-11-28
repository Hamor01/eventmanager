from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'eventApp'


urlpatterns = [
    path('', views.index, name= 'index'),
    path('partner/', views.partner, name='partner'),
    path('award/', views.award, name = 'award'),
    path('contact/', views.contact, name = 'contact'),
    path('schedule/', views.schedule, name = 'schedule'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('ticket/', views.ticket, name='ticket'),
    path('success/', views.success, name = 'success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


