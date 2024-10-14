import React, { useState } from 'react';
import Filter from './Filter';
import './Destinos.css';

const Destinos = () => {
    const [filteredAgencias, setFilteredAgencias] = useState([]);

    const handleSearch = ({ origin, district }) => {
        setFilteredAgencias(filteredAgencias);
    };

    return (
        <div className="destinos-container">
            <h1>Buscar Agencias de Envíos</h1>
            <Filter onSearch={handleSearch} />
        </div>
    );
};

export default Destinos;
