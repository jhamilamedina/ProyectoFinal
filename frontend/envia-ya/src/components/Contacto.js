import React, { useState } from 'react';
import './Contacto.css';
import { Link } from 'react-router-dom';

const App = () => {
  const initialFormData = {
    nombres: '',
    email: '',
    celular: '',
    distrito: '',
    mensaje: '',
    aceptoPolitica: false
  };

  const [formData, setFormData] = useState(initialFormData);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { nombres, email, celular, distrito, mensaje, aceptoPolitica } = formData;

    if (!nombres || !email || !celular || !distrito || !mensaje) {
      alert('Te falta llenar todos los campos.');
      return;
    }

    if (!aceptoPolitica) {
      alert('Debes aceptar la política de privacidad.');
      return;
    }

    alert('Datos enviados correctamente');
    console.log('Formulario enviado:', formData);

    // Resetear el formulario
    setFormData(initialFormData);
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
