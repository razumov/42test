from django.contrib.auth.models import User
from django.test import TestCase
from django.core.management import call_command
import sys
from StringIO import StringIO
from models import Person, LogModel
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
        
    def test_requests(self):
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
            
    def test_context_processor(self):
        # A response
        response = self.client.get('/')
        # Check if context contains project settings
        self.failUnlessEqual(response.context['settings'].SECRET_KEY, \
            'q^x45_#81=5uxd9&9yp(i86v6zj7^=iyw6+0&%w!7d5t+15$a2')       
       
    def test_edit(self):        
        # Check 'edit'
        response = self.client.get('/edit/')
        # Check response status before auth
        self.failUnlessEqual(response.status_code, 302)
        #Authorization
        User.objects.create_user(username="test",
                                 email="test@test.com",
                                 password="test")
        self.failUnlessEqual(self.client.login(username="test",
                                               password="test"), True)
        
        # A response
        response = self.client.get('/edit/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)

        # Person data
        data = ['Denis', 'Razumov', "Sometext", "telephone"]
        # Data in the reponse content
        for item in data:
            self.failUnlessEqual(item in response.content, True)
        ctx = {'name': 'test_1', 'surname': 'test_2', 'bio': 'test_3',
               'contacts': 'test_4'}
        # Form submitting
        self.client.post('/edit/', ctx)
        response = self.client.get('/edit/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Person data
        data = ['test_1', 'test_2', "test_3", "test_4"]
        # Data in the reponse content
        for item in data:
            self.failUnlessEqual(item in response.content, True)
            
    def test_reversed(self):
        #Authorization
        User.objects.create_user(username="test",
                                 email="test@test.com",
                                 password="test")
        self.failUnlessEqual(self.client.login(username="test",
                                               password="test"), True)
        # A response
        response = self.client.get('/edit/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        # Check if fields was reversed
        self.failIf(response.content.index('id="id_name"') <
                    response.content.index('id="id_bio"'))

    def test_tag(self):
        # A response
        response = self.client.get('/tag/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)               
        # Authorization
        User.objects.create_user(username="test",
                                 email="test@test.com",
                                 password="test")                              
        self.failUnlessEqual(self.client.login(username="test",
                                               password="test"), True)
        # A response
        response = self.client.get('/tag/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        # Check link
        self.assertTrue("Edit object" in response.content)

    def test_modelsinfo(self):
        temp = sys.stderr
        sys.stderr = stderr = StringIO()
        call_command('modelsinfo')
        sys.stderr = temp
        test_string = "<class 'django.contrib.auth.models.User'> " +\
                      "contains 1 objects"
        self.assertTrue(test_string in stderr.getvalue())

    def test_signals(self):
        # Testing "Changed" option
        customer = Person.objects.all()[0]
        customer.name = "Test"
        customer.save()
        log = LogModel.objects.order_by('date')[0]
        self.assertTrue(log.action, "Changed")
        # Testing "Created" option
        customer = Person.objects.create()
        customer.name = "Temp"
        customer.save()
        log = LogModel.objects.order_by('date')[0]
        self.assertTrue(log.action, "Created")
        # Testing "Deleted" option
        customer = Person.objects.get(name='Temp')
        customer.delete()
        log = LogModel.objects.order_by('date')[0]
        self.assertTrue(log.action, "Deleted")
        
    def test_priority(self):
        # Authorization
        User.objects.create_user(username="test",
                                 email="test@test.com",
                                 password="test")
        self.failUnlessEqual(self.client.login(username="test",
                                               password="test"), True)
        # Priority 1 request
        self.client.get('/')
        self.client.logout()
        # Priority 0 request
        self.client.get('/')
        # Context
        ctx = {'priority': '1'}
        # Emulating form submitting
        response = self.client.post('/requests/', ctx)
        self.failIf(response.content.index('0</div>') <
                    response.content.index('1</div>'))
        # Context
        ctx = {'priority': '0'}
        # Emulating form submitting
        response = self.client.post('/requests/', ctx)
        self.failIf(response.content.index('0</div>') >
                    response.content.index('1</div>'))