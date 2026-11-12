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

    def test_detalle_producto(self):
        producto = Producto.objects.get(nombre='Laptop de prueba')
        r = self.client.get(reverse('producto_detalle', kwargs={'pk': producto.pk}))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Laptop de prueba')
        self.assertTemplateUsed(r, 'producto_detalle.html')

    def test_detalle_inexistente(self):
        r = self.client.get(reverse('producto_detalle', kwargs={'pk': 999999}))
        self.assertEqual(r.status_code, 404)

    def test_relacionados_misma_categoria_sin_actual(self):
        primero = Producto.objects.get(nombre='Laptop de prueba')
        segundo = Producto.objects.create(nombre='Otra laptop', precio=Decimal('1499'), categoria='Laptops', stock=2)
        r = self.client.get(reverse('producto_detalle', kwargs={'pk': primero.pk}))
        self.assertIn(segundo, r.context['relacionados'])
        self.assertNotIn(primero, r.context['relacionados'])
