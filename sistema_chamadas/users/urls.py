from django.urls import path
from .views import RegisterUserView, LoginView, AuthenticatedView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('authenticated/', AuthenticatedView.as_view(), name='authenticated'),
]
