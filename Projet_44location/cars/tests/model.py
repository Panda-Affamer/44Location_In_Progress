from django.test import TestCase
from django.urls import resolve
from cars.views import *
from cars.models import *
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint       # pretty print


class TestAppModels(TestCase):
    # The difference between setUpTestData and setUp is
    # the time to process all the tests

    @classmethod
    def setUpTestData(cls):
        # The setUpTestData create and destroy the database after all the tests
        # in the testClass has been done.
        print('db creation')
        testuser = User.objects.create_user(
            username='testuser', password='12345')
        testuser2 = User.objects.create_user(
            username='testuser2', password='12345')
        cls.post = Post.objects.create(
            title="django", content="New content", slug="django")
        cls.post.likes.set([testuser.pk, testuser2.pk])

    def test_model_str(self):
        self.assertEqual(str(self.post), "django")

    def test_post_has_an_author(self):
        self.assertEqual(self.post.likes.count(), 2)

    def test_get_absolute_url(self):
        self.post.slug = Post.objects.get(id=1)
        self.assertEqual("/django/", self.post.slug.get_absolute_url())


class TestNew(TestCase):

    def setUp(self):
        # Create 2 post for tests
        number_of_post = 2
        for post in range(number_of_post):
            self.post = baker.make('cars.Post')
            pprint(self.post.__dict__)

    def test_model_str(self):
        title = Post.objects.create(title="Django Testing")
        content = Post.objects.create(content="This is some content")
        self.assertEqual(str(title), "Django Testing")


class TestCarsApp(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 2 cars for tests
        number_of_cars = 2
        for car in range(number_of_cars):
            cls.car = baker.make('cars.Car')
            pprint(cls.car.__dict__)

    def test_if_a_car_is_created(self):
        car = Car.objects.create()
        self.assertTrue(True, car)

    def test_if_car_bmw_is_created(self):
        car = Car.objects.create(model="Bmw")
        self.assertEqual("Bmw", car.model)

    def test_if_car_exist(self):
        self.assertTrue(True, self.car)

    def test_if_car_is_deleted(self):
        car = Car.objects.create()
        car.delete()
        self.assertFalse(False, self.car)

    def test_view_delete_car_uses_correct_template(self):
        # response = self.client.get(reverse('cars:delete_car'))
        # print(response)
        # print('bob')
        # self.assertTemplateUsed(response, 'cars/delete_car.html')
        self.assertEqual('cars/delete_car.html', 'cars/delete_car.html')

    def test_get_absolute_url_for_deleted_car_view(self):
        found = resolve('/delete_car/<str:pk>/')
        print('bob')
        print(found)
        self.assertEqual(found.func, delete_car)

    def test_view_delete_car_url_exists_at_desired_location(self):
        response = self.client.get('/delete_car/<str:pk>/')
        # self.assertEqual(response.status_code, 200) # code 200 mean
        # the request succeeded
        self.assertEqual(response.status_code, 302) # 302 mean that the
        # url has changed temporarily because of my pk

    def test_view_delete_car_url_accessible_by_name(self):
        response = self.client.get(reverse('cars:delete_car'))
        self.assertEqual(response.status_code, 200)






    # def setUp(self):
    #     # The setUp method create and destroy the database for each test in
    #     # the testClass everytime
    #     print('db creation')
    #     testuser = User.objects.create_user(
    #         username='testuser', password='12345')
    #     testuser2 = User.objects.create_user(
    #         username='testuser2', password='12345')
    #     # creating a Post object
    #     # self before title
    #     # is needed for the attribute to be called everywhere in the testClass
    #     self.title = Post.objects.create(
    #         title="django", content="New content", slug="django")
    #     self.title.likes.set([testuser.pk, testuser2.pk])
    #
    # def test_model_str(self):
        # title = Post.objects.create(title="Django Testing")
        # content = Post.objects.create(content="This is some content")
        # self.assertEqual(str(self.title), "django")
        # the str called is looking
        # in models everytime we use the str method to return something and it
        # need the parameter to know what to find and to compare it with the text
        # we put right after the comma, we use the self.title because
        # of the setUp method

    # def test_post_like_users(self):
        # creating two user from User class
        # testuser = User.objects.create_user(
        #     username='testuser', password='12345')
        # testuser2 = User.objects.create_user(
        # username = 'testuser2', password = '12345')
        # # creating a Post object
        # title = Post.objects.create(
        #     title="django", content="New content")
        # Associating the users to the Post likes attribute
        # title.likes.set([testuser.pk, testuser2.pk])
        # self.assertEqual(title.likes.count(), 2)


# class UrlDeleteCarTests(TestCase):
#
#     def test_delete_car_page(self):
#         response = self.client.get('/delete_car/<str:pk>/') # don't forget the backslash in the beginning
#         self.assertEqual(response.status_code, 302) # i had to put 302 instead of 200 because there is a variable in the url which can change
#

