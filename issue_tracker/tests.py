from django.test import TestCase
from django.apps import apps
from .apps import IssueTrackerConfig

class TestAccountsConfig(TestCase):
    def test_accounts_app(self):
        self.assertEqual("issue_tracker", IssueTrackerConfig.name)
        self.assertEqual("issue_tracker", apps.get_app_config("issue_tracker").name)
        
class TestViews(TestCase):
    def test_login_page(self):
        page = self.client.get("/issue_tracker/community")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "community.html")
    
    def test_signup_page(self):
        page = self.client.get("/issue_tracker/contact_us")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact_us.html")