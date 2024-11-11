from django.shortcuts import get_object_or_404, render
from linkshortener.models import Links
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class LinksAPIView(APIView):
    def get(self, request, link_id):
        link_db = get_object_or_404(Links, id=link_id)
        context = {
            'full_link': link_db.full_link
        }
        return Response(context)
    
    def post(self, request):
        url_in = request.data.get('url')
        if url_in is None:
            return Response({'Bad request': 'No key "url" in dictionary!'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        if Links.objects.exists():
            last_id = Links.objects.last().id
        else:
            last_id = 0
        short_url = f'http://localhost:8000/{last_id + 1}' 
        context = {
            'full_link': url_in,
            'short_link': short_url,
        }
        try:
            Links.objects.create(
                full_link = context['full_link'],
                short_link = context['short_link']
            )
        except:
            return Response({'Database Error': 'New record in the database has not been created!'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'short_link': context['short_link']}, status=status.HTTP_201_CREATED)


