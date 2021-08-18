from django.test import TestCase
from .forms import CallbackFormForm

# Create your tests here.
from callbackform.models import CallbackForm


class CallbackFormTestCase(TestCase):
    def setUp(self):
        CallbackForm.objects.create(name='Test name 1',
                                    phone_number='111111',
                                    company='Test company 1',
                                    email='test1@test.com',
                                    subject='Test subject 1',
                                    problem_description='This is an example of the problem description for test case 1',
                                    support_datetime='2021-08-17 19:00')

        CallbackForm.objects.create(name=' ',
                                    phone_number='222222',
                                    company='Test company 2',
                                    email='test2@test.com',
                                    subject='Test subject 2',
                                    problem_description='This is an example of the problem description for test case 2',
                                    support_datetime='2021-08-17 18:30')

    def test_if_data_entered_correctly_into_database(self):
        """This test is used to check if data was properly saved to the database"""
        test_record_1 = CallbackForm.objects.get(name="Test name 1")
        self.assertEqual(test_record_1.name, 'Test name 1')
        self.assertEqual(test_record_1.phone_number, '111111')
        self.assertEqual(test_record_1.company, 'Test company 1')
        self.assertEqual(test_record_1.email, 'test1@test.com')
        self.assertEqual(test_record_1.subject, 'Test subject 1')
        self.assertEqual(test_record_1.problem_description,
                         'This is an example of the problem description for test case 1')
        self.assertEqual(test_record_1.support_datetime.strftime('%Y-%m-%d %H:%M'), '2021-08-17 19:00')

    def test_when_submitting_empty_required_fields(self):
        """Test if there are errors after submitting form with missing required fields"""

        all_required_fields_list = ['name', 'email', 'subject', 'problem_description']
        no_name = {'email': 'test2@test.com',
                   'subject': 'Test subject 2',
                   'problem_description': 'This is an example of the problem description for test case 2'}

        no_email = {'name': 'Test case 2',
                    'subject': 'Test subject 2',
                    'problem_description': 'This is an example of the problem description for test case 2'}

        form_no_name = CallbackFormForm(no_name)
        form_no_email = CallbackFormForm(no_email)
        form_no_name.is_valid()
        form_no_email.is_valid()
        self.assertEqual(len(list(form_no_name.cleaned_data.keys())), len(all_required_fields_list) - 1)
        self.assertEqual(len(list(form_no_email.cleaned_data.keys())), len(all_required_fields_list) - 1)

