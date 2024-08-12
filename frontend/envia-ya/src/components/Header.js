import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';
import logo from '../assets/logo.jpeg';

const Header = ({ userName, userEmail }) => {
  const [showDropdown, setShowDropdown] = useState(false);
  const navigate = useNavigate();

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  const handleViewProfile = () => {
    navigate('/perfil'); // No es necesario pasar userName y userEmail si ya se cargan desde localStorage
  };

  const handleLogout = () => {
    // Limpiar datos del perfil en localStorage
    localStorage.removeItem('nombre');
    localStorage.removeItem('usuario');
    localStorage.removeItem('correo');
    localStorage.removeItem('foto');

    // Redirigir a la página de inicio
    navigate('/home'); // Cambia la ruta según tus necesidades
  };

  return (
    <header className='header'>
      <div className='logo-slogan'>
        <img src={logo} alt='Envía Ya logo' className='logo' />
        <h1>Envía Ya</h1>
      </div>
      <nav>
        <ul className='nav-links'>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/destinos">Destinos</Link></li>
          <li><Link to="/empresas">Empresas</Link></li>
          <li><Link to="/nosotros">Nosotros</Link></li>
          <li><Link to="/Inicio">Inicio de Sesión</Link></li>
        </ul>
      </nav>
      {userName && (
        <div className="user-section" onClick={toggleDropdown}>
          Hola, {userName}
          {showDropdown && (
            <div className="user-dropdown">
              <div className="dropdown-item" onClick={handleViewProfile}>Ver Perfil</div>
              <div className="dropdown-item" onClick={handleLogout}>Cerrar Sesión</div>
            </div>
          )}
        </div>
      )}
    </header>
  );
};

export default Header;
