
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import TODO
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    # simple ViewSet for CRUD for todo app.

    queryset = TODO.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [
      DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
    ]
    filterset_fields = ("title", "user", "is_finished")
    search_fields = ("title")
    ordering_fields = ("is_finished", "created_at", "updated_at")

