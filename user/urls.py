from django.urls import path
from user import views
urlpatterns = [ path('account/profile/', views.UserAccountUpdateView.as_view()) ]