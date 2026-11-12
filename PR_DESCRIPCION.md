# feat: fichas de producto y favoritos locales

## Resumen
Agrega páginas de detalle para cada producto del catálogo NEOTECH y botones de favoritos persistidos en el navegador.

## Cambios
- `DetailView` en `/catalogo/<id>/` y sección de productos relacionados mediante ORM.
- Enlaces «Ver detalles» en tarjetas del inicio y catálogo.
- Favoritos accesibles con `aria-pressed`, almacenados en `localStorage`; contador del encabezado.
- Diseño responsive y transiciones respetando `prefers-reduced-motion`.
- Tres nuevas pruebas automatizadas y documentación actualizada.

## Cómo probar
```bash
python manage.py check
python manage.py test
python manage.py runserver
```
Visitar `/catalogo/`, abrir una ficha y pulsar el corazón; comprobar persistencia al recargar.

## Evidencias sugeridas
- Captura del listado con iconos de favoritos.
- Captura de `/catalogo/1/` (o el ID existente).
- Captura de la terminal con pruebas exitosas.
