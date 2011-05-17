from django.test import TestCase
from models import Person
from models import Request


class SimpleTest(TestCase):

    def test_contacts(self):
        # A response
        response = self.client.get('/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check page information
        p = Person.objects.get(pk=1)
        self.assertContains(response, p.name, 1)
        self.assertContains(response, p.surname, 1)
        self.assertContains(response, p.bio, 1)
        self.assertContains(response, p.contacts, 1)

        # A response
        response = self.client.get('/requests/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'requests.html', msg_prefix='')
        # Check requests
        requests = Request.objects.order_by('-date')[:10]
        for request in response.context['requests']:
            self.assertTrue(request in requests)
