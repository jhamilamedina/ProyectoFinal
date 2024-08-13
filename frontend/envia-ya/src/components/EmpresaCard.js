// import React, { useState } from 'react';
// import { Link } from 'react-router-dom';
import React from 'react';
import './Empresas.css';

const EmpresaCard = ({ nombre, direccion, descripcion, sitio_web }) => {
  return (
    <div className="host-card">
      <div className="host-info">
        <div className="host-details">
          <h2>{nombre}</h2>
          <p>{direccion}</p>
        </div>
      </div>
      <p className="host-description">
        {descripcion}
      </p>
      <p className="external-info">
        <a href={sitio_web}>Ver sitio web</a>
      </p>
    </div>
  );
};

export default EmpresaCard;
