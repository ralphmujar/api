#url_shortener/views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.http import JsonResponse




from .models import Url
from .serializers import UrlSerializer


class UrlCreate(APIView):

    serializer_class = UrlSerializer

    def post(self, request):
        from hashlib import md5 

        long_url = request.data.get('url')
        l = str(long_url)
        h = md5(l.encode()).hexdigest()[:10]


        data = {'short_url': h, 'long_url': l}

        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('http://u.c/'+str(data['short_url']), safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UrlDetail(RetrieveUpdateDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


