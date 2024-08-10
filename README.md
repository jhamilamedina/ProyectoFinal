# ENVIA YA

## Introduccion
_Envia Ya_ es una pagina web que permite a los usuarios conocer la reputación de diferentes empresas de envío. Los usuarios pueden acceder a información detallada sobre las empresas, dejar comentarios, valoraciones y calificaciones con estrellas para ayudar a otros a tomar decisiones informadas.

La página muestra información relevante sobre las empresas de envío, como dirección, descripción y más. Los usuarios pueden:

- Consultar información detallada de las empresas de envío.
- Dejar comentarios y valoraciones sobre sus experiencias.
- Calificar a las empresas con estrellas.
- Ver la información de las agencias asociadas a las empresas (dirección, horario de atención, teléfono, etc.).
- Filtrar agencias por distrito de destino para facilitar la toma de decisiones.

_Nota: Envia Ya es una plataforma informativa. No permite realizar pagos ni reservas._

---
**LinkedIn del autor(es):** 

Eduar Vallejos Chumbe - https://www.linkedin.com/in/eduar-vallejos-chumbe/

Maly Jhamila Medina Maylle - https://www.linkedin.com/in/malyjmedina/

Misael Jair Bazán Franco - https://www.linkedin.com/in/misael-baz%C3%A1n-franco-95805b25a?originalSubdomain=pe 

Jorgelina Isabel Silva Mauricio - https://www.linkedin.com/in/jorgelina2292

---

### Tabla de Contenidos
- [Instalacion](#instalacion)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Proyectos Relacionados](#proyectos-relacionados)
- [Licencia](#licencia)

## Instalacion

Para instalar y ejecutar el proyecto localmente, sigue estos pasos:

Debe tener `Python` instalado: https://www.python.org

1. Clona el repositorio:

``` bash
git clone https://github.com/jhamilamedina/Proyecto_Envia_Ya

cd Proyecto_Envia_Ya

```

2. Crea un entorno virtual y actívalo:

``` bash
python3 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Instala las dependencias:

``` bash
pip install -r requirements.txt
```

4. Realiza las migraciones de la base de datos:

``` bash
python manage.py makemigrations
python manage.py migrate
```

5. Ejecuta el servidor:

``` bash
python manage.py runserver
```

## Uso

Una vez instalado, puedes acceder a la aplicación en `http://localhost:8000`. Algunas de las funcionalidades principales incluyen:

- Consultar la información de las empresas de envío
- Crear una cuenta
- Leer y publicar comentarios y valoraciones.
- Filtrar agencias por distrito de destino.

## Contribuciones

¡Contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu función (`git checkout -b feature/nueva-funcion`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva función'`).
4. Haz push a la rama (`git push origin feature/nueva-funcion`).
5. Abre un Pull Request.

## Proyectos Relacionados

- proyecto relacionado 1
- proyecto relacionado 2

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.