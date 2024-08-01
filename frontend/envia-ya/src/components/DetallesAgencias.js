import React from 'react';
import './DetallesAgencias.css';
import EstrellasRating from './EstrellasRating'; // Asegúrate de tener este componente implementado

const DetallesAgencias = ({ empresa }) => {
  return (
    <div className="empresa-card">
      
      <div className="empresa-header">
        <div>
          <img src={empresa.logo} alt={empresa.nombre} className="empresa-logo" />
          <h2>{empresa.nombre}</h2>
        </div>
        <div className="empresa-rating">
          <div className="stars">
            <EstrellasRating rating={empresa.valoracion} />
          </div>
          <a href="/comentarios" className="empresa-comment-link">{empresa.evaluaciones} comentarios</a>
        </div>
      </div>
      <div className="empresa-info">
        <p>{empresa.direccion}</p>
        <div className="empresa-contact">
          <strong>DATOS DE CONTACTO Y ATENCIÓN</strong>
          <ul>
            <li>Dirección: {empresa.direccion}</li>
            <li>Teléfono: {empresa.telefono}</li>
            <li>Horarios de atención: {empresa.horarios}</li>
            <li>Web: <a href={empresa.web} target="_blank" rel="noopener noreferrer">{empresa.web}</a></li>
            <li>Correo de contacto: {empresa.correo}</li>
            <li>cochera: {empresa.cochera}</li>
            <li>Recojo a domicilio: {empresa.recojoDomicilio}</li>
            <li>Entrega a domicilio: {empresa.entregaDomicilio}</li>
            <li>Seguimiento de pedido: {empresa.seguimientoPedido}</li>
          </ul>
        </div>
      </div>
      <div className="empresa-description">
        <p>{empresa.descripcion}</p>
      </div>
      <div className="empresa-map">
        <h3>Ver en mapa</h3>
        <a href={empresa.mapaUrl} target="_blank" rel="noopener noreferrer">
          <img src={empresa.mapaImageUrl} alt="Mapa de ubicación" />
        </a>
      </div>
    </div>
  );
};

export default DetallesAgencias;
