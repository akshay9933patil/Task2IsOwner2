from rest_framework.views import APIView
from .serialIers import BlogSerializer, BlogModel
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerPermission


class BlogAPIView(APIView):

    serializer_class = BlogSerializer
    model_class = BlogModel
    permission_classes = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        fetched = self.model_class.objects.all()
        serializer = self.serializer_class(fetched, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class BloagDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel
    permission_classes = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]
