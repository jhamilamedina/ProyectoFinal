import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Filter.css';

const Filter = ({ onSearch }) => {
    const [departments, setDepartments] = useState([]);
    const [provinces, setProvinces] = useState([]);
    const [districts, setDistricts] = useState([]);
    const [origin, setOrigin] = useState('');
    const [department, setDepartment] = useState('');
    const [province, setProvince] = useState('');
    const [district, setDistrict] = useState('');

    useEffect(() => {
        // Fetch departments
        axios.get('http://localhost:8000/api/departamentos/')
            .then(response => {
                setDepartments(response.data);
            })
            .catch(error => {
                console.error('Error fetching departments:', error);
            });
    }, []);

    useEffect(() => {
        // Fetch provinces
        if (department) {
            axios.get(`http://localhost:8000/api/departamentos/${department}/`)
                .then(response => {
                    setProvinces(response.data.provincias);
                    setProvince('');
                    setDistrict('');
                })
                .catch(error => {
                    console.error('Error fetching provinces:', error);
                });
        } else {
            setProvinces([]);
            setProvince('');
            setDistrict('');
        }
    }, [department]);

    useEffect(() => {
        if (province) {
            axios.get(`http://localhost:8000/api/provincias/${province}/`)
                .then(response => {
                    setDistricts(response.data.distrito);
                    setDistrict('');
                })
                .catch(error => {
                    console.error('Error fetching districts:', error);
                });
        } else {
            setDistricts([]);
            setDistrict('');
        }
    }, [province]);

    const handleSearch = () => {
        onSearch({ origin, department, province, district });
    };

    return (
        <div className='filter-container'>
            <h2>Buscador de Agencias</h2>
            <div>
                <label>
                    Origen (Lima Metropolitana):
                    <select value={origin} onChange={(e) => setOrigin(e.target.value)}>
                        <option value="">Seleccione un distrito</option>
                        <option value="Miraflores">Miraflores</option>
                        <option value="San Isidro">San Isidro</option>
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Departamento:
                    <select value={department} onChange={(e) => setDepartment(e.target.value)}>
                        <option value="">Seleccione un departamento</option>
                        {departments.map((dept) => (
                            <option key={dept.id} value={dept.id}>{dept.nombre}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Provincia:
                    <select value={province} onChange={(e) => setProvince(e.target.value)} disabled={!department}>
                        <option value="">Seleccione una provincia</option>
                        {provinces.map((prov) => (
                            <option key={prov.id} value={prov.id}>{prov.nombre}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Distrito:
                    <select value={district} onChange={(e) => setDistrict(e.target.value)} disabled={!province}>
                        <option value="">Seleccione un distrito</option>
                        {districts.map((dist) => (
                            <option key={dist.id} value={dist.id}>{dist.nombre}</option>
                        ))}
                    </select>
                </label>
            </div>
            <button onClick={handleSearch}>Buscar</button>
        </div>
    );
};

export default Filter;
