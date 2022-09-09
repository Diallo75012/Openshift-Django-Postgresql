from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from http import HTTPStatus
from users.models import StockInfo
import unittest
import os
import django
#import pytest


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webApp.settings_for_tests.py')
django.setup()

#@pytest.mark.django_db
class TestUserApp(TestCase):
  def setUp(self):
    self.client = Client()
    self.Report = StockInfo.objects.create(user='Michika', codeAction='LVMH', pays='France', industrie='Luxe', resultat='34245667765', potentiel='Bon', montantDividende='12345', commentaires='stock interessant toujours en progression')

  def test_url_works(self):
    url1 = reverse('updateinfo', arg=[1])
    self.assertEqual(url1, '/updateinfo/1')

  def test_template_name_correct(self):
    response = self.client.get(reverse("loginuser"))
    self.assertTemplateUsed(response, "accounts/loginuser.html")

  def test_template_content(self):
    response = self.client.get(reverse("login"))
    self.assertContains(response, "<h3 id='form-title'>LOGIN</h3>")
    self.assertNotContains(response, "<h3 id='form-title'>REGISTER</h3>")

