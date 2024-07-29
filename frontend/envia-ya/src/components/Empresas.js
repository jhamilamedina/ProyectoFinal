import React from 'react';
import EmpresaCard from './EmpresaCard';

import logoOlva from '../assets/empresas_fotos/olva_logo.jpg';

import './Empresas.css';

const Empresas = () => {
  const empresasData = [
    {
      nombre: "Olva Courier",
      direccion: "Avenida Argentina 4458, Callao, Perú",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "Especialistas en última milla, brindando servicios de calidad en transporte de encomiendas a domicilio o a cualquiera de nuestras tiendas o agentes a nivel ...",
      mapaUrl: "https://www.google.com/maps/place/Olva+Courier+Central/@-12.0486303,-77.0993648,15z/data=!4m6!3m5!1s0x9105c954339772e7:0xa66e7836d17a0617!8m2!3d-12.0486303!4d-77.0993648!16s%2Fg%2F11bxc7kpx2?entry=ttu",
      logoUrl: logoOlva
    },
    {
      nombre: "Shalóm",
      direccion: "Avenida México 1187,Cercado de Lima, Perú",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "Shalom tiene una amplia red de distribución de puntos de entrega y acopio en los 24 departamentos del Perú",
      mapaUrl: "https://www.google.com/maps/place/Av.+M%C3%A9xico+1187,+Lima+15033/@-12.0734046,-77.0201806,17z/data=!3m1!4b1!4m6!3m5!1s0x9105c89b35fbbe8d:0x3d0d514b446e946e!8m2!3d-12.0734099!4d-77.0176057!16s%2Fg%2F11gbld_n73?entry=ttu",
      logoUrl: ""
    },
    {
      nombre: "DHL",
      direccion: "Av. Inca Garcilaso de la Vega 1337, Cercado de Lima, Lima",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "DHL es una empresa líder en logística a nivel mundial, especializada en envíos internacionales, servicios de mensajería y transporte ",
      mapaUrl: "https://www.google.com/maps/place/1337,+Av.+Garcilaso+de+la+Vega+1337,+Lima+15001/@-12.057,-77.0403334,17z/data=!3m1!4b1!4m6!3m5!1s0x9105c8c6b87c1e8d:0x4e5e7bf312868c3c!8m2!3d-12.0570053!4d-77.0377585!16s%2Fg%2F11jym_9wsl?entry=ttu",
      logoUrl: ""
    },
    {
      nombre: "Servientrega",
      direccion: "Av. Argentina 1790, Cercado de Lima, Lima",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "Servientrega es una compañía orientada a ofrecer soluciones integrales de logística en recolección, transporte, almacenamiento, empaque y embalaje, logística ",
      mapaUrl: "https://www.google.com/maps/place/Av.+Argentina+1790,+Lima+15081/@-12.0449734,-77.0652634,17z/data=!4m6!3m5!1s0x9105c92d002f1e9d:0x4b1408d0f77b4f03!8m2!3d-12.0450014!4d-77.0651034!16s%2Fg%2F11fw279k2t?entry=ttu",
      logoUrl: ""
    },
    {
      nombre: "FedEx",
      direccion: "Pasaje Martir Olaya 260 , Miraflores , Perú",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "FedEx es una empresa de servicios de mensajería y logística que opera en Perú y a nivel mundial",
      mapaUrl: "https://www.google.com/maps/place/C.+M%C3%A1rtir+Jos%C3%A9+Olaya+260,+Miraflores+15074/@-12.1206129,-77.0328449,17z/data=!3m1!4b1!4m6!3m5!1s0x9105c819b5cbd65d:0xc2ad0303ca0d4048!8m2!3d-12.1206182!4d-77.03027!16s%2Fg%2F11cs6c0c7w?entry=ttu",
      logoUrl: ""
    },
    {
      nombre: "Ups",
      direccion: "Jr. Flora Tristan 310, Magdalena, Lima",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "UPS ofrece opciones para envíos de bajo y gran volumen.",
      mapaUrl: "https://www.google.com/maps/place/Flora+Trist%C3%A1n+310,+Magdalena+del+Mar+15076/@-12.0942405,-77.0599095,17z/data=!3m1!4b1!4m6!3m5!1s0x9105c9acc5ac5557:0xf5b209e5a0b74f30!8m2!3d-12.0942458!4d-77.0573346!16s%2Fg%2F11fw24m26g?entry=ttu",
      logoUrl: ""
    },
    {
      nombre: "Urbano",
      direccion: "Avenida Materiales 3049, Cercado de Lima, Lima",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "Urbano es una empresa de servicios logísticos en Perú. Su enfoque está en planificación urbana y desarrollo.",
      mapaUrl: "https://www.google.com/maps/place/Av.+Materiales+3049,+Lima+15081/@-12.0428993,-77.0841263,17z/data=!3m1!4b1!4m6!3m5!1s0x9105ceb532688bf7:0x71c9a08a61f93b7a!8m2!3d-12.0429046!4d-77.0815514!16s%2Fg%2F11thrq7dj4?entry=ttu",
      logoUrl: ""
    },
    {
      nombre: "Transmar",
      direccion: "Avenida Nicolás Arriola 197, La Victoria",
      evaluaciones: 2,
      valoracion: 0,
      caracteristicas: ["Puntualidad", "Seguridad", "Económica", "Amabilidad", "Caro", "Inseguro", "Impuntual"],
      descripcion: "Transmar es un grupo empresarial con 39 años de experiencia en el servicio de transporte ",
      mapaUrl: "https://www.google.com/maps/place/Av+Nicol%C3%A1s+Arriola+197,+La+Victoria+15034/@-12.0886491,-77.0199107,17z/data=!3m1!4b1!4m6!3m5!1s0x9105c87c393eeb45:0x7a4341d31cd20ce7!8m2!3d-12.0886544!4d-77.0173358!16s%2Fg%2F11c1xg6z3x?entry=ttu",
      logoUrl: ""
    }
  ];

  return (
    <div className="host-list">
      {empresasData.map((empresa, index) => (
        <EmpresaCard
          key={index}
          nombre={empresa.nombre}
          direccion={empresa.direccion}
          evaluaciones={empresa.evaluaciones}
          valoracion={empresa.valoracion}
          caracteristicas={empresa.caracteristicas}
          descripcion={empresa.descripcion}
          mapaUrl={empresa.mapaUrl}
          logoUrl={empresa.logoUrl}
        />
      ))}
    </div>
  );
};

export default Empresas;
