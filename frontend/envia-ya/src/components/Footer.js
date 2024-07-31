import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer">
            <ul>
                <li><Link to=""></Link></li>
                <li><Link to="/Ayuda">Ayuda</Link></li>
                <li><Link to="/Privacidad">Pólitica de Privacidad</Link></li>
                <li><Link to=""></Link></li>
                </ul>
                <p>2024 Envía Ya. Todos los derechos reservados</p>
        </footer>
    );
};

export default Footer;