import os
import django
from random import sample, randint

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
    {'logo': 'static/images/olva courier.png', 'nombre': 'Olva Courier', 'sede_principal': 'Avenida Argentina 4458, Callao, Perú', 'descripcion': """En OLVA, nos esforzamos por ofrecer un servicio de calidad que supere las expectativas de nuestros clientes. Trabajamos con actitudes positivas y vivimos nuestros valores en nuestro día a día.

    Es una empresa peruana de mensajería y logística, reconocida por ofrecer servicios de envío de documentos, paquetes y mercancías a nivel nacional. Fundada en 1987, Olva Courier ha crecido para convertirse en una de las principales empresas de su sector en Perú, con una amplia red de agencias que cubre todo el país.

    Servicios Ofrecidos
    Envíos Nacionales: Olva Courier ofrece servicios de envío de documentos y paquetes a cualquier destino dentro del Perú, con opciones de entrega en agencia o a domicilio.
    Envíos Internacionales: También proporciona servicios para envíos al extranjero, facilitando la logística de exportación e importación.
    Olva Box: Un servicio especializado en compras internacionales que permite a los usuarios adquirir productos de tiendas en el extranjero y recibirlos en Perú.
    Soluciones para Empresas: Ofrecen servicios personalizados para empresas, incluyendo la gestión de envíos masivos, distribución de productos y logística para comercio electrónico.
    Seguimiento de Envíos: Los clientes pueden rastrear sus envíos en tiempo real a través de la plataforma en línea de Olva Courier.
    Cobertura
    Olva Courier cuenta con una red de más de 300 agencias en todo el país, lo que le permite llegar a las principales ciudades y a zonas rurales de difícil acceso. Además, su infraestructura incluye centros de distribución y una flota de vehículos que aseguran la entrega rápida y segura de los envíos.""", 'sitio_web': 'https://www.olvacourier.com'},


    {'logo': 'static/images/shalom.png', 'nombre': 'Shalom', 'sede_principal': 'Avenida México 1187,Cercado de Lima, Perú', 'descripcion': """Shalom Transportes y Encomiendas es una empresa peruana especializada en el envío de paquetes y mercancías a nivel nacional.

    Shalom nació en Lima, Perú, con la misión de proporcionar un servicio de transporte seguro, eficiente y accesible. Con el tiempo, la empresa ha crecido exponencialmente, ampliando su cobertura a lo largo y ancho del país, así como estableciendo alianzas estratégicas que le permiten operar en el ámbito internacional.

    Servicios Ofrecidos
    Envíos Nacionales: Paquetes y Documentos, Encomiendas Especiales.
    Transporte de Carga Pesada: Transporte de maquinaria industrial, vehículos y equipos especializados.
    Logística Integral para Empresas: Gestión de Inventarios, Distribución y Almacenamiento.
    Servicios Internacionales: Envíos internacionales, gestión aduanera, y seguimiento en tiempo real.""", 'sitio_web': 'https://shalom.com.pe'},


    {'logo': 'static/images/dhl.png','nombre': 'DHL', 'sede_principal': 'Av. Inca Garcilaso de la Vega 1337, Cercado de Lima, Lima', 'descripcion': """DHL es una empresa global de logística y mensajería que opera en más de 220 países y territorios. Fundada en 1969 por Adrian Dalsey, Larry Hillblom y Robert Lynn, sus siglas derivan de los apellidos de los fundadores. DHL comenzó ofreciendo servicios de mensajería aérea, un concepto innovador que revolucionó la logística al permitir la entrega rápida de documentos a nivel internacional.

    Servicios Ofrecidos
    DHL Express: Especializado en envíos urgentes y entregas internacionales rápidas. Ofrece soluciones de transporte para documentos y paquetes con tiempos de entrega garantizados.
    DHL Global Forwarding: Gestión de fletes aéreos, marítimos y terrestres. Proporciona soluciones de transporte para grandes volúmenes de carga, incluyendo la coordinación y el despacho aduanero.
    DHL Freight: Transporte terrestre de cargas completas y parciales en toda Europa. Ofrece soluciones personalizadas para empresas que requieren transporte especializado.
    DHL Supply Chain: Logística de contratación para empresas, que incluye gestión de almacenes, distribución y optimización de la cadena de suministro. Este servicio es fundamental para empresas que buscan externalizar partes críticas de su logística.
    DHL ECommerce: Soluciones para el comercio electrónico, que incluyen la gestión de devoluciones, entregas a domicilio y opciones de entrega flexible.
    DHL SameDay: Servicios de entrega urgente el mismo día, ideal para envíos críticos que no pueden esperar.
    Infraestructura y Cobertura
    DHL cuenta con una vasta infraestructura global que incluye más de 350,000 empleados y alrededor de 260 aviones dedicados exclusivamente a sus operaciones logísticas. Su red global le permite manejar una gran variedad de envíos, desde pequeños paquetes hasta cargas industriales.""", 'sitio_web': 'https://www.dhl.com/pe-es/home.html'},


    {'logo': 'static/images/servientrega.png', 'nombre': 'Servientrega', 'sede_principal': 'Av. Argentina 1790, Cercado de Lima, Lima', 'descripcion': 'Servientrega es una compañía orientada a ofrecer soluciones integrales de logística en recolección, transporte, almacenamiento, empaque y embalaje, logística promocional y distribución de documentos y mercancías', 'sitio_web': 'https://servientrega.com.pe/'},


    {'logo': 'static/images/fedex.png', 'nombre': 'FedEx', 'sede_principal': 'Pasaje Martir Olaya 260', 'descripcion': """FedEx, o Federal Express, es una empresa multinacional de logística y servicios de mensajería con sede en Memphis, Tennessee, Estados Unidos. Fundada en 1971, FedEx comenzó sus operaciones en 1973 bajo el nombre original de Federal Express.

    Servicios
    FedEx Express: Servicios de mensajería y entrega exprés a nivel global.
    FedEx Ground: Entregas terrestres económicas en los EE.UU. y Canadá.
    FedEx Freight: Servicios de carga y transporte de mercancías pesadas.
    FedEx Office: Servicios de impresión y oficina, anteriormente conocido como Kinko's.
    FedEx Supply Chain: Soluciones de cadena de suministro y logística.
    Operaciones
    FedEx opera en más de 220 países y territorios, con una de las flotas aéreas más grandes del mundo, que cuenta con más de 600 aviones. Su hub principal es el aeropuerto de Memphis (MEM), conocido como el "Superhub".""", 'sitio_web': 'https://www.fedex.com/es-pe/home.html'},


    {'logo': 'static/images/ups.png', 'nombre': 'Ups', 'sede_principal': 'Jr. Flora Tristan 310, Magdalena, Lima', 'descripcion': """UPS (United Parcel Service) es una empresa global de logística y mensajería conocida por sus servicios de transporte y distribución. Fundada en 1907 como American Messenger Company y rebautizada como United Parcel Service en 1919, UPS comenzó con una flota de bicicletas y motocicletas antes de expandir su red para incluir camiones y aviones.

    Servicios
    UPS Ground: Servicios de entrega terrestre que abarcan los EE.UU., Canadá, y México, con tiempos de entrega basados en la distancia y el tipo de servicio seleccionado.
    UPS Air: Ofrece servicios de entrega urgente y programada a nivel nacional e internacional. Incluye opciones de entrega en un día, dos días y otros plazos.
    UPS Freight: Proporciona servicios de carga de mercancías pesadas y menos que carga (LTL), con cobertura en EE.UU., Canadá y México.
    UPS Supply Chain Solutions: Ofrece servicios integrales de gestión de la cadena de suministro, que incluyen logística, gestión de inventarios, distribución y soluciones de cadena de suministro personalizadas.
    UPS Store: Red de franquicias que proporciona servicios de impresión, envío de paquetes y soluciones de oficina a nivel nacional.
    UPS Capital: Servicios financieros y seguros, incluyendo protección de paquetes y soluciones de financiamiento.
    Operaciones
    Red Global: UPS opera en más de 220 países y territorios, con una red extensa que abarca entregas internacionales y nacionales.
    Hub Principal: El hub más importante de UPS es el Worldport en Louisville, Kentucky, que es uno de los centros de clasificación de paquetes más grandes del mundo.""", 'sitio_web': 'www.ups.com'},


    {'logo': 'static/images/urbano.png', 'nombre': 'Urbano', 'sede_principal': 'Avenida Materiales 3049, Cercado de Lima, Lima', 'descripcion': """Urbano es una empresa dedicada a ofrecer soluciones integrales de transporte y logística, con un enfoque en mejorar la eficiencia y cobertura en áreas urbanas y rurales.

    Fundada para ofrecer soluciones de transporte y logística, con un enfoque en mejorar la eficiencia y la cobertura en áreas urbanas y rurales.
    La empresa ha crecido para abarcar una red amplia de agencias y servicios, adaptándose a las necesidades cambiantes del mercado.
    Servicios
    Transporte de Mercancías: Ofrece servicios de transporte para paquetes y encomiendas, con opciones para envíos urgentes y estándar.
    Logística: Proporciona soluciones logísticas integrales que incluyen gestión de inventarios, distribución y cadena de suministro.
    Red de Agencias: Cuenta con una red de agencias en varias localidades para facilitar la entrega y recepción de mercancías.""", 'sitio_web': 'https://www.urbano.com.pe'},


    {'logo': 'static/images/transmar.png', 'nombre': 'Transmar', 'sede_principal': 'Avenida Nicolás Arriola 197, La Victoria', 'descripcion': """Transmar es una empresa líder en logística y mensajería, especializada en ofrecer soluciones de transporte y distribución eficientes a nivel global. Con un enfoque en la entrega exprés y la gestión de la cadena de suministro, Transmar se destaca por su compromiso con la puntualidad y la calidad en el servicio.

    Desarrollando y cultivando a través de cuatro décadas de experiencia en la industria en el sector del transporte y la logística, así como nuestra creciente presencia en el terreno en los principales puertos de la región, nos han dado una capacidad incomparable para satisfacer las necesidades de los clientes.

    Fiabilidad: En Transmar, honramos los compromisos de nuestros clientes, aprovechando nuestra experiencia en la industria y nuestra tecnología de punta para entregar los productos de la manera más confiable y rápida.

    Seguridad: Otorgamos un gran valor a la seguridad de nuestras operaciones marítimas, manteniendo los más altos estándares de conciencia de seguridad, disciplina del personal y responsabilidad individual.""", 'sitio_web': 'https://transmar.pe'},
]

