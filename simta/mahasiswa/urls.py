from django.urls import path
from mahasiswa.views import *

urlpatterns = [
    path('', dashboardViewMhs.as_view(), name='index'),
    path('pembimbing', pembimbingViewMhs.as_view(), name='pembimbing'),
    path('pengajuan-judul', pengajuanJudulViewMhs.as_view(), name='pembimbing'),
]