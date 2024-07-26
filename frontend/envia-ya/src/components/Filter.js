import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Filter.css';

const Filter = ({ onSearch }) => {
    const districsLima = ['Miraflores', 'San Isidro', 'Barranco', 'Surco', 'La Molina', 'La Victoria'];
    const destinations = {
        "Lima": {
          "Lima": ["Miraflores", "San Isidro", "Barranco", "Surco", "La Molina"],
          "Callao": ["Bellavista", "Carmen de La Legua", "La Perla", "La Punta", "Ventanilla"]
        },
        "Arequipa": {
          "Arequipa": ["Cayma", "Cerro Colorado", "Characato", "Chiguata", "Jacobo Hunter"],
          "Camana": ["Camana", "Mariscal Caceres", "Nicolas de Pierola", "Ocoña", "Quilca"]
        }
    };

    const [origin, setOrigin] = useState('');
    const [department, setDepartment] = useState('');
    const [province, setProvince] = useState('');
    const [district, setDistrict] = useState('');

    const handleDepartmentChange = (e) => {
        setDepartment(e.target.value);
        setProvince(''); // Reset province
        setDistrict(''); // Reset district
    };

    const handleProvinceChange = (e) => {
        setProvince(e.target.value);
        setDistrict(''); // Reset district
    };

    const handleSearch = () => {
        onSearch({ origin, department, province, district});
    };

    return (
        <div className='filter-container'>
            <h2>Buscador de Agencias</h2>
            <div>
                <label>
                    Origen (Lima Metropolitana):
                    <select value={origin} onChange={(e) => setOrigin(e.target.value)}>
                        <option value="">Seleccione un distrito</option>
                        {districsLima.map((district) => (
                            <option key={district} value={district}>{district}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Departamento:
                    <select value={department} onChange={handleDepartmentChange}>
                        <option value="">Seleccione un departamento</option>
                        {Object.keys(destinations).map((dept) => (
                            <option key={dept} value={dept}>{dept}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Provincia:
                    <select
                        value={province}
                        onChange={handleProvinceChange}
                        disabled={!department}
                    >
                        <option value="">Seleccione una provincia</option>
                        {department && Object.keys(destinations[department]).map((prov) => (
                            <option key={prov} value={prov}>{prov}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Distrito:
                    <select
                        value={district}
                        onChange={(e) => setDistrict(e.target.value)}
                        disabled={!province}
                    >
                        <option value="">Seleccione un distrito</option>
                        {province && destinations[department][province].map((dist) => (
                            <option key={dist} value={dist}>{dist}</option>
                        ))}
                    </select>
                </label>
            </div>
            <button onClick={handleSearch}>Buscar</button>
        </div>
    );
};

export default Filter;