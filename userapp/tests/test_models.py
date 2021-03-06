from django.test import TestCase


from .models import Register

class RegisterModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Register.objects.create()

    def test_username_label(self):
        user=Register.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_email_label(self):
        user=Register.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')

    def test_username_max_length(self):
        user=Register.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length,32)

    def test_password_label(self):
        user=Register.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label,'password')