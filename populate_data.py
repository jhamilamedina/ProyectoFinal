import os
import django
from random import sample

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from API_ENVIA_YA.models import Empresas, AgenciasLima, Departamentos, Provincias, Distritos, Valoraciones, Estrellas

# Nombres de Departamentos
nombres_departamentos = [
    'Arequipa',
    'Cusco',
    'Junin',
    'San Martin'
]

# Nombres de Provincias por cada Departamento
nombres_provincias = {
    'Arequipa': [
        'Camaná',
        'Caravelí',
        'Castilla',
        'Caylloma'
    ],
    'Cusco': [
        'Cusco',
        'Acomayo',
        'Espinar',
        'Anta'
    ],
    'Junin': [
        'Jauja',
        'Yauli',
        'Huancayo',
        'Chanchamayo'
    ],
    'San Martin': [
        'Moyobamba',
        'Tocache',
        'Bellavista',
        'San Martin'
    ]
}

# Nombres de Distritos por cada Provincia
nombres_distritos = {
    'Camaná': [
        'Camaná', 'José María Quimper', 'Mariano Nicolás Valcarcel', 'Mariscal Cáceres'
    ],
    'Caravelí': [
        'Caravelí', 'Acarí', 'Atico', 'Atiquipa'
    ],
    'Castilla': [
        'Aplao', 'Andahua', 'Ayo', 'Chachas'
    ],
    'Caylloma': [
        'Caylloma', 'Achoma', 'Cabanaconde', 'Callalli'
    ],
    'Cusco': [
        'Cusco', 'Ccorca', 'Poroy', 'San Jerónimo'
    ],
    'Acomayo': [
        'Acomayo', 'Acopía', 'Acos', 'Mosoc Llacta'
    ],
    'Espinar': [
        'Yauri', 'Condoroma', 'Coporaque', 'Ocoruro'
    ],
    'Anta': [
        'Anta', 'Ancahuasi', 'Cachimayo', 'Chinchaypujio'
    ],
    'Jauja': [
        'Jauja', 'Acolla', 'Apata', 'Ataura'
    ],
    'Yauli': [
        'La Oroya', 'Chacapalpa', 'Huayhuay', 'Marcapomacocha'
    ],
    'Huancayo': [
        'Huancayo', 'El Tambo', 'Chilca', 'Colca'
    ],
    'Chanchamayo': [
        'Chanchamayo (La Merced)', 'Vitoc', 'San Salvador', 'Pichanaki'
    ],
    'Moyobamba': [
        'Calzada', 'Habana', 'Jepelacio', 'Soritor'
    ],
    'Tocache': [
        'Nuevo Progreso', 'Polvora', 'Shunte', 'Uchiza'
    ],
    'Bellavista': [
        'Alto Biavo', 'Bajo Biavo', 'Huallaga', 'San Pablo'
    ],
    'San Martin': [
        'Tarapoto', 'Alberto Leveau', 'Cacatachi', 'Chazuta'
    ]
}

# Crear Departamentos, Provincias y Distritos
for nombre_dept in nombres_departamentos:
    # Crear Departamento
    departamento = Departamentos.objects.create(nombre=nombre_dept)
    
    provincias = nombres_provincias[nombre_dept]
    for nombre_prov in provincias:
        # Crear Provincia
        provincia = Provincias.objects.create(
            nombre=nombre_prov,
            departamento=departamento  # Usar el nombre correcto del campo
        )
        
        distritos = nombres_distritos[nombre_prov]
        for nombre_dist in distritos:
            # Crear Distrito
            Distritos.objects.create(
                provincia=provincia, 
                nombre=nombre_dist
            )

