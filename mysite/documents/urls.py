from django.urls import path
from . import views

urlpatterns = [
    path('', views.docs_page),
    path('<int:pk>', views.DocsDetailView.as_view(), name='docs-detail')
]
