from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ..models import Notes
from .serializers import PostSerializer, NotesSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self, pk=None):
        model = PostSerializer.Meta.model
        if pk is None:
            query = model.objects.filter(is_archived=False)
            return query
        query = model.objects.filter(is_archived = False, id=pk)
        return query
    

class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = NotesSerializer
    
    def get_queryset(self, pk=None):
        model = NotesSerializer.Meta.model
        if pk is None:
            query = model.objects.filter(is_archived=False)
            return query
        query = model.objects.get(is_archived=False, id=pk)
        return query
    
    @action(detail=True, methods=['post'], url_path='fijado')
    def fijado(self,request,pk=None):
        note = Notes.objects.get(is_archived =True)

        if note:
            note.is_fijado = not note.is_fijado
            note.save()
            boolean = note.is_fijado
            return Response({"message": f"Nota {"Fijada" if boolean else "Desfijada"}"}, status=status.HTTP_201_CREATED)
        return Response({"error": "no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
    

