from django.test import TestCase
from chatbot.llm import query_llm_local
from chatbot.services.service import recommend_trips
from trips.models import Trip

class LLMTest(TestCase):
    def test_llm_output(self):
        prompt = "我想找三天的東京行程"
        result = query_llm_local(prompt)
        self.assertIn("東京", result)
        self.assertIn("天數", result)

class RecommendTripsTest(TestCase):
    def setUp(self):
        Trip.objects.create(
            name="東京三日遊",
            description="東京經典行程",
            price=10000,
            image="tokyo.jpg",
            start_date="2025-07-01",
            end_date="2025-07-03",
            available_seats=10,
            location="東京",
            style="城市",
            duration=3
        )

    def test_recommend_trips(self):
        llm_output = '{"天數": 3, "地點": "東京", "風格": "城市"}'
        trips = recommend_trips(llm_output)
        self.assertEqual(len(trips), 1)
        self.assertEqual(trips[0].name, "東京三日遊")