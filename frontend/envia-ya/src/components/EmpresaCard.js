// import React, { useState } from 'react';
// import { Link } from 'react-router-dom';
import React from 'react';
import './Empresas.css';

const EmpresaCard = ({ id, logo, nombre, direccion, descripcion, sitio_web }) => {
  return (
    <div className="host-card">
      <div className="host-info">
        <div className="host-details">
        <img src={`http://localhost:8000/${logo}`} alt={`${nombre} logo`} />
          <h2><a href={`http://localhost:3000/empresas/${id}/`}>{nombre}</a></h2>
          <p><strong>Oficina Principal: </strong>{direccion}</p>
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
