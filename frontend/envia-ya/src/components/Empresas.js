import React, { useState, useEffect } from 'react';
import axios from 'axios';
import EmpresaCard from './EmpresaCard';
import './Empresas.css';

const Empresas = () => {
  const [empresas, setEmpresas] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/empresas/')
      .then(response => {
        setEmpresas(response.data);
      })
      .catch(error => {
        console.error('Error fetching empresas:', error);
      });
  }, []);

  // Función para truncar la descripción
  const truncateDescription = (description, maxLength) => {
    if (description.length > maxLength) {
      return description.substring(0, maxLength) + '...';
    }
    return description;
  };

  return (
    <div className="empresas-container">
      <h2>Lista de Empresas</h2>
      <div className="empresas-list">
        {empresas.map((empresa) => (
          <EmpresaCard
            key={empresa.id}
            id={empresa.id}
            logo={empresa.logo}
            nombre={empresa.nombre}
            direccion={empresa.sede_principal}
            descripcion={truncateDescription(empresa.descripcion, 200)}
            sitio_web={empresa.sitio_web}
          />
        ))}
      </div>
    </div>  
  );
};

export default Empresas;
