import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Perfil.css'; // Asegúrate de importar los estilos

const Perfil = () => {
  const [usuario, setUsuario] = useState(null);
  const [mensaje, setMensaje] = useState('');
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');
  const [foto, setFoto] = useState(null);
  const navigate = useNavigate();
  const userId = JSON.parse(localStorage.getItem('user'))?.id;

  useEffect(() => {
    if (userId) {
      axios.get(`http://localhost:8000/api/usuarios/${userId}/`)
        .then(response => {
          setUsuario(response.data.Usuario);
          setNombre(response.data.Usuario.nombre);
          setEmail(response.data.Usuario.email);
        })
        .catch(error => {
          setMensaje('Error al cargar el perfil');
          console.error('Error al cargar el perfil:', error);
        });
    } else {
      setMensaje('ID de usuario no proporcionado');
      navigate('/login');
    }
  }, [userId, navigate]);

  const handleFotoChange = (event) => {
    setFoto(event.target.files[0]);
  };

  const handleUpdate = () => {
    if (userId) {
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('email', email);
      if (foto) formData.append('foto_usuario', foto);

      axios.put(`http://localhost:8000/api/usuarios/${userId}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(response => {
        setUsuario(response.data.data);
        setMensaje('Perfil actualizado con éxito');
      })
      .catch(error => {
        setMensaje('Error al actualizar el perfil');
        console.error('Error al actualizar el perfil:', error);
      });
    }
  };

  return (
    <div className="perfil-container">
      <h2>Perfil de Usuario</h2>
      {usuario ? (
        <div className="perfil-info">
          <p><strong>Nombre:</strong> {usuario.nombre}</p>
          <p><strong>Email:</strong> {usuario.email}</p>
          <img src={`http://localhost:8000/${usuario.foto_usuario}`} alt="Foto de perfil" style={{ width: '100px', height: '100px' }} />
          <div className="input-group">
            <input 
              type="text" 
              value={nombre} 
              onChange={(e) => setNombre(e.target.value)} 
              placeholder="Nuevo nombre"
            />
            <input 
              type="email" 
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              placeholder="Nuevo email"
            />
            <input type="file" onChange={handleFotoChange} />
            <button className="button-update" onClick={handleUpdate}>Actualizar Perfil</button>
          </div>
          {mensaje && <p className="mensaje">{mensaje}</p>}
        </div>
      ) : (
        <p className="mensaje">{mensaje || 'Cargando...'}</p>
      )}
    </div>
  );
};

export default Perfil;
