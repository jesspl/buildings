# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets, permissions
# from p1.models import Calles, Semaforos, Manzanas
# from p1.serializers import CallesSerializer, SemaforosSerializer, ManzanasSerializer

# class CallesModelViewSet(viewsets.ModelViewSet):
#     queryset = Calles.objects.all()
#     serializer_class = CallesSerializer
#     permission_classes = [permissions.AllowAny]

# class SemaforosModelViewSet(viewsets.ModelViewSet):
#     queryset = Semaforos.objects.all()
#     serializer_class = SemaforosSerializer
#     permission_classes = [permissions.AllowAny]

# class ManzanasModelViewSet(viewsets.ModelViewSet):
#     queryset = Manzanas.objects.all()
#     serializer_class = ManzanasSerializer
#     permission_classes = [permissions.AllowAny]

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from p1.models import Calles, Semaforos, Manzanas
from p1.serializers import CallesSerializer, SemaforosSerializer, ManzanasSerializer

class CallesModelViewSet(viewsets.ModelViewSet):
    queryset = Calles.objects.all()
    serializer_class = CallesSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SemaforosModelViewSet(viewsets.ModelViewSet):
    queryset = Semaforos.objects.all()
    serializer_class = SemaforosSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ManzanasModelViewSet(viewsets.ModelViewSet):
    queryset = Manzanas.objects.all()
    serializer_class = ManzanasSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]