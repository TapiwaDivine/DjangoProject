from django.test import TestCase
from django.shortcuts import reverse
from django.apps import apps
from .apps import ServicesConfig
from .models import Feature
from .forms import FeatureCreationForm, CommentForm

class TestServicesConfig(TestCase):
    def test_services_app(self):
        self.assertEqual("services", ServicesConfig.name)
        self.assertEqual("services", apps.get_app_config("services").name)

class TestViews(TestCase):
    def test_services_page(self):
        page = self.client.get("/services/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "services.html")

        
class TestFeatureForm(TestCase):
    # testing feature creation form
    def test_feature_form(self):
        # test if form is validating
        form = FeatureCreationForm({'title': 'Test', 'content': 'Testing the test', 'author': 'Janed'})
        self.assertTrue(form.is_valid)
    
    def test__is_required_title(self):
        # Test if username is required
        form = FeatureCreationForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

    def test_is_required_content(self):
        # Test is email is required
        form = FeatureCreationForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])

    def test_feature_status(self):
        # test if default status is todo
        bug = Feature(title="Testing bug creation", status="To Do")
        bug.save()
        self.assertEqual(bug.title, "Testing bug creation")
        self.assertEqual(bug.status, "To Do")
        
    def test_feature_comment(self):
        # testing bug comments
        form = CommentForm({'text': 'test comments'})
        self.assertTrue(form.is_valid)