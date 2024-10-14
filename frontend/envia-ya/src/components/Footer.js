import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer__container">
                <div className="footer__col">
                    <h4>Envía ya</h4>
                    <p>
                        En Envía ya podrás encontrar información centralizada
                        completamente gratis las 24 horas del día y los 365 
                        días del año.
                    </p>
                    <div className="footer__socials">
                        <a href=""><i className="ri-facebook-circle-fill"></i></a>
                        <a href=""><i className="ri-instagram-line"></i></a>
                        <a href=""><i className="ri-twitter-fill"></i></a>
                    </div>
                </div>
                <div className="footer__col">
                    <h4>Información</h4>
                    <Link to="/inicio">Inicio</Link>
                    <Link to="/nosotros">Nosotros</Link>
                    <Link to="/empresas">Empresas</Link>
                    <Link to="/ayuda">Ayuda</Link>
                </div>
                <div className="footer__col">
                    <h4>Recursos</h4>
                    <Link to="/privacidad">Políticas de Privacidad</Link>
                </div>
                <div className="footer__col">
                    <h4>Contacto</h4>
                    <a href="mailto:enviaya@gmail.com">
                        <i className="ri-mail-line"></i> enviaya@gmail.com
                    </a>
                    <a href="tel:9876543210">
                        <i className="ri-phone-line"></i> 9876543210
                    </a>
                </div>
            </div>
            <div className="footer__bar">
                Copyright © 2024 Envía ya - Todos los derechos reservados.
            </div>
        </footer>
    );
};

export default Footer;
