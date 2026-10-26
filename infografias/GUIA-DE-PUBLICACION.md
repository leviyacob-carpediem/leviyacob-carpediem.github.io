# Biblioteca Digital de Infografías · Guía de publicación

Historia con Levi | Carpe Diem · Proyecto docente independiente.

## Añadir un material sin editar el diseño
1. Conserva el archivo original de alta resolución fuera del sitio. Comprueba autoría, fuentes históricas y permiso para publicar/descargar; evita datos personales del alumnado.
2. Guarda la imagen de lectura y su miniatura en la carpeta de la colección. Usa WebP para fotografías e ilustraciones; si el texto pierde nitidez, PNG. Admite JPG, JPEG y AVIF. Miniatura vertical recomendada: 480 px de ancho; lectura: 1600–2400 px o el ancho necesario para leer todos los textos al ampliar. No amplíes artificialmente una imagen pequeña. Revisa en celular. Usa nombres sin espacios ni acentos.
3. Agrega un objeto al arreglo `infografias` de `catalogo.json` con los campos indicados abajo. No existe límite fijo por colección. El visor carga la imagen grande al abrirla y la cuadrícula muestra 24 materiales por página.
4. Ejecuta `python infografias/validar_catalogo.py` desde la raíz del repositorio. Debe terminar sin errores antes de publicar.
5. Confirma los cambios en `main`, espera GitHub Pages y comprueba miniatura, lectura, créditos y descarga pública.

## Campos de cada infografía
- `id`: identificador único, sin espacios (ej.: mesopotamia-escritura).
- `coleccion`: uno de los 12 identificadores de `colecciones`.
- `titulo`, `descripcion`, `alt`: textos reales, en español; el alt describe el contenido visual.
- `imagen`: ruta desde la raíz del museo, por ejemplo `infografias/mesopotamia/escritura.webp`. No anteponer `/`.
- `miniatura`: ruta local de la miniatura optimizada. Puede omitirse; se usará la imagen principal.
- `tipo`: `Infografía educativa`, `Fotografía`, `Ilustración` o `Recreación artística con IA · Interpretación hipotética`, según corresponda.
- `etiquetas`: arreglo de palabras clave para búsqueda.
- `fecha`: fecha ISO `AAAA-MM-DD`.
- `creditos`: objeto con `autor`, `licencia`, `fuente` (nombre de la fuente), `url` (URL HTTPS opcional) y `nota` opcional. Indica expresamente uso de IA si corresponde. Para publicaciones propias puede indicarse la autorización real del autor; no inventes licencias.
- `descarga`: `null` cuando no hay descarga autorizada; en otro caso un objeto con `ruta` local de una imagen/PDF autorizado y `nombre` de archivo sugerido. Solo muestra el botón si existe este campo y la imagen de lectura carga.
- `publicado`: `true` para mostrar; `false` para borradores. Los borradores almacenados en un repositorio público no son privados.

No agregues archivos o entradas ficticias como publicaciones. La biblioteca comienza sin infografías: las 12 colecciones son espacios preparados. Las fotografías de las exposiciones no se copian ni se convierten automáticamente en infografías.

## Privacidad y analítica
La biblioteca usa una sola etiqueta GA4 `G-C5387P9TWG`. La búsqueda se realiza en el navegador; no se envían consultas mediante eventos personalizados. No se añaden formularios ni sistemas de registro.
