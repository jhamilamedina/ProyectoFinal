import React from 'react';
import { Link } from 'react-router-dom';
import EstrellasRating from './EstrellasRating';

import './Empresas.css';

const EmpresaCard = ({ nombre, direccion, evaluaciones, valoracion, caracteristicas, descripcion, mapaUrl, logoUrl }) => {
  return (
    <div className="host-card">
      <div className="host-info">
        <img className="Olva" src={logoUrl} alt={`${nombre}_logo`} />
        <div className="host-details">
          <h2>{nombre}</h2>
          <p>{direccion}</p>
          <div className="host-stats">
            <Link to="/Evaluacion">{evaluaciones} Evaluaciones</Link>
            <div className="rating-container">
              <Link to="/rating-pagina" className="rating-link">{valoracion} Valoración</Link>
              <EstrellasRating rating={valoracion} />
            </div>
          </div>
        </div>
      </div>
      <div className="host-extra-info">
        {caracteristicas.map((caracteristica, index) => (
          <p key={index}><i className="fas fa-briefcase"></i> {caracteristica}</p>
        ))}
      </div>
      <p className="host-description">
        {descripcion}
      </p>
      <Link to="/Evaluacion" className="show-more-link">Mostrar más evaluaciones</Link>
      <p>
        <i className="fas fa-map-marker-alt"></i> 
        <a href={mapaUrl} target="_blank" rel="noopener noreferrer">
          Ver mapa de ubicación
        </a>
      </p>
    </div>
  );
};

export default EmpresaCard;
