from django.urls import path
from tendik.views import dashboardView, pembimbingView

urlpatterns = [
    path('', dashboardView.as_view(), name='index'),
    path('pembimbing', pembimbingView.as_view(), name='pembimbing'),
]