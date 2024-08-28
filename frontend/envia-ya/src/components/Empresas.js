import React, { useState, useEffect } from 'react';
import axios from 'axios';
import EmpresaCard from './EmpresaCard';
import './Empresas.css';

const Empresas = () => {
  const [empresas, setEmpresas] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/empresas/')
      .then(response => {
        setEmpresas(response.data);
      })
      .catch(error => {
        console.error('Error fetching empresas:', error);
      });
  }, []);

<<<<<<< HEAD
  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  // Filtra las empresas según el término de búsqueda
  const filteredEmpresas = empresas.filter(empresa =>
    empresa.nombre.toLowerCase().includes(searchTerm.toLowerCase())
  );

=======
  // Función para truncar la descripción
  const truncateDescription = (description, maxLength) => {
    if (description.length > maxLength) {
      return description.substring(0, maxLength) + '...';
    }
    return description;
  };

>>>>>>> 13ee243f452153e2f4585bb2e92158bfa49f4607
  return (
    <div className="empresas-container">
      <h2>Lista de Empresas</h2>
      <input
        type="text"
        placeholder="Buscar por nombre"
        value={searchTerm}
        onChange={handleSearchChange}
        className="search-input"
      />
      <div className="empresas-list">
        {filteredEmpresas.map((empresa) => (
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
