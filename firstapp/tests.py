from django.test import TestCase
from django.contrib.auth import get_user_model


class AuthTests(TestCase):
	def test_register_creates_user_and_redirects(self):
		resp = self.client.post('/register/', data={
			'fname': 'Alice',
			'lname': 'Smith',
			'email': 'alice@example.com',
			'uname': 'alice123',
			'pass1': 'password123',
			'pass2': 'password123',
		})

		# should redirect to login after successful registration
		self.assertRedirects(resp, '/login/')

		User = get_user_model()
		self.assertTrue(User.objects.filter(username='alice123').exists())

	def test_register_duplicate_username(self):
		User = get_user_model()
		User.objects.create_user(username='bob', email='bob@example.com', password='pwd')

		resp = self.client.post('/register/', data={
			'fname': 'Bob',
			'lname': '',
			'email': 'bob2@example.com',
			'uname': 'bob',
			'pass1': 'pwd1',
			'pass2': 'pwd1',
		})

		# duplicate username should redirect back to register
		self.assertRedirects(resp, '/register/')
		self.assertEqual(User.objects.filter(username='bob').count(), 1)

	def test_register_allows_empty_last_name(self):
		resp = self.client.post('/register/', data={
			'fname': 'Dana',
			'lname': '',
			'email': 'dana@example.com',
			'uname': 'dana_user',
			'pass1': 'mypwd',
			'pass2': 'mypwd',
		})

		self.assertRedirects(resp, '/login/')

		User = get_user_model()
		self.assertTrue(User.objects.filter(username='dana_user').exists())

	def test_login_success(self):
		User = get_user_model()
		User.objects.create_user(username='charlie', password='pwd123')

		resp = self.client.post('/login/', data={'uname': 'charlie', 'pass1': 'pwd123'})
		self.assertRedirects(resp, '/')

		# subsequent requests should show an authenticated user
		resp2 = self.client.get('/')
		self.assertTrue(resp2.context['user'].is_authenticated)

	def test_login_wrong_creds(self):
		resp = self.client.post('/login/', data={'uname': 'noone', 'pass1': 'wrong'})
		self.assertRedirects(resp, '/login/')
