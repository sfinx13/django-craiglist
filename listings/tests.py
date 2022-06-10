from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.timezone import utc
from django.core.files.uploadedfile import InMemoryUploadedFile
from listings.models import Category
from listings.models import Advert
from listings.models import TEST_IMAGE
from authentification.models import User
from unittest import mock
from datetime import datetime
from io import BytesIO
import tempfile
import base64


class ListingsHomeViewTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse("home"))
        html = response.content.decode("utf8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("<title>Craiglist</title>", html)
        self.assertTrue(html.endswith("</html>"))

class CategoryModelTest(TestCase):
    @mock.patch("django.utils.timezone.now")
    def test_default_values(self, mock_now):
        mock_date = datetime(2022, 6, 1, 0, 0, 0).replace(tzinfo=utc)
        mock_now.return_value = mock_date

        category = Category.objects.create(title="Furnitures", slug="furnitures")
        self.assertEqual(category.title, "Furnitures")
        self.assertEqual(category.slug, "furnitures")
        self.assertEqual(category.created_at, mock_date)
        self.assertEqual(category.updated_at, mock_date)

class AdvertModelTest(TestCase):
    @mock.patch("django.utils.timezone.now")
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_default_values(self, mock_now):
        mock_date = datetime(2022, 6, 1, 0, 0, 0).replace(tzinfo=utc)
        mock_now.return_value = mock_date

        in_memory_image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name="tempfile",
            name="tempfile.png",
            content_type="image/png",
            size=len(TEST_IMAGE),
            charset="utf-8",
        )

        category = Category.objects.create(title="Furnitures", slug="furnitures")

        published_by = User.objects.create(
            first_name="Doe",
            last_name="John",
            email="john.doe@yopmail.com",
            password="123456",
        )
        advert = Advert.objects.create(
            title="Grey Four-Cushion Convertible Sofa",
            description="""
                Lorem ipsum dolor sit amet, consectetur 
                adipiscing elit, sed do eiusmod tempor 
                incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud 
                exercitation ullamco laboris nisi ut aliquip 
                ex ea commodo consequat. Duis aute irure 
                dolor in reprehenderit in voluptate velit 
                esse cillum dolore eu fugiat nulla pariatur. 
                """,
            price=298.50,
            zipcode=13016,
            ended_at=datetime(2023, 1, 1, 0, 0, 0).replace(tzinfo=utc),
            picture=in_memory_image,
            category=category,
            published_by=published_by,
        )

        self.assertEqual(advert.title, "Grey Four-Cushion Convertible Sofa")
        self.assertEqual(advert.price, 298.50)
        self.assertEqual(advert.zipcode, 13016)
        self.assertEqual(advert.ended_at, datetime(2023, 1, 1, 0, 0, 0).replace(tzinfo=utc))
        self.assertIn("Lorem ipsum", advert.description)
        self.assertIsInstance(advert.category, Category)        
        self.assertIn('.png', advert.picture.name)
        self.assertEqual(advert.created_at, mock_date)
        self.assertEqual(advert.updated_at, mock_date)
