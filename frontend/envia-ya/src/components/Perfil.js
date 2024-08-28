import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Perfil = () => {
  const [usuario, setUsuario] = useState(null);
  const [mensaje, setMensaje] = useState('');
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');
  const [foto, setFoto] = useState('');
  const navigate = useNavigate();
  const userId = JSON.parse(localStorage.getItem('user'))?.id; // Obtén el ID del usuario desde localStorage

  useEffect(() => {
    if (userId) {
      axios.get(`http://localhost:8000/api/usuarios/${userId}/`)
        .then(response => {
          setUsuario(response.data.Usuario);
        })
        .catch(error => {
          setMensaje('Error al cargar el perfil');
          console.error('Error al cargar el perfil:', error);
        });
    } else {
      setMensaje('ID de usuario no proporcionado');
    }
  }, [userId]);

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
    <div>
      <h2>Perfil de Usuario</h2>
      {usuario ? (
        <div>
          <p><strong>Nombre:</strong> {usuario.nombre}</p>
          <p><strong>Email:</strong> {usuario.email}</p>
          <img src={`http://localhost:8000/${usuario.foto_usuario}`} alt="Foto de perfil" style={{ width: '100px', height: '100px' }} />
          <div>
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
            <button onClick={handleUpdate}>Actualizar Perfil</button>
          </div>
          {mensaje && <p>{mensaje}</p>}
        </div>
      ) : (
        <p>{mensaje || 'Cargando...'}</p>
      )}
    </div>
  );
};

export default Perfil;
