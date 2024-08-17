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

  return (
    <div className="empresas-container">
      <h2>Lista de Empresas</h2>
      <div className="empresas-list">
        {empresas.map((empresa) => (
          <EmpresaCard
            key={empresa.id}
            id={empresa.id}
            nombre={empresa.nombre}
            direccion={empresa.sede_principal}
            descripcion={empresa.descripcion}
            sitio_web={empresa.sitio_web}
          />
        ))}
      </div>
    </div>  
  );
};
export default Empresas;
