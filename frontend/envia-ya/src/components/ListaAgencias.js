import React from 'react';
import DetallesAgencias from './DetallesAgencias';
import './DetallesAgencias.css';

const ListaAgencias = () => {
  const empresasData = [
    {
      nombre: "Olva Courier",
      direccion: "Avenida Garcilazo de la Vega 1358 Cercado de Lima",
      evaluaciones: 2,
      valoracion: 4,
      telefono: "7140909",
      horarios: "9:30am a 7pm lunes a sábado",
      web: "https://www.olvacourier.com/",
      correo: "ventas@olva.com.pe",
      cochera: "No",
      recojoDomicilio: "No",
      entregaDomicilio: "Sí",
      seguimientoPedido: "Sí",
      mapaUrl: "https://maps.app.goo.gl/eAYMu6dSNMoKkpXt9",
      mapaImageUrl: "", // Asegúrate de tener la imagen del mapa
      logoUrl: "https://lh5.googleusercontent.com/p/AF1QipNI8_JonuQlBaXwMw9nGKu_ES1V6nX2DfJjuRm_=w426-h240-k-no" // Asegúrate de tener la imagen del logo
    },
    {
      nombre: "Olva Courier",
      direccion: "Las Tapadas 198, Rimac, Lima",
      evaluaciones: 3,
      valoracion: 3,
      telefono: "912156055",
      horarios: "9:30am a 7:30pm lunes a sábado",
      web: "https://www.olvacourier.com/",
      correo: "ventas@olva.com.pe",
      cochera: "No",
      recojoDomicilio: "Si",
      entregaDomicilio: "Sí",
      seguimientoPedido: "no",
      mapaUrl: "https://maps.app.goo.gl/pXgZaY3gkkLkhk6J6",
      mapaImageUrl: "", // Asegúrate de tener la imagen del mapa
      logoUrl: "" // Asegúrate de tener la imagen del logo
    },
    {
      nombre: "Olva Courier",
      direccion: "Jirón Antonio Bazo 1280, La Victoria, Lima",
      evaluaciones: 2,
      valoracion: 5,
      telefono: "7140908",
      horarios: "9:30am a 7pm lunes a sábado",
      web: "https://www.olvacourier.com/",
      correo: "ventas@olva.com.pe",
      cochera: "Sí",
      recojoDomicilio: "No",
      entregaDomicilio: "Sí",
      seguimientoPedido: "Sí",
      mapaUrl: "https://maps.app.goo.gl/B4W32YXbNF2YywDK7",
      mapaImageUrl: "", // Asegúrate de tener la imagen del mapa
      logoUrl: "" // Asegúrate de tener la imagen del logo
    },
    {
      nombre: "Olva Courier",
      direccion: "Avenida Comande Espinar 659, Miraflores, Lima",
      evaluaciones: 3,
      valoracion: 3,
      telefono: "987655900",
      horarios: "8:00am a 7:00pm lunes a sábado",
      web: "https://www.olvacourier.com/",
      correo: "ventas@olva.com.pe",
      cochera: "Sí",
      recojoDomicilio: "No",
      entregaDomicilio: "Sí",
      seguimientoPedido: "Sí",
      mapaUrl: "https://maps.app.goo.gl/iDSyvBgCV1N7oLk79",
      mapaImageUrl: "", // Asegúrate de tener la imagen del mapa
      logoUrl: "" // Asegúrate de tener la imagen del logo
    },
    
  ];

  return (
    <div className="lista-agencias">
      {empresasData.map((empresa, index) => (
        <DetallesAgencias key={index} empresa={empresa} />
      ))}
    </div>
  );
};

export default ListaAgencias;
