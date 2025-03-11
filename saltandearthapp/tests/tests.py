from rest_framework.test import APITestCase
from rest_framework import status
from saltandearthapp.models import City, Lodging, Restaurant, Tag, User

class CityTests(APITestCase):
    def setUp(self):
        self.city = City.objects.create(name="Nashville", image="http://example.com/image.jpg")

    def test_get_cities(self):
        response = self.client.get("/cities")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_city_by_id(self):
        response = self.client.get(f"/cities/{self.city.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Nashville")

    def test_create_city(self):
        data = {"name": "Memphis", "image": "http://example.com/memphis.jpg"}
        response = self.client.post("/cities", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_city(self):
        data = {"name": "Updated Nashville", "image": "http://example.com/new.jpg"}
        response = self.client.put(f"/cities/{self.city.id}", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_city(self):
        response = self.client.delete(f"/cities/{self.city.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class LodgingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Test", last_name="User", uid="test-uid")
        self.city = City.objects.create(name="Nashville", image="http://example.com/image.jpg")
        self.lodging = Lodging.objects.create(
            user_id=self.user,
            uid="123",
            city_id=self.city,
            name="Hotel Example",
            address="123 Main St",
            description="A great place to stay",
            image="http://example.com/hotel.jpg",
            link="http://example.com"
        )

    def test_get_lodging(self):
        response = self.client.get("/lodging")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lodging_by_id(self):
        response = self.client.get(f"/lodging/{self.lodging.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Hotel Example")

    def test_create_lodging(self):
        data = {
            "user_id": self.user.id,
            "uid": "456",
            "city_id": self.city.id,
            "name": "New Hotel",
            "address": "456 Street",
            "description": "Another great stay",
            "image": "http://example.com/newhotel.jpg",
            "link": "http://example.com"
        }
        response = self.client.post("/lodging", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_lodging(self):
        response = self.client.delete(f"/lodging/{self.lodging.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RestaurantTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Test", last_name="User", uid="test-uid")
        self.city = City.objects.create(name="Nashville", image="http://example.com/image.jpg")
        self.restaurant = Restaurant.objects.create(
            user_id=self.user,
            uid="123",
            city_id=self.city,
            name="Deli Example",
            address="321 Market St",
            description="Great sandwiches",
            image="http://example.com/deli.jpg",
            link="http://example.com"
        )

    def test_get_restaurants(self):
        response = self.client.get("/restaurants")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_restaurant(self):
        data = {
            "user_id": self.user.id,
            "uid": "789",
            "city_id": self.city.id,
            "name": "New Deli",
            "address": "555 Main St",
            "description": "Amazing food",
            "image": "http://example.com/deli2.jpg",
            "link": "http://example.com"
        }
        response = self.client.post("/restaurants", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_restaurant(self):
        data = {
            "user_id": self.user.id,  # Added user_id
            "city_id": self.city.id,  # Added city_id
            "uid": "123",
            "name": "Updated Deli",
            "address": "321 Market St",
            "description": "Better sandwiches",
            "image": "http://example.com/deli_updated.jpg",
            "link": "http://example.com"
        }
        response = self.client.put(f"/restaurants/{self.restaurant.id}", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TagTests(APITestCase):
    def test_update_tag(self):
        data = {"name": "Sustainable"}
        response = self.client.put(f"/tags/{self.tag.id}", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def setUp(self):
        self.tag = Tag.objects.create(name="Eco-Friendly")

    def test_get_tags(self):
        response = self.client.get("/tags")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tag(self):
        data = {"name": "Vegan"}
        response = self.client.post("/tags", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_tag(self):
        response = self.client.delete(f"/tags/{self.tag.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
