from django.test import TestCase
from django.apps import apps
from .apps import ServicesConfig

class TestServicesConfig(TestCase):
    def test_services_app(self):
        self.assertEqual("services", ServicesConfig.name)
        self.assertEqual("services", apps.get_app_config("services").name)

# class TestViews(TestCase):
#     def test_services_page(self):
#         page = self.client.get("/services/")
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "services.html")