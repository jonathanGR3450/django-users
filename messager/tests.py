from django.test import TestCase
from django.contrib.auth.models import User
from messager.models import Thread, Message

# Create your tests here.
class MessagesTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'lol123lol')
        self.user2 = User.objects.create_user('user2', None, 'lol123lol')
        self.user3 = User.objects.create_user('user3', None, 'lol123lol')
        self.thread = Thread.objects.create()

    def test_add_user_to_thread(self):
        self.thread.user.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.user.all()), 2)

    def test_filter_thread_by_user(self):
        self.thread.user.add(self.user1, self.user2)
        thread = Thread.objects.filter(user=self.user1).filter(user=self.user2)
        self.assertEqual(self.thread, thread[0])
    
    def test_is_not_exist_thread(self):
        thread = Thread.objects.filter(user=self.user1).filter(user=self.user2)
        self.assertEqual(len(thread), 0)
    
    def test_add_message_to_thread(self):
        msg1 = Message.objects.create(user=self.user1, content='Hola')
        msg2 = Message.objects.create(user=self.user2, content='Hola, como estas?')
        self.thread.messages.add(msg1, msg2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        # vamos a recorrer el hilo para mostrar los mensajes
        for message in self.thread.messages.all():
            print('Usuario <{}>: {}'.format(message.user, message.content))
    
    # test para probar el manager custom del modelo
    def test_find_by_users(self):
        self.thread.user.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    def test_find_by_users_none(self):
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertIsNone(thread)

    def test_find_or_create_thread(self):
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertIsNotNone(thread)
    
    def test_find_or_create_thread_create(self):
        self.thread.user.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    def test_mesage_user_not_in_thread(self):
        self.thread.user.add(self.user1, self.user2)
        msg1 = Message.objects.create(user=self.user1, content='Hola')
        msg2 = Message.objects.create(user=self.user2, content='Hola, como estas?')
        msg3 = Message.objects.create(user=self.user3, content='espia')
        self.thread.messages.add(msg1, msg2, msg3)
        self.assertEqual(len(self.thread.messages.all()), 2)

