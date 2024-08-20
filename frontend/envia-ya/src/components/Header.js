import React, { useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import './Header.css';
import logo from '../assets/logo.jpeg';

const Header = () => {
  const [showDropdown, setShowDropdown] = useState(false);
  const { user, logout } = useContext(AuthContext); // Obtén el usuario del contexto
  const navigate = useNavigate();

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  const handleViewProfile = () => {
    navigate('/perfil');
  };

  const handleLogout = () => {
    logout(); // Llama la función de logout del contexto
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
          <li><Link to="/registro">Inicio / Registro</Link></li>
        </ul>
      </nav>
      {user && (
        <div className="user-section" onClick={toggleDropdown}>
          Hola, {user.nombre} {/* Muestra el nombre del usuario */}
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
