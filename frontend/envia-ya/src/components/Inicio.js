import React, { useState } from 'react';
import './Inicio.css';

const App = () => {
  const [formData, setFormData] = useState({
    nombres: '',
    apellidos: '',
    contraseña: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Formulario enviado:', formData);
    
  };

  return (
    <div className="form-container">
      <h1>Crear Cuenta</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="nombres">Nombres:</label>
          <input 
            type="text" 
            id="nombres" 
            name="nombres" 
            value={formData.nombres} 
            onChange={handleChange} 
            required 
          />
        </div>
        <div className="form-group">
          <label htmlFor="apellidos">Email:</label>
          <input 
            type="text" 
            id="email" 
            name="email" 
            value={formData.email} 
            onChange={handleChange} 
            required 
          />
        </div>
        <div className="form-group">
          <label htmlFor="contraseña">Contraseña:</label>
          <input 
            type="password" 
            id="contraseña" 
            name="contraseña" 
            value={formData.contraseña} 
            onChange={handleChange} 
            required 
          />
        </div>
        <button type="submit">Crear Cuenta</button>
      </form>
    </div>
  );
}

export default App;
