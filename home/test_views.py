from django.test import TestCase

class TestViews(TestCase):
    
    def test_if_index_page_diplays_correctly(self):
        page = self.client.get("home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