# Datos de prueba para empresas
datos_empresas = [
    {'logo': 'images/olva courier.png', 'nombre': 'Olva Courier', 'sede_principal': 'Avenida Argentina 4458, Callao, Perú', 'descripcion': 'Como especialistas en última milla, brindan servicios de calidad en transporte de encomiendas  a domicilio o a cualquiera de sus tiendas o agentes a nivel nacional', 'sitio_web': 'https://www.olvacourier.com'},

    {'logo': 'images/shalom.png', 'nombre': 'Shalom', 'sede_principal': 'Avenida México 1187,Cercado de Lima, Perú', 'descripcion': 'Shalom tiene una amplia red de distribución de puntos de entrega y acopio en los 24 departamentos del Perú', 'sitio_web': 'https://shalom.com.pe'},

    {'logo': 'images/dhl.png','nombre': 'DHL', 'sede_principal': 'Av. Inca Garcilaso de la Vega 1337, Cercado de Lima, Lima', 'descripcion': 'DHL es una empresa líder en logística a nivel mundial, especializada en envíos internacionales, servicios de mensajería y transporte', 'sitio_web': 'https://www.dhl.com/pe-es/home.html'},

    {'logo': 'images/servientrega.png', 'nombre': 'Servientrega', 'sede_principal': 'Av. Argentina 1790, Cercado de Lima, Lima', 'descripcion': 'Servientrega es una compañía orientada a ofrecer soluciones integrales de logística en recolección, transporte, almacenamiento, empaque y embalaje, logística promocional y distribución de documentos y mercancías', 'sitio_web': 'https://servientrega.com.pe/'},

    {'logo': 'images/fedex.png', 'nombre': 'FedEx', 'sede_principal': 'Pasaje Martir Olaya 260', 'descripcion': 'FedEx es una empresa de servicios de mensajería y logística que opera en Perú y a nivel mundial', 'sitio_web': 'https://www.fedex.com/es-pe/home.html'},

    {'logo': 'images/ups.png', 'nombre': 'Ups', 'sede_principal': 'Jr. Flora Tristan 310, Magdalena, Lima', 'descripcion': 'UPS ofrece opciones para envíos de bajo y gran volumen.', 'sitio_web': 'www.ups.com'},

    {'logo': 'images/urbano.png', 'nombre': 'Urbano', 'sede_principal': 'Avenida Materiales 3049, Cercado de Lima, Lima', 'descripcion': 'Urbano es una empresa de servicios logísticos en Perú. Su enfoque está en planificación urbana y desarrollo.', 'sitio_web': 'https://www.urbano.com.pe'},

    {'logo': 'images/transmar.png', 'nombre': 'Transmar', 'sede_principal': 'Avenida Nicolás Arriola 197, La Victoria', 'descripcion': 'Transmar es un grupo empresarial con 39 años de experiencia en el servicio de transporte de pasajeros, transporte de personal, encomiendas y transferencia de dinero.', 'sitio_web': 'https://transmar.pe'},
]

