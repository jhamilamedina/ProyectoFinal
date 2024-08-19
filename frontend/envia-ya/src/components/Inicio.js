import React, { useState } from 'react';
import axios from 'axios';
import './Inicio.css';

const Login = () => {
  const [formData, setFormData] = useState({
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

    axios.post('http://localhost:8000/api/login/', formData)
      .then(response => {
        setMensaje(`Inicio de sesión exitoso. Bienvenido, ${response.data.nombre}`);
        console.log(response.data);
      })
      .catch(error => {
        if (error.response) {
          const errorMessage = typeof error.response.data === 'string'
            ? error.response.data
            : JSON.stringify(error.response.data);
          setMensaje(errorMessage);
        } else {
          setMensaje('Error al iniciar sesión');
        }
      });
  };

  return (
    <div>
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit}>
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
        <button type='submit'>Iniciar Sesión</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
};

export default Login;
