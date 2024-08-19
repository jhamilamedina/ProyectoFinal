import React, { useState } from 'react';
import axios from 'axios';
import './Inicio.css';

const Registro = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    email: '',
    contrasenia: '',
  });

  const [mensaje, setMensaje] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://localhost:8000/api/usuarios/', formData)
      .then(response => {
        setMensaje('Usuario creado con éxito');
        console.log(response.data);
      })
      .catch(error => {
        if (error.response) {
          const errorMessage = typeof error.response.data === 'string'
            ? error.response.data
            : JSON.stringify(error.response.data);
          setMensaje(errorMessage);
        } else {
          setMensaje('Error al crear el usuario');
        }
      });
  };

  return (
    <div className="registro-container"> {/* Aplicar la clase aquí */}
      <h2>Crear Cuenta</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nombre:</label>
          <input 
            type="text"
            name='nombre'
            value={formData.nombre}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Email:</label>
          <input 
            type='email'
            name='email'
            value={formData.email}
            onChange={handleChange}
            required
          /> 
        </div>
        <div>
          <label>Contraseña:</label>
          <input 
            type='password'
            name='contrasenia'
            value={formData.contrasenia}
            onChange={handleChange}
            required
          />
        </div>
        <button type='submit'>Registrar</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
};

export default Registro;
