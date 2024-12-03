import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planetarium.settings")


from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import (
    AstronomyShow,
    ShowSession,
    PlanetariumDome,
    Reservation,
)
from core.serializers import (
    AstronomyShowSerializer,
    ShowSessionSerializer,
)

ASTRONOMY_SHOW_URL = reverse("planetarium:astronomyshow-list")
SHOW_SESSION_URL = reverse("planetarium:showsessions-list")


def sample_astronomy_show(**params):
    defaults = {
        "title": "Sample Show",
        "description": "A fascinating journey through the stars.",
    }
    defaults.update(params)
    return AstronomyShow.objects.create(**defaults)


def sample_planetarium_dome(**params):
    defaults = {"name": "Main Dome", "rows": 10, "seats_in_row": 15}
    defaults.update(params)
    return PlanetariumDome.objects.create(**defaults)


def sample_show_session(**params):
    astronomy_show = sample_astronomy_show()
    planetarium_dome = sample_planetarium_dome()

    defaults = {
        "show_time": "2024-12-02T15:00:00Z",
        "astronomy_show": astronomy_show,
        "planetarium_dome": planetarium_dome,
    }
    defaults.update(params)
    return ShowSession.objects.create(**defaults)


class UnauthenticatedPlanetariumApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required_for_astronomy_show(self):
        res = self.client.get(ASTRONOMY_SHOW_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedPlanetariumApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com", "testpassword"
        )
        self.client.force_authenticate(self.user)

    def test_list_astronomy_shows(self):
        sample_astronomy_show()
        sample_astronomy_show()

        res = self.client.get(ASTRONOMY_SHOW_URL)

        shows = AstronomyShow.objects.all().order_by("id")
        serializer = AstronomyShowSerializer(shows, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_reservation(self):
        show_session = sample_show_session()
        payload = {"show_session": show_session.id}

        res = self.client.post(reverse("planetarium:reservation-list"), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        reservation = Reservation.objects.get(id=res.data["id"])
        self.assertEqual(reservation.user, self.user)
        self.assertEqual(reservation.show_session, show_session)


class AdminPlanetariumApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            "admin@test.com", "adminpassword"
        )
        self.client.force_authenticate(self.admin_user)

    def test_create_astronomy_show(self):
        payload = {
            "title": "New Show",
            "description": "A new fascinating show about the universe.",
        }

        res = self.client.post(ASTRONOMY_SHOW_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        show = AstronomyShow.objects.get(id=res.data["id"])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(show, key))


class ShowSessionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            "admin@test.com", "adminpassword"
        )
        self.client.force_authenticate(self.admin_user)

    def test_list_show_sessions(self):
        sample_show_session()
        sample_show_session()

        res = self.client.get(SHOW_SESSION_URL)

        sessions = ShowSession.objects.all().order_by("id")
        serializer = ShowSessionSerializer(sessions, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_show_session(self):
        astronomy_show = sample_astronomy_show()
        planetarium_dome = sample_planetarium_dome()
        payload = {
            "show_time": "2024-12-05T10:00:00Z",
            "astronomy_show": astronomy_show.id,
            "planetarium_dome": planetarium_dome.id,
        }

        res = self.client.post(SHOW_SESSION_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        session = ShowSession.objects.get(id=res.data["id"])
        self.assertEqual(session.astronomy_show, astronomy_show)
        self.assertEqual(session.planetarium_dome, planetarium_dome)
