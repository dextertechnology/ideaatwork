from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from django.contrib.auth import authenticate

from .models import Idea, Vote
from .serializers import (
    IdeaSerializer,
    VoteSerializer,
    UserSerializer
)


class IdeaViewSet(viewsets.ModelViewSet):
    pass


class CreateVote(APIView):
    pass


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                "token": user.auth_token.key
            })
        else:
            return Response(
                {
                    "error": "Wrong Credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
