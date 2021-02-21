from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

from .serializers import NoteSerializer, UserSerializer
from .models import Note
from .permissions import IsOwner


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('created_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
