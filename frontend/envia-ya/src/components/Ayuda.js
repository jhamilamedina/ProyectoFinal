import React from 'react';
import { Link } from 'react-router-dom';
import './Ayuda.css';

const FAQ = () => {
  return (
    <div className="faq">
      <h1>Preguntas frecuentes</h1>
      <h2>¿Qué es envía ya?</h2>
      <p>Envía ya es una plataforma web en donde podrás comparar la calidad de servicio de distintas agencias de envío que existen en Lima.</p>
      <h2>¿Cómo funciona?</h2>
      <p>Al acceder a nuestra web, podrás filtrar por el lugar a donde deseas enviar. Luego podrás ver la relación de empresas más cercanas y podrás escoger la que mejor se acomode a tus necesidades.</p>
      <h2>¿Puedo hacer pagos en Envía ya?</h2>
      <p>No. Nuestra web es sólo informativa. No se pueden realizar pagos.</p>
      <h2>¿Hacen envíos?</h2>
      <p>No. Solo te mostraremos información transparente de las agencias de envíos. Te facilitaremos todos sus datos de contacto y servicios para que realices los envíos directamente desde sus páginas.</p>
      <h2>¿Tienen alguna guía para poder usar la página?</h2>
      <p>Sí, te adjunto el PDF para que puedas realizar tu navegación de manera más fácil.</p>
      <p><a href="/infografia_envia_ya.pdf" target="_blank" rel="noopener noreferrer">Descargar Guía</a></p>
      <h2>
        <Link to="/contacto">¿Aún tienes dudas? Contáctanos aquí</Link>
      </h2>
    </div>
  );
};

export default FAQ;
