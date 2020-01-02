from django.test import TestCase
from django.apps import apps
from .apps import IssueTrackerConfig
from .models import Bug
from .forms import BugCreationForm, CommentForm

class TestIssueTrackerConfig(TestCase):
    # testing app 
    def test_accounts_app(self):
        self.assertEqual("issue_tracker", IssueTrackerConfig.name)
        self.assertEqual("issue_tracker", apps.get_app_config("issue_tracker").name)
        
class TestViews(TestCase):
    # testing rendering of communtiy page
    def test_communtiy_page(self):
        page = self.client.get("/issue_tracker/community")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "community.html")
    
    def test_contact_us_page(self):
    # testing rendering of contact us page
        page = self.client.get("/issue_tracker/contact_us")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact_us.html")

class TestBugForm(TestCase):
    # testing bug creation
    def test_bug_form(self):
        # test form is validating
        form = BugCreationForm({'title': 'Test', 'content': 'Testing the test', 'author': 'Janed'})
        self.assertTrue(form.is_valid)
    
    def test__is_required_title(self):
        # Test if username is required
        form = BugCreationForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

    def test_is_required_content(self):
        # Test is email is required
        form = BugCreationForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])

    def test_bug_status(self):
        # test if default status is todo
        bug = Bug(title="Testing bug creation", status="To Do")
        bug.save()
        self.assertEqual(bug.title, "Testing bug creation")
        self.assertEqual(bug.status, "To Do")
        
    def test_bug_comment(self):
        # testing bug comments
        form = CommentForm({'text': 'test comments'})
        self.assertTrue(form.is_valid)
        
        
        