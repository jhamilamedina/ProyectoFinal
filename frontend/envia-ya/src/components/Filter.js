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
    const [agencies, setAgencies] = useState([]);

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
                    setProvinces(response.data.Provincias);
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
                    setDistricts(response.data.Distritos);
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
        if (district) {
            axios.get(`http://localhost:8000/api/agenciasdistritos/${district}/`)
                .then(response => {
                    let filteredAgencies = response.data.Agencias;

                    if (origin) {
                        filteredAgencies = filteredAgencies.filter(agency =>
                            agency.direccion.includes(origin)
                        );
                    }
                    setAgencies(filteredAgencies);
                })
                .catch(error => {
                    console.error('Error fetching agencies', error);
                });
        }
    };

    return (
        <div className='filter-container'>
            <h2>Buscador de Agencias</h2>
            <div>
                <label>
                    Origen (Lima Metropolitana):
                    <select value={origin} onChange={(e) => setOrigin(e.target.value)}>
                        <option value="">Seleccione un distrito</option>
                        <option value="Cercado de Lima">Cercado de Lima</option>
                        <option value="Ancón">Ancón</option>
                        <option value="Ate">Ate</option>
                        <option value="Barranco">Barranco</option>
                        <option value="Breña">Breña</option>
                        <option value="Carabayllo">Carabayllo</option>
                        <option value="Chaclacayo">Chaclacayo</option>
                        <option value="Chorrillos">Chorrillos</option>
                        <option value="Cieneguilla">Cieneguilla</option>
                        <option value="Comas">Comas</option>
                        <option value="El Agustino">El Agustino</option>
                        <option value="Huaycán">Huaycán</option>
                        <option value="Independencia">Independencia</option>
                        <option value="Jesús María">Jesús María</option>
                        <option value="La Molina">La Molina</option>
                        <option value="La Victoria">La Victoria</option>
                        <option value="Lince">Lince</option>
                        <option value="Los Olivos">Los Olivos</option>
                        <option value="Lurigancho">Lurigancho</option>
                        <option value="Lurín">Lurín</option>
                        <option value="Magdalena del Mar">Magdalena del Mar</option>
                        <option value="Miraflores">Miraflores</option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                        <option value=""></option>
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Departamento:
                    <select value={department} onChange={(e) => setDepartment(e.target.value)}>
                        <option value="">Seleccione un departamento*</option>
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
                        <option value="">Seleccione una provincia*</option>
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
                        <option value="">Seleccione un distrito*</option>
                        {districts.map((dist) => (
                            <option key={dist.id} value={dist.id}>{dist.nombre}</option>
                        ))}
                    </select>
                </label>
            </div>
            <button onClick={handleSearch}>Buscar</button>
            <div className="agencies-list">
                <h3>Agencias en el distrito seleccionado:</h3>
                {agencies.length > 0 ? (
                    <ul>
                        {agencies.map((agency) => (
                            <li key={agency.id}>
                                <h4>{agency.nombre_referencial}</h4>
                                <p>{agency.direccion}</p>
                                <p>Horario de atención: {agency.horario_de_atencion}</p>
                                <p>Teléfono: {agency.telefono}</p>
                                <p>Cochera: {agency.cochera ? 'Sí' : 'No'}</p>
                                <a href={agency.link_mapa} target="_blank" rel="noopener noreferrer">Ver en mapa</a>
                                <br></br>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>No se encontraron agencias para el distrito seleccionado :c</p>
                )}
            </div>
        </div>
    );
};

export default Filter;