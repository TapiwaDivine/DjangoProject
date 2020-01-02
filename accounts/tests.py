from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User
from .apps import AccountsConfig
from .forms import UserRegistrationForm, UserLoginForm

class TestAccountsConfig(TestCase):
# Assert that the app is working 
    def test_accounts_app(self):
        self.assertEqual("accounts", AccountsConfig.name)
        self.assertEqual("accounts", apps.get_app_config("accounts").name)
        
class TestViews(TestCase):
    def test_login_page(self):
        #Assert if the login.html is working
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_signup_page(self):
        # Asserts if signup page is working and displaying
        page = self.client.get("/accounts/signup/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "signup.html")
        
class TestSignupForm(TestCase):
    def test_sign_up_(self):
        # Assert if signup from is working well
        form = UserRegistrationForm({'first_name' : 'Jane', 'last_name' : 'doe', 'username' : 'janed', 'email': 'janedoe@test.com' ,'password1' : '123testing', 'password2' : '123testing'})
        self.assertTrue(form.is_valid)
    
    def test__is_required_username(self):
        # Test if username is required
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_is_required_email(self):
        # Test is email is required
        form = UserRegistrationForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_confirm_password(self):
        # checking confirm password is it working
        form = UserRegistrationForm({'password1': '#123testing', 'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'This field is required.'])

    def test_is_matching_passwords(self):
        # checking if passwords match
        form = UserRegistrationForm({'password1': '#12testing', 'password2': 'testing'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])
    
    def setUp(self):
        # Create Users
        self.user_1 = User.objects.create_user('niahm kennedy', 'niahm@test.com', 'tqtqtqtq')
        self.user_2 = User.objects.create_user('kevin hart', 'kevin@hart.com', 'jumanji')
        self.user_3 = User.objects.create_user('Sadio Mane', 'sadio@mane.com', 'liverpool')

class TestLoginForm(TestCase):
    # Testing login form
    def test_login(self):
        # test if user login is working
        form = UserLoginForm({'username': 'Test', 'password': '123testing'})
        self.assertTrue(form.is_valid)


    def test_is_required_login_username(self):
        # checking if username login field is required 
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

        
    def test_is_required_password(self):
        # checking if password login field is required
        form = UserLoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
    