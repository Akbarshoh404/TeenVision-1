from django_filters import rest_framework as django_filters
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


from core.models import Program
from core.serializers import ProgramSerializer
from core.filters import ProgramFilter


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProgramFilter
    search_fields = ['title', 'desc']

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def like(self, request, pk=None):
        program = self.get_object()
        user = request.user
        if program in user.liked_programs.all():
            user.liked_programs.remove(program)
            return Response({'message': 'Program unliked'}, status=status.HTTP_200_OK)
        else:
            user.liked_programs.add(program)
            return Response({'message': 'Program liked'}, status=status.HTTP_200_OK)
