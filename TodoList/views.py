from rest_framework.response import Response
from rest_framework import generics
from todoapp.models import Dog,Breed
from todoapp.serializer import BreedSerializer,DogSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter


class BreedListView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset=Breed.objects.all()
    serializer_class=BreedSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 3
    filter_backends = [SearchFilter]
    search_fields = ['name','size'] 
    
    
class BreedDetailView(generics.RetrieveUpdateDestroyAPIView):
        # authentication_classes = [TokenAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated,IsAdminUser]
        queryset=Breed.objects.all()
        serializer_class=BreedSerializer
        def delete(self, request,pk):
            try:
                return super().delete(request,pk)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class DogListView(generics.ListCreateAPIView):
    queryset=Dog.objects.all()
    serializer_class=DogSerializer
    
class DogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Dog.objects.all()
    serializer_class=DogSerializer
    