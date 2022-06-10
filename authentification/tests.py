from django.test import TestCase
from authentification.models import User
from datetime import datetime
from unittest import mock
from django.utils.timezone import utc


class UserModelTest(TestCase):
    @mock.patch("django.utils.timezone.now")
    def test_default_values(self, mock_now):
        mock_date = datetime(2022, 6, 1, 0, 0, 0).replace(tzinfo=utc)
        mock_now.return_value = mock_date

        user = User.objects.create(
            first_name="Doe",
            last_name="John",
            email="john.doe@yopmail.com",
            password="123456",
        )

        self.assertEqual(user.email, "john.doe@yopmail.com")
        self.assertEqual(user.username, None)
        self.assertEqual(user.created_at, mock_date)
        self.assertEqual(user.updated_at, mock_date)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

