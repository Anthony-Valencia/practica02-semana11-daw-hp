from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from .models import Producto
class CatalogoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Producto.objects.create(nombre='Laptop de prueba',precio=Decimal('1999.90'),categoria='Laptops',stock=4,destacado=True)
        Producto.objects.create(nombre='Audio sin stock',precio=Decimal('100.00'),categoria='Audio',stock=0)
    def test_inicio(self):
        r=self.client.get(reverse('home'));self.assertEqual(r.status_code,200);self.assertContains(r,'Laptop De Prueba')
    def test_catalogo(self):
        r=self.client.get(reverse('catalogo'));self.assertEqual(r.status_code,200);self.assertContains(r,'Audio Sin Stock')
    def test_filtrado_categoria(self):
        r=self.client.get(reverse('catalogo'),{'categoria':'Laptops'});self.assertContains(r,'Laptop De Prueba');self.assertNotContains(r,'Audio Sin Stock')
    def test_filtrado_stock(self):
        r=self.client.get(reverse('catalogo'),{'disponibilidad':'stock'});self.assertContains(r,'Laptop De Prueba');self.assertNotContains(r,'Audio Sin Stock')
    def test_busqueda(self):
        r=self.client.get(reverse('catalogo'),{'q':'Laptop'});self.assertContains(r,'Laptop De Prueba');self.assertNotContains(r,'Audio Sin Stock')
