from django.urls import path
from .views import EmailUpdated, SignUpView, ProfileUpdate

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdated.as_view(), name='profile_email')
]
