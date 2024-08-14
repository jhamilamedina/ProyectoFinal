import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './Perfil.css';

function Perfil({ userName, setUserName, setUserEmail, setFotoPerfil }) {
  const [nombre, setNombre] = useState('');
  const [usuario, setUsuario] = useState('');
  const [correo, setCorreo] = useState('');
  const [foto, setFoto] = useState('/ruta/imagen/default.jpg');
  const [isEditing, setIsEditing] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (userName) {
      setNombre(userName);
      const generatedUsername = `@${userName.split(' ').join('').toLowerCase()}`;
      setUsuario(generatedUsername);
      const generatedEmail = `${userName.split(' ').join('').toLowerCase()}@correo.com`;
      setCorreo(generatedEmail);
    }
  }, [userName]);

  const handlePhotoUpload = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onloadend = () => {
      setFoto(reader.result);
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  };

  const handleButtonClick = () => {
    navigate('/home');
  };

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const handleSaveClick = () => {
    setIsEditing(false);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name === 'nombre') {
      setNombre(value);
    } else if (name === 'usuario') {
      setUsuario(value);
    } else if (name === 'correo') {
      setCorreo(value);
    }
  };

  const handleDeleteAccount = () => {
    navigate('/eliminar-cuenta', {
      state: { nombre, usuario },
    });
  };

  return (
    <div className="perfil-container">
      <h1 className="perfil-header">Bienvenido {nombre.split(' ')[0]}</h1>
      <div className="perfil-content">
        <img src={foto} alt="Foto de perfil" className="perfil-foto" />
        <div className="perfil-info">
          <p>Usuario: {usuario}</p>
          <input type="file" accept="image/*" onChange={handlePhotoUpload} />
        </div>
      </div>
      <div className="perfil-enlaces">
        <a href="/datos" className="perfil-enlace">Mis datos</a>
        <p>
          Nombre: 
          {isEditing ? (
            <input
              type="text"
              name="nombre"
              value={nombre}
              onChange={handleInputChange}
            />
          ) : (
            <span>{nombre}</span>
          )}
          {isEditing ? (
            <button onClick={handleSaveClick}>Guardar</button>
          ) : (
            <button onClick={handleEditClick} className="perfil-enlace-button">Modificar</button>
          )}
        </p>
        <p>
          Usuario: 
          {isEditing ? (
            <input
              type="text"
              name="usuario"
              value={usuario}
              onChange={handleInputChange}
            />
          ) : (
            <span>{usuario}</span>
          )}
          {isEditing ? (
            <button onClick={handleSaveClick}>Guardar</button>
          ) : (
            <button onClick={handleEditClick} className="perfil-enlace-button">Modificar</button>
          )}
        </p>
        <p>
          Correo: 
          {isEditing ? (
            <input
              type="email"
              name="correo"
              value={correo}
              onChange={handleInputChange}
            />
          ) : (
            <span>{correo}</span>
          )}
          {isEditing ? (
            <button onClick={handleSaveClick}>Guardar</button>
          ) : (
            <button onClick={handleEditClick} className="perfil-enlace-button">Modificar</button>
          )}
        </p>
      </div>
      <div className="eliminar-cuenta-container">
        <button onClick={handleDeleteAccount} className="eliminar-cuenta-boton">
          Eliminar mi cuenta
        </button>
      </div>
      <div className="perfil-boton-container">
        <h2>¡Quiero buscar empresas de envío!</h2>
        <button onClick={handleButtonClick} className="perfil-boton">
          INGRESA AQUÍ
        </button>
      </div>
    </div>
  );
}

export default Perfil;
