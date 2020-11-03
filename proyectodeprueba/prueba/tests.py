from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class PizzaDetalleViewTest(TestCase):
    fixtures = ['datitos.json']

    def test_detalle_pizza_argumento_inexistente(self):
        response = self.client.get(
            reverse("prueba:detalle_pizzero", args=("r")))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza inexistente")
        self.assertEqual(response.context["object"], None)

    def test_detalle_pizza_inexistente(self):
        pass
