import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import './EliminoCuenta.css';

function EliminarCuenta({ setUserName, setUserEmail, setFotoPerfil }) {
  const navigate = useNavigate();
  const location = useLocation();
  const { nombre, usuario } = location.state || { nombre: '', usuario: '' };

  const handleDelete = () => {
    // Borra todos los datos del perfil
    setUserName('');
    setUserEmail('');
    setFotoPerfil('/ruta/imagen/default.jpg');

    // Opcional: Limpia cualquier almacenamiento local
    localStorage.clear(); // Limpia localStorage
    sessionStorage.clear(); // Limpia sessionStorage si es necesario

    // Redirige a la página de inicio o login
    navigate('/inicio');
  };

  const handleCancel = () => {
    alert('Tu cuenta aún está activa.'); // Muestra una alerta
    navigate('/perfil'); // Redirige al perfil
  };

  return (
    <div className="eliminar-cuenta-container">
      <h1>Bienvenido {nombre}</h1>
      <p>¿Estás seguro que deseas eliminar de manera definitiva tu cuenta?</p>
      <p>Usuario: {usuario}</p>
      <div className="eliminar-cuenta-botones">
        <button onClick={handleDelete} className="eliminar-cuenta-boton si">
          Sí
        </button>
        <button onClick={handleCancel} className="eliminar-cuenta-boton no">
          No
        </button>
      </div>
    </div>
  );
}

export default EliminarCuenta;
