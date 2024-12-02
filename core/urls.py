from django.urls import path, include
from rest_framework import routers

from .views import (
    AstronomyShowViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    TicketViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
)

router = routers.DefaultRouter()

router.register("astronomy_shows", AstronomyShowViewSet)
router.register("show_sessions", ShowSessionViewSet, basename="showsessions")
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet, basename="tickets")
router.register("show_themes", ShowThemeViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "planetarium"