datos_agencias = [
    #Olva Courier
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier Cercado De Lima', 'foto':'static/agencias_imagenes/olva_cercado_de_lima.png', 'direccion': 'Avenida Garcilazo de la Vega 1358 Cercado de Lima', 'link_mapa': 'https://maps.app.goo.gl/eAYMu6dSNMoKkpXt9', 'horario de atencion': '9:30am a 7:00pm - lunes a sábados', 'telefono': '7140909', 'cochera': False},
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier Rimac', 'foto':'static/agencias_imagenes/olva_rimac.png', 'direccion': 'Las Tapadas 198, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/pXgZaY3gkkLkhk6J6', 'horario de atencion': '9:30am a 7:30pm - lunes a sábado', 'telefono': '912156055', 'cochera': False},
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier La Victoria', 'foto': 'static/agencias_imagenes/olva_la_victoria.png', 'direccion': 'Jirón Antonio Bazo 1280, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/B4W32YXbNF2YywDK7', 'horario de atencion': '8:00am a 6:30pm - lunes a sábado', 'telefono': '7140908', 'cochera': True},
    {'empresa_nombre': 'Olva Courier', 'nombre_referencial': 'Olva Courier Miraflores', 'foto': 'static/agencias_imagenes/olva_miraflores.png', 'direccion': 'Avenida Comande Espinar 659, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/iDSyvBgCV1N7oLk79', 'horario de atencion': '8:00am a 7:00pm - lunes a sábado', 'telefono': '987655900', 'cochera': True},
    #Shalom
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom Rimac', 'foto': 'static/agencias_imagenes/shalom_rimac.png', 'direccion': 'Avenida Amancaes 644, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/WNJ1AdEQthXUCZyUA', 'horario de atencion': '8:30am a 7:00pm - lunes a sábado', 'telefono': '5007878', 'cochera': False},
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom La Victoria', 'foto': 'static/agencias_imagenes/shalom_la_victoria.png', 'direccion': 'Jirón Luna Pizarro, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/zmvvkb781rx2hv3f6', 'horario de atencion': '7:00am a 5:30pm - lunes a sábado', 'telefono': '7158800', 'cochera': True},
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom Breña', 'foto': 'static/agencias_imagenes/shalom_breña.png', 'direccion': 'Avenida República de Venezuela 1670, Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/SZvunBWwX2fXvBR98', 'horario de atencion': '9:00am a 7:00pm - lunes a sábado', 'telefono': '5452222', 'cochera': True},
    {'empresa_nombre': 'Shalom', 'nombre_referencial': 'Shalom Miraflores', 'foto': 'static/agencias_imagenes/shalom_miraflores.png', 'direccion': 'Avenida José Pardo 533, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/bNwtMwLNMFqFsiB99', 'horario de atencion': '8:00am a 6:30pm - lunes a sábado', 'telefono': '5007878', 'cochera': True},
    #DHL
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL La Victoria', 'foto': 'static/agencias_imagenes/dhl_la_victoria.png', 'direccion': 'Jirón Antonio Bazo 613,La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/DaEjazvTG6zdJQZp6', 'horario de atencion': '9:00am a 6:30pm - lunes a sábado', 'telefono': '94181895', 'cochera': False},
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL Breña', 'foto': 'static/agencias_imagenes/dhl_breña.png', 'direccion': 'Jirón Huaraz 1592,Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/GpLJ8sEVT24AK5FN9', 'horario de atencion': '8:30am a 6:30pm - lunes a sábado', 'telefono': '5172500', 'cochera': False},
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL Miraflores', 'foto': 'static/agencias_imagenes/dhl_miraflores.png', 'direccion': 'Avenida Alfredo Benavides 708, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/T9xT3sKxrnt2iG8w6', 'horario de atencion': '9:00am a 7:00pm - lunes a sábado', 'telefono': '932108772', 'cochera': False},
    {'empresa_nombre': 'DHL', 'nombre_referencial': 'DHL San Luis', 'foto': 'static/agencias_imagenes/dhl_san_luis.png', 'direccion': 'Avenida San Luis 2211, San Luis', 'link_mapa': 'https://maps.app.goo.gl/jF5Bgh4o3Z93t3UA9', 'horario de atencion': '9:00am a 6:30pm - lunes a sábado', 'telefono': '951369412', 'cochera': True},

    #Servientrega
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega Breña', 'foto': 'static/agencias_imagenes/servientrega_breña.png', 'direccion': 'Avenida Argentina 515,Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/8JHR76dn7tK4GJrY8', 'horario de atencion': '8:30am a 6:30pm ', 'telefono': '5653232', 'cochera': False},
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega Miraflores', 'foto': 'static/agencias_imagenes/servientrega_miraflores.png', 'direccion': 'Avenida Javier Prado, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/Tezb1w5zbqWdb3Uc8', 'horario de atencion': '8:30am a 6:30pm - lunes a sábado', 'telefono': '914668870', 'cochera': True},
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega San Luis', 'foto': 'static/agencias_imagenes/servientrega_san_luis.png', 'direccion': 'Avenida Agustín de la Rosa Toro 490, San Luis, Lima', 'link_mapa': 'https://maps.app.goo.gl/pc3bEapAXK6sysXG8', 'horario de atencion': '9:00am a 7:00pm - lunes a sábado', 'telefono': '914668870', 'cochera': True},
    {'empresa_nombre': 'Servientrega', 'nombre_referencial': 'Servientrega Cercado De Lima', 'foto': 'static/agencias_imagenes/servientrega_cercado_de_lima.png', 'direccion': 'Jirón de la Torre Ugarte 155, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/VTFRLcrtmkw2wJiQ6', 'horario de atencion': '8:30am a 7:00pm  - Lunes a sábado', 'telefono': '914668870', 'cochera': True},
    #Fedex
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx Miraflores', 'foto': 'static/agencias_imagenes/fedex_miraflores.png', 'direccion': 'Calle Alcanfores 350, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/TZbBQpChaRrrxscg9', 'horario de atencion': '8:30am a 7:30pm ', 'telefono': '6806120', 'cochera': True},
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx San Luis', 'foto': 'static/agencias_imagenes/fedex_san_luis.png', 'direccion': 'Avenida Ricardo Basilio 1382,San Luis, Lima', 'link_mapa': 'https://maps.app.goo.gl/TZbBQpChaRrrxscg9', 'horario de atencion': '9:00am a 6:00pm - Lunes a sábado', 'telefono': '6806120', 'cochera': True},
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx Cercado de lima', 'foto': 'static/agencias_imagenes/fedex_cercado_de_lima.png', 'direccion': 'Calle Los Cedros 350, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/Yj6gKCFntspQZ3dv7', 'horario de atencion': '8:30am a 6:30pm - lunes a sábado', 'telefono': '6806120', 'cochera': True},
    {'empresa_nombre': 'FedEx', 'nombre_referencial': 'FedEx Rimac', 'foto': 'static/agencias_imagenes/fedex_rimac.png', 'direccion': 'Calle Lomas de Almancaes 548, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/TZbBQpChaRrrxscg9', 'horario de atencion': '7:00am a 6:00pm - lunes a sábado', 'telefono': '6806120', 'cochera': True},
    #Ups
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups San Luis', 'foto': 'static/agencias_imagenes/ups_san_luis.png', 'direccion': 'Avenida Javier Prado Este 1500, San Luis, Lima', 'link_mapa': 'https://maps.app.goo.gl/WwbjGLPGoMdkRoG69', 'horario de atencion': '7:30am a 6:30pm - Lunes a sábado', 'telefono': '7155184', 'cochera': True},
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups Cercado De Lima', 'foto': 'static/agencias_imagenes/ups_cercado_de_lima.png', 'direccion': 'Jirón Huallaga 288, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/Zcgx18tg58RQLsxG6', 'horario de atencion': '10:00am a 7:30pm - Lunes a sábado', 'telefono': '969671160', 'cochera': True},
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups Rimac', 'foto': 'static/agencias_imagenes/ups_rimac.png', 'direccion': 'Jirón Santa Cecilia 1502, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/WLXwqUkJZ2Ucx4to6', 'horario de atencion': '9:30am a 5:30pm - lunes a sábado', 'telefono': '3184195', 'cochera': True},
    {'empresa_nombre': 'Ups', 'nombre_referencial': 'Ups La Victoria', 'foto': 'static/agencias_imagenes/ups_la_victoria.png', 'direccion': 'Avenida Elmer Faucett 158, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/4nyhtkNp3UiFhHr96', 'horario de atencion': '7:00am a 5:00pm - lunes a sábado', 'telefono': '6142500', 'cochera': True},
    #Urbano
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano Cercado De Lima', 'foto': 'static/agencias_imagenes/urbano_cercado_de_lima.png', 'direccion': 'Avenida Materiales 3049, Cercado de Lima, Lima', 'link_mapa': 'https://maps.app.goo.gl/99dJcASG76Fx9wn49', 'horario de atencion': '9:00am a 6:30pm - Lunes a sábado', 'telefono': '6323270', 'cochera': True},
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano Rimac', 'foto': 'static/agencias_imagenes/urbano_rimac.png', 'direccion': 'Calle San German 205, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/qHPZ7sFhS5ktERAX6', 'horario de atencion': '9:00am a 6:30pm - Lunes a sábado', 'telefono': '6323270', 'cochera': True},
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano La Victoria', 'foto': 'static/agencias_imagenes/urbano_la_victoria.png', 'direccion': 'Jirón Lucanas 671,La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/FyzLkxmKkjoapmed7', 'horario de atencion': '9:00am a 6:30pm', 'telefono': '6323270', 'cochera': False},
    {'empresa_nombre': 'Urbano', 'nombre_referencial': 'Urbano Breña', 'foto': 'static/agencias_imagenes/urbano_breña.png', 'direccion': 'Avenida Arica 150 Breña', 'link_mapa': 'https://maps.app.goo.gl/uGg8zh4GffZtU6sP7', 'horario de atencion': '9:00am a 7:00pm', 'telefono': '6323270', 'cochera': None},
    #Transmar
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar Rimac', 'foto': 'static/agencias_imagenes/transmar_rimac.png', 'direccion': 'Avenida 28 de Julio 1511, Rimac, Lima', 'link_mapa': 'https://maps.app.goo.gl/jmysdCK7CNKFsuwi9', 'horario de atencion': '7:00am a 6:30pm - Lunes a sábado', 'telefono': '2650190', 'cochera': True},
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar La Victoria', 'foto': 'static/agencias_imagenes/transmar_la_victoria.png', 'direccion': 'Avenida Bauzate y Meza 680, La Victoria, Lima', 'link_mapa': 'https://maps.app.goo.gl/w9t6nHMPj3PJiSQZA', 'horario de atencion': '8:00am a 6:00pm - Lunes a sábado', 'telefono': '995737290', 'cochera': True},
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar Breña ', 'foto': 'static/agencias_imagenes/transmar_breña.png', 'direccion': 'Jirón Pucallpa 266, Breña, Lima', 'link_mapa': 'https://maps.app.goo.gl/ZTCP5mU2tFp6EBLKA', 'horario de atencion': '8:00am a 7:30pm - Lunes a sábado', 'telefono': '995737290', 'cochera': False},
    {'empresa_nombre': 'Transmar', 'nombre_referencial': 'Transmar Miraflores', 'foto': 'static/agencias_imagenes/transmar_miraflores.png', 'direccion': 'Avenida Nicolás Arriola 197, Miraflores, Lima', 'link_mapa': 'https://maps.app.goo.gl/TJCCNZNK1VGiSGHs8', 'horario de atencion': '8:00am a 6:00pm - Lunes a sábado', 'telefono': '995737290', 'cochera': True},
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
        puntualidad=randint(0, 20),
        seguridad=randint(0, 20),
        economica=randint(0, 20),
        amabilidad=randint(0, 20),
        caro=randint(0, 20),
        inseguro=randint(0, 20),
        impuntual=randint(0, 20),
        poco_amables=randint(0, 20)
    )
    
    # Crear Estrellas para la Empresa
    Estrellas.objects.create(
        empresa=empresa,
        estrella_1=randint(0, 5),
        estrella_2=randint(0, 5),
        estrella_3=randint(0, 5),
        estrella_4=randint(0, 5),
        estrella_5=randint(0, 5),
    )

print("Datos de prueba creados exitosamente.")
