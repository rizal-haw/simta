from django.urls import path
from tendik.views import dashboardView, pembimbingView, mahasiswaView, pengajuanJudulView

urlpatterns = [
    path('', dashboardView.as_view(), name='index'),
    path('pembimbing', pembimbingView.as_view(), name='pembimbing'),
    path('mahasiswa', mahasiswaView.as_view(), name='mahasiswa'),
    path('pengajuan-judul', pengajuanJudulView.as_view(), name='mahasiswa'),
]