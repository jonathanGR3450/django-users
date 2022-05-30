from django.urls import path

from messager.views import ThreadListView, ThreadDetailView
from messager import views

messager_urlpatterns = ([
    path('thread/', ThreadListView.as_view(), name='thread'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='detail'),
    path('thread/<int:pk>/send/', views.send_message_to_thread, name='send'),
    path('thread/init/<int:pk>/', views.create_thread_for_user, name='init'),
], 'messager')
