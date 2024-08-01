import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import EstrellasRating from './EstrellasRating';
import PropTypes from 'prop-types';

import './Empresas.css';

const EmpresaCard = ({ nombre, direccion, evaluaciones, valoracion, caracteristicas, descripcion, mapaUrl, webUrl, logoUrl, detallesUrl }) => {
  const [rating, setRating] = useState(valoracion);

  const handleRatingChange = (newRating) => {
    setRating(newRating);
  };

  return (
    <div className="empresa-card">
      <div className="empresa-info">
        <img className="empresa-logo" src={logoUrl} alt={`${nombre}_logo`} />
        <div className="empresa-details">
          <h2>
            <a href={webUrl} target="_blank" rel="noopener noreferrer">
              {nombre}
            </a>
          </h2>
          <p>{direccion}</p>
          <div className="empresa-stats">
            <Link to="/evaluacion">{evaluaciones} Comentarios</Link>
            <div className="rating-container">
              <Link to="/rating-pagina" className="rating-link">{rating} Valoración</Link>
              <EstrellasRating rating={rating} onRatingChange={handleRatingChange} />
            </div>
          </div>
        </div>
      </div>
      <div className="empresa-extra-info">
        {caracteristicas.map((caracteristica, index) => (
          <div key={index} className="caracteristica">
            <input type="checkbox" defaultChecked />
            <p>{caracteristica}</p>
          </div>
        ))}
      </div>
      <p className="empresa-description">
        {descripcion}
      </p>
      <Link to={detallesUrl} className="show-more-link">Más detalles de la empresa</Link>
      <p>
        <i className="fas fa-map-marker-alt"></i> 
        <a href={mapaUrl} target="_blank" rel="noopener noreferrer">
          Ver mapa de ubicación
        </a>
      </p>
    </div>
  );
};

EmpresaCard.propTypes = {
  nombre: PropTypes.string.isRequired,
  direccion: PropTypes.string.isRequired,
  evaluaciones: PropTypes.number.isRequired,
  valoracion: PropTypes.number.isRequired,
  caracteristicas: PropTypes.arrayOf(PropTypes.string).isRequired,
  descripcion: PropTypes.string.isRequired,
  mapaUrl: PropTypes.string.isRequired,
  webUrl: PropTypes.string.isRequired,
  logoUrl: PropTypes.string,
  detallesUrl: PropTypes.string.isRequired
};

export default EmpresaCard;
