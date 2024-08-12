import React, { useState } from 'react';
import './Inicio.css';

const Inicio = ({ setUserName, setUserEmail }) => {
  const [formData, setFormData] = useState({
    nombres: '',
    email: '',
    contraseña: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    // Genera automáticamente un correo basado en el nombre
    if (name === 'nombres') {
      const generatedEmail = value.toLowerCase().replace(/\s+/g, '') + '@correo.com';
      setFormData((prevData) => ({ ...prevData, email: generatedEmail }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setUserName(formData.nombres);
    setUserEmail(formData.email);
    console.log('Formulario enviado:', formData);
    alert('Cuenta creada correctamente');
    // Resetear el formulario
    setFormData({
      nombres: '',
      email: '',
      contraseña: ''
    });
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
          <label htmlFor="email">Email:</label>
          <input 
            type="email" 
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
};

export default Inicio;
