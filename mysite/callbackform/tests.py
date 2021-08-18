from django.test import TestCase
from .forms import CallbackFormForm
from callbackform.models import CallbackForm
# Create your tests here.



class CallbackFormTestCase(TestCase):
    def setUp(self):
        CallbackForm.objects.create(name='Test name 1',
                                    phone_number='111111',
                                    company='Test company 1',
                                    email='test1@test.com',
                                    subject='Test subject 1',
                                    problem_description='This is an example of the problem description for test case 1',
                                    support_datetime='2021-08-17 19:00')


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


