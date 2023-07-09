from rest_framework import generics, permissions,status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,UserProfileSerializer,MedicalHistorySerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import UserProfile,MedicalHistory
from django.db import IntegrityError

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)









class UserProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            error_message = "A userprofile already exists for this user."
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method \"POST\" not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserProfileRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        self.perform_destroy(profile)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# class MedicalHistoryListCreateView(generics.ListCreateAPIView):
#     serializer_class = MedicalHistorySerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return MedicalHistory.objects.filter(user=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class MedicalHistoryListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicalHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicalHistory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            error_message = "A medical history already exists for this user."
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method \"POST\" not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class MedicalHistoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicalHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return MedicalHistory.objects.get(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        medicalhistory = self.get_object()
        self.perform_destroy(medicalhistory)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
