from django_filters import rest_framework as django_filters
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser


from core.models import Program
from core.serializers import ProgramSerializer, LikeProgramSerializer
from core.filters import ProgramFilter


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.active.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    lookup_field = 'slug'
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProgramFilter
    search_fields = ['title', 'desc']

    @action(detail=False, methods=['get'])
    def tutorials(self, request):
        tutorials = self.queryset.filter(type='tutorial')

        page = self.paginate_queryset(tutorials)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(tutorials, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def programs(self, request):
        programs = self.queryset.exclude(type='tutorial')
        page = self.paginate_queryset(programs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly], serializer_class=LikeProgramSerializer)
    def like(self, request, slug=None):
        program = self.get_object()
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "Ro‘yxatdan o‘ting."}, status=401)

        if program in user.liked_programs.all():
            user.liked_programs.remove(program)
            return Response({"message": "Unlike"})

        user.liked_programs.add(program)
        return Response({"message": "Like"})
