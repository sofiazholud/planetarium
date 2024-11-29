from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)
from .serializers import (
    AstronomyShowSerializer,
    ShowThemeSerializer,
    PlanetariumDomeSerializer,
    ShowSessionSerializer,
    ReservationSerializer,
    TicketSerializer,
)


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    permission_classes = [IsAdminUser]


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    permission_classes = [IsAdminUser]


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = [IsAdminUser]


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer
    permission_classes = [IsAuthenticated]

    @action(
        methods=["POST"],
        detail=True,
        url_path="reserve",
        permission_classes=[IsAuthenticated],
    )
    def reserve(self, request, pk=None):
        show_session = self.get_object()

        return Response({"message": "Ticket reserved successfully!"}, status=200)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
