from django.test import TestCase

from django.urls import reverse

from minerals.models import Mineral


# Create your tests here.
class MineralViewsTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name = "Stevenite",
            category = "Techdegree Student",
            group = "Halides"
            )
        self.mineral2 = Mineral.objects.create(
            name = "Rockite",
            category = "rock",
            group = "Sulfides"
            )

    def test_mineral_list_view(self):
        '''List view'''
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_details_view(self):
        '''Detail view'''
        resp = self.client.get(reverse('minerals:details',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_search_by_letter_view(self):
        '''Search by letter view'''
        resp = self.client.get(reverse('minerals:by_letter',
                            kwargs={'letter': 's'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_search_view(self):
        '''Search view'''
        resp = self.client.get(reverse('minerals:search'), {'q': 'Stev'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_search_by_group_view(self):
        '''Search by mineral group name'''
        resp = self.client.get(reverse('minerals:group',
                                kwargs={'group': self.mineral.group}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')