import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';
import logo from '../assets/logo.jpeg'
const Header = () => {
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
		</header>
	);
};

export default Header;
