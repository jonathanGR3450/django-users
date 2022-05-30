from django.urls import path
from . import views
from .views import PagesListView, PageDetailView, PageCreate, PageUpdateView, PageDeleteView

pages_urlpatterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path("create/", PageCreate.as_view(), name="create"),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
], 'pages')