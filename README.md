# NEOTECH — Catálogo de Productos Tecnológicos

**Universidad Nacional del Centro del Perú · Ingeniería de Sistemas · Desarrollo de Aplicaciones Web · Semana 11 (2026)**

Proyecto académico Django con diseño responsive estilo _tech editorial_, modo oscuro, animaciones CSS y fotografías de productos cargadas desde Unsplash. **No es una tienda de comercio electrónico**: los precios, marcas ficticias, stocks y descripciones son demostrativos.

INTEGRANTES:

- Hinojosa Yaranga Renzo Sebastian
- Valencia Bernaola Andres Anthony

## Instalación en Windows / VS Code (PowerShell)

```powershell
cd NEOTECH_Catalogo_Django
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py cargar_productos
python manage.py check
python manage.py runserver
```

**Enlaces:** `http://127.0.0.1:8000/` y `http://127.0.0.1:8000/catalogo/`.

**Panel de administración:** ejecutar `python manage.py createsuperuser` y entra en `http://127.0.0.1:8000/admin/`.

## Rutas

- `/`: vista basada en función `home(request)` con `render` y QuerySet de destacados.
- `/catalogo/`: CBV `ProductoListView(ListView)` con filtrado, búsqueda, ordenamiento y paginación.
- `/admin/`: mantenimiento de datos a través del administrador Django.

## Modelo

`Producto` contiene nombre, precio (DecimalField), categoría, stock, descripción, URL de imagen, etiqueta, destacado y fecha de creación. Las imágenes se sirven desde URLs públicas de Unsplash; se incluye fallback SVG local. Las fotografías requieren internet. La interfaz también usa Google Fonts y Font Awesome desde CDN; con internet luce completa, y sin internet se usan tipografías del sistema y los íconos externos pueden no aparecer.

## Validación

```powershell
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py check
python manage.py test
```
Prueba el inicio, catálogo, categoría, búsqueda y filtrado de disponibilidad. El catálogo utiliza `for`, `empty`, `if`, `url`, `title`, `truncatechars`, `floatformat` y plantillas extendidas de `base.html`.

## Capturas del entregable

En `docs/capturas/` se encuentra una guía con las capturas que deben realizarse después de ejecutar el proyecto. No se incluyen capturas ficticias.

=======

## Trabajo grupal

- Integrante 1: arquitectura Django, URLs, modelos, ORM y migraciones.
- Integrante 2: vistas, plantillas, interfaz responsive, pruebas y documentación.

## Estructura

```text
NEOTECH_Catalogo_Django/
├── config/ (settings.py, urls.py, wsgi.py, asgi.py)
├── catalogo/ (models.py, views.py, admin.py, urls.py, migrations/, management/, tests.py)
├── templates/ (base.html, home.html, catalogo.html, partials/)
├── static/ (css/, js/, images/)
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Créditos y uso

Las imágenes remotas de referencia provienen de [Unsplash](https://unsplash.com/) y deben usarse conforme a sus condiciones. Íconos de Font Awesome Free y fuentes de Google Fonts, accesibles desde sus CDN públicos. Proyecto destinado a demostración local; para producción hay que configurar `DEBUG=0`, una clave secreta propia, hosts y static files.


## Aporte colaborativo — fichas de detalle y favoritos

- Nueva ruta `catalogo/<int:pk>/` implementada con `DetailView`, donde se consulta el producto por clave primaria.
- Ficha completa con foto, descripción, precio, disponibilidad y productos relacionados mediante un QuerySet por categoría.
- Botones accesibles de favoritos en las tarjetas y fichas. Persisten en `localStorage` del navegador, sin cuentas ni base de datos adicional. El indicador del encabezado muestra el número de favoritos.
- Pruebas para detalle existente, error 404 y productos relacionados.
- Los precios son demostrativos y el sitio no procesa compras.

**Validación del aporte:** `python manage.py check` y `python manage.py test`.

**Nota de Git:** integrar esta contribución en una rama nueva mediante pull request; no reemplazar directamente `main`.
=======

