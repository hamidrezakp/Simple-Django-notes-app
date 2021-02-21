from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register', views.CreateUserView.as_view(), name='register'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
