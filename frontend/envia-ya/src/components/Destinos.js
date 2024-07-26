import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Filter from './Filter';
import './Destinos.css';
import shalomImage from '../assets/agencias_fotos/shalom_mexico.jpeg'

const agenciasData = [
    {
        id: 1,
        empresa: 'Shalom',
        referencial: 'Av. México',
        direccion: 'Av. México 1234, La Victoria',
        foto: {shalomImage},
        horario: '08:00 - 18:00',
        telefono: 987654321,
        cochera: 1,
        destinos: ['Huamanga', 'Characato', 'La Joya', 'Chiguata'],
        mapa: 'https://maps.app.goo.gl/Nf7Zs8ZHNrkeJa4i7'
    },
    {
        id: 2,
        empresa: 'Oltursa',
        referencial: 'Av. Javier Prado',
        direccion: 'Av. Javier Prado 5678, Lima',
        foto: 'ruta/a/la/foto2.jpg',
        horario: '07:00 - 20:00',
        telefono: 987654322,
        cochera: 1,
        destinos: ['Trujillo', 'Chiclayo', 'Ica'],
        mapa: 'https://goo.gl/maps/abcd5678'
      },
];

const Destinos = () => {
    const [filteredAgencias, setFilteredAgencias] = useState([]);

    const handleSearch = ({ origin, district }) => {
        const filtered = agenciasData.filter(
            agencias =>
                agencias.direccion.includes(origin) &&
                agencias.destinos.includes(district)
        );
        setFilteredAgencias(filtered);
    };

    return (
        <div>
            <h1>Buscar Agencias de Envíos</h1>
            <Filter onSearch={handleSearch} />
            <div>
                {filteredAgencias.map((agencia, index) => (
                    <div key={index} className='agencia-card'>
                        <h2>{`${agencia.empresa} - ${agencia.referencial}`}</h2>
                        <p>Dirección: {agencia.direccion}</p>
                        <p>Destinos: <strong>{agencia.destinos.join(', ')}</strong></p>
                        <p>Horario de atención: <strong>{agencia.horario}</strong></p>
                        <p>Mapa: <a href={agencia.mapa}>Ver ubicación</a></p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Destinos;