datos_agencias = [
    #Olva Courier
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier Cercado De Lima', 'foto':'agencias_imagenes/olva_cercado_de_lima.png', 'direccion': 'Avenida Garcilazo de la Vega 1358 Cercado de Lima', 'link_mapa': 'https://maps.app.goo.gl/eAYMu6dSNMoKkpXt9', 'horario de atencion': '9:30am a 7:00pm - lunes a sábados', 'telefono': '7140909', 'cochera': False},
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier Rimac', 'foto':'agencias_imagenes/olva_rimac.png', 'direccion': 'Las Tapadas 198, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/pXgZaY3gkkLkhk6J6', 'horario de atencion': '9:30am a 7:30pm - lunes a sábado', 'telefono': '912156055', 'cochera': False},
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier La Victoria', 'foto': 'agencias_imagenes/olva_la_victoria.png', 'direccion': 'Jirón Antonio Bazo 1280, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/B4W32YXbNF2YywDK7', 'horario de atencion': '8:00am a 6:30pm - lunes a sábado', 'telefono': '7140908', 'cochera': True},
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier Miraflores', 'foto': 'agencias_imagenes/olva_miraflores.png', 'direccion': 'Avenida Comande Espinar 659, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/iDSyvBgCV1N7oLk79', 'horario de atencion': '8:00am a 7:00pm - lunes a sábado', 'telefono': '987655900', 'cochera': True},
    #Shalom
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom Rimac', 'foto': 'agencias_imagenes/shalom_rimac.png', 'direccion': 'Avenida Amancaes 644, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/WNJ1AdEQthXUCZyUA', 'horario de atencion': '8:30am a 7:00pm - lunes a sábado', 'telefono': '5007878', 'cochera': False},
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom La Victoria', 'foto': 'agencias_imagenes/shalom_la_victoria.png', 'direccion': 'Jirón Luna Pizarro, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/zmvvkb781rx2hv3f6', 'horario de atencion': '7:00am a 5:30pm - lunes a sábado', 'telefono': '7158800', 'cochera': True},
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom Breña', 'foto': 'agencias_imagenes/shalom_breña.png', 'direccion': 'Avenida República de Venezuela 1670, Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/SZvunBWwX2fXvBR98', 'horario de atencion': '9:00am a 7:00pm - lunes a sábado', 'telefono': '5452222', 'cochera': True},
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom Miraflores', 'foto': 'agencias_imagenes/shalom_miraflores.png', 'direccion': 'Avenida José Pardo 533, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/bNwtMwLNMFqFsiB99', 'horario de atencion': '8:00am a 6:30pm - lunes a sábado', 'telefono': '5007878', 'cochera': True},
    #DHL
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL La Victoria', 'foto': 'agencias_imagenes/dhl_la_victoria.png', 'direccion': 'Jirón Antonio Bazo 613,La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/DaEjazvTG6zdJQZp6', 'horario de atencion': '9:00am a 6:30pm - lunes a sábado', 'telefono': '94181895', 'cochera': False},
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL Breña', 'foto': 'agencias_imagenes/dhl_breña.png', 'direccion': 'Jirón Huaraz 1592,Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/GpLJ8sEVT24AK5FN9', 'horario de atencion': '8:30am a 6:30pm - lunes a sábado', 'telefono': '5172500', 'cochera': False},
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL Miraflores', 'foto': 'agencias_imagenes/dhl_miraflores.png', 'direccion': 'Avenida Alfredo Benavides 708, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/T9xT3sKxrnt2iG8w6', 'horario de atencion': '9:00am a 7:00pm - lunes a sábado', 'telefono': '932108772', 'cochera': False},
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL San Luis', 'foto': 'agencias_imagenes/dhl_san_luis.png', 'direccion': 'Avenida San Luis 2211, San Luis', 'link_mapa': 'https://maps.app.goo.gl/jF5Bgh4o3Z93t3UA9', 'horario de atencion': '9:00am a 6:30pm - lunes a sábado', 'telefono': '951369412', 'cochera': True},

    #Servientrega
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega Breña', 'foto': 'agencias_imagenes/servientrega_breña.png', 'direccion': 'Avenida Argentina 515,Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/8JHR76dn7tK4GJrY8', 'horario de atencion': '8:30am a 6:30pm ', 'telefono': '5653232', 'cochera': False},
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega Miraflores', 'foto': 'agencias_imagenes/servientrega_miraflores.png', 'direccion': 'Avenida Javier Prado, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/Tezb1w5zbqWdb3Uc8', 'horario de atencion': '8:30am a 6:30pm - lunes a sábado', 'telefono': '914668870', 'cochera': True},
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega San Luis', 'foto': 'agencias_imagenes/servientrega_san_luis.png', 'direccion': 'Avenida Agustín de la Rosa Toro 490, San Luis, Lima', 'link_mapa': 'https://maps.app.goo.gl/pc3bEapAXK6sysXG8', 'horario de atencion': '9:00am a 7:00pm - lunes a sábado', 'telefono': '914668870', 'cochera': True},
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega Cercado De Lima', 'foto': 'agencias_imagenes/servientrega_cercado_de_lima.png', 'direccion': 'Jirón de la Torre Ugarte 155, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/VTFRLcrtmkw2wJiQ6', 'horario de atencion': '8:30am a 7:00pm  - Lunes a sábado', 'telefono': '914668870', 'cochera': True},
    #Fedex
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx Miraflores', 'foto': 'agencias_imagenes/fedex_miraflores.png', 'direccion': 'Calle Alcanfores 350, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/TZbBQpChaRrrxscg9', 'horario de atencion': '8:30am a 7:30pm ', 'telefono': '6806120', 'cochera': True},
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx San Luis', 'foto': 'agencias_imagenes/fedex_san_luis.png', 'direccion': 'Avenida Ricardo Basilio 1382,San Luis, Lima', 'link_mapa': 'https://maps.app.goo.gl/TZbBQpChaRrrxscg9', 'horario de atencion': '9:00am a 6:00pm - Lunes a sábado', 'telefono': '6806120', 'cochera': True},
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx Cercado de lima', 'foto': 'agencias_imagenes/fedex_cercado_de_lima.png', 'direccion': 'Calle Los Cedros 350, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/Yj6gKCFntspQZ3dv7', 'horario de atencion': '8:30am a 6:30pm - lunes a sábado', 'telefono': '6806120', 'cochera': True},
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx Rimac', 'foto': 'agencias_imagenes/fedex_rimac.png', 'direccion': 'Calle Lomas de Almancaes 548, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/TZbBQpChaRrrxscg9', 'horario de atencion': '7:00am a 6:00pm - lunes a sábado', 'telefono': '6806120', 'cochera': True},
    #Ups
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups San Luis', 'foto': 'agencias_imagenes/ups_san_luis.png', 'direccion': 'Avenida Javier Prado Este 1500, San Luis, Lima', 'link_mapa': 'https://maps.app.goo.gl/WwbjGLPGoMdkRoG69', 'horario de atencion': '7:30am a 6:30pm - Lunes a sábado', 'telefono': '7155184', 'cochera': True},
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups Cercado De Lima', 'foto': 'agencias_imagenes/ups_cercado_de_lima.png', 'direccion': 'Jirón Huallaga 288, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/Zcgx18tg58RQLsxG6', 'horario de atencion': '10:00am a 7:30pm - Lunes a sábado', 'telefono': '969671160', 'cochera': True},
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups Rimac', 'foto': 'static/agencias_imagenes/ups_rimac.png', 'direccion': 'Jirón Santa Cecilia 1502, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/WLXwqUkJZ2Ucx4to6', 'horario de atencion': '9:30am a 5:30pm - lunes a sábado', 'telefono': '3184195', 'cochera': True},
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups La Victoria', 'foto': 'agencias_imagenes/ups_la_victoria.png', 'direccion': 'Avenida Elmer Faucett 158, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/4nyhtkNp3UiFhHr96', 'horario de atencion': '7:00am a 5:00pm - lunes a sábado', 'telefono': '6142500', 'cochera': True},
    #Urbano
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano Cercado De Lima', 'foto': 'agencias_imagenes/urbano_cercado_de_lima.png', 'direccion': 'Avenida Materiales 3049, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/99dJcASG76Fx9wn49', 'horario de atencion': '9:00am a 6:30pm - Lunes a sábado', 'telefono': '6323270', 'cochera': True},
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano Rimac', 'foto': 'agencias_imagenes/urbano_rimac.png', 'direccion': 'Calle San German 205, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/qHPZ7sFhS5ktERAX6', 'horario de atencion': '9:00am a 6:30pm - Lunes a sábado', 'telefono': '6323270', 'cochera': True},
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano La Victoria', 'foto': 'agencias_imagenes/urbano_la_victoria.png', 'direccion': 'Jirón Lucanas 671,La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/FyzLkxmKkjoapmed7', 'horario de atencion': '9:00am a 6:30pm', 'telefono': '6323270', 'cochera': False},
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano Breña', 'foto': 'agencias_imagenes/urbano_breña.png', 'direccion': 'Avenida Arica 150 Breña', 'link_mapa': 'https://maps.app.goo.gl/uGg8zh4GffZtU6sP7', 'horario de atencion': '9:00am a 7:00pm', 'telefono': '6323270', 'cochera': None},
    #Transmar
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar Rimac', 'foto': 'agencias_imagenes/transmar_rimac.png', 'direccion': 'Avenida 28 de Julio 1511, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/jmysdCK7CNKFsuwi9', 'horario de atencion': '7:00am a 6:30pm - Lunes a sábado', 'telefono': '2650190', 'cochera': True},
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar La Victoria', 'foto': 'agencias_imagenes/transmar_la_victoria.png', 'direccion': 'Avenida Bauzate y Meza 680, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/w9t6nHMPj3PJiSQZA', 'horario de atencion': '8:00am a 6:00pm - Lunes a sábado', 'telefono': '995737290', 'cochera': True},
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar Breña ', 'foto': 'agencias_imagenes/transmar_breña.png', 'direccion': 'Jirón Pucallpa 266, Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/ZTCP5mU2tFp6EBLKA', 'horario de atencion': '8:00am a 7:30pm - Lunes a sábado', 'telefono': '995737290', 'cochera': False},
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar Miraflores', 'foto': 'agencias_imagenes/transmar_miraflores.png', 'direccion': 'Avenida Nicolás Arriola 197, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/TJCCNZNK1VGiSGHs8', 'horario de atencion': '8:00am a 6:00pm - Lunes a sábado', 'telefono': '995737290', 'cochera': True},
]
# Crear Empresas, Agencias y Valoraciones
for datos_empresa in datos_empresas:
    # Crear Empresa
    empresa = Empresas.objects.create(
        logo=datos_empresa['logo'],
        nombre=datos_empresa['nombre'],
        sede_principal=datos_empresa['sede_principal'],
        descripcion=datos_empresa['descripcion'],
        sitio_web=datos_empresa['sitio_web']
    )
    
    # Crear Agencias
    for datos_agencia in datos_agencias:
        if datos_agencia['empresa_nombre'] == empresa.nombre:
            # Seleccionar 2-4 distritos aleatorios para la agencia
            distritos = Distritos.objects.order_by('?')[:sample(range(15, 20), 1)[0]]
        
            agencia = AgenciasLima.objects.create(
                empresa=empresa,
                nombre_referencial=datos_agencia['nombre_referencial'],
                foto=datos_agencia['foto'],
                direccion=datos_agencia['direccion'],
                link_mapa=datos_agencia['link_mapa'],
                horario_de_atencion=datos_agencia['horario de atencion'],
                telefono=datos_agencia['telefono'],
                cochera=datos_agencia['cochera']
            )   
            agencia.distritos.set(distritos)  # Asignar distritos a la agencia
    
    # Crear una Valoración para la Empresa
    Valoraciones.objects.create(
        empresa=empresa,
        puntualidad=0,
        seguridad=0,
        economica=0,
        amabilidad=0,
        caro=0,
        inseguro=0,
        impuntual=0,
        poco_amables=0
    )
    
    # Crear Estrellas para la Empresa
    Estrellas.objects.create(
        empresa=empresa,
        estrella_1=0,
        estrella_2=0,
        estrella_3=0,
        estrella_4=0,
        estrella_5=0
    )

print("Datos de prueba creados exitosamente.")
