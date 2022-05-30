from django.urls import path
from profiles.views import ProfilesListView, ProfileDetailView

profiles_urlpatterns = ([
    path('', ProfilesListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], 'profiles')
