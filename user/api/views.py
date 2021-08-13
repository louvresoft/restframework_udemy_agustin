from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from rest_framework.permissions import IsAuthenticated
from user.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from user.models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, requests):
        serializer = UserSerializer(requests.user)
        return Response(serializer.data)

    def put(self, requests):
        user = User.objects.get(id=requests.user.id)
        serializer = UserUpdateSerializer(user, requests.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
