import React, { useState } from 'react';
import './Contacto.css';
import { Link } from 'react-router-dom';

const App = () => {
  const [formData, setFormData] = useState({
    nombres: '',
    empresa: '',
    email: '',
    celular: '',
    distrito: '',
    mensaje: '',
    aceptoPolitica: false // Estado para el checkbox
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.aceptoPolitica) {
      alert('Debes aceptar la política de privacidad.');
      return;
    }
    console.log('Formulario enviado:', formData);
    // Aquí puedes agregar la lógica para enviar el formulario
  };

  return (
    <div className="form-container">
      <h2>Formulario de Contacto</h2>
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
          <label htmlFor="empresa">Empresa:</label>
          <input 
            type="text" 
            id="empresa" 
            name="empresa" 
            value={formData.empresa} 
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
          <label htmlFor="celular">Nro Celular:</label>
          <input 
            type="text" 
            id="celular" 
            name="celular" 
            value={formData.celular} 
            onChange={handleChange} 
            required 
          />
        </div>
        <div className="form-group">
          <label htmlFor="distrito">Distrito:</label>
          <input 
            type="text" 
            id="distrito" 
            name="distrito" 
            value={formData.distrito} 
            onChange={handleChange} 
            required 
          />
        </div>
        <div className="form-group">
          <label htmlFor="mensaje">Mensaje:</label>
          <textarea 
            id="mensaje" 
            name="mensaje" 
            value={formData.mensaje} 
            onChange={handleChange} 
            rows="4" 
            required 
          />
        </div>
        <div className="form-group">
          <label>
            <input 
              type="checkbox" 
              name="aceptoPolitica" 
              checked={formData.aceptoPolitica} 
              onChange={handleChange} 
              required 
            />
            He leído y acepto la <Link to="/Privacidad">política de privacidad</Link>
          </label>
        </div>
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}

export default App;
