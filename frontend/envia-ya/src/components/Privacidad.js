import React from 'react';
import './Privacidad.css'; // Asegúrate de crear este archivo CSS

const PrivacyPolicy = () => {
    return (
        <div className="privacy-policy-container">
            <h1>Política de Privacidad</h1>

            <h2>¿Quién somos?</h2>
            <p>Envía Ya es una pagina web informativa donde se muestran distintas empresas dedicadas a los servicios de envío. Nos comprometemos a proteger la privacidad de 
              nuestros usuarios. Esta política explica cómo recopilamos, utilizamos y protegemos tu información personal cuando utilizas nuestro sitio web y servicios.</p>

            <h2>¿Qué información recopilamos?</h2>
            <ul>
                <li><strong>Información de contacto:</strong> Nombre, dirección de correo electrónico, número de teléfono y dirección física.</li>
                <li><strong>Información de pago:</strong> Datos de tu tarjeta de crédito o débito para procesar pagos.</li>
                <li><strong>Información de envío:</strong> Dirección de envío y detalles del paquete.</li>
            </ul>

            <h2>¿Cómo utilizamos tu información?</h2>
            <ul>
                <li><strong>Procesar tus pedidos:</strong> Utilizaremos tu información para procesar tus pedidos de envío y mantenerte informado sobre el estado de los mismos.</li>
                <li><strong>Comunicación:</strong> Te enviaremos correos electrónicos con actualizaciones sobre tu pedido, noticias de la empresa y ofertas especiales. Puedes optar por no recibir estos correos en cualquier momento.</li>
                <li><strong>Mejorar nuestros servicios:</strong> Analizamos tu información para mejorar nuestros servicios y ofrecerte una mejor experiencia de usuario.</li>
            </ul>

            <h2>¿Cómo protegemos tu información?</h2>
            <p>Implementamos medidas de seguridad técnicas y organizativas para proteger tu información personal de pérdidas, acceso no autorizado, divulgación, alteración o destrucción.</p>

            <h2>¿Con quién compartimos tu información?</h2>
            <p>No vendemos, alquilamos ni compartimos tu información personal con terceros, excepto en los siguientes casos:</p>
            <ul>
                <li><strong>Proveedores de servicios:</strong> Podemos compartir tu información con terceros que nos ayudan a prestar nuestros servicios (por ejemplo, empresas de transporte).</li>
                <li><strong>Cumplimiento legal:</strong> Podemos divulgar tu información si lo exige la ley o para proteger nuestros derechos.</li>
            </ul>

            <h2>Tus derechos</h2>
            <p>Tienes derecho a:</p>
            <ul>
                <li><strong>Acceder a tu información:</strong> Puedes solicitar una copia de la información que tenemos sobre ti.</li>
                <li><strong>Corregir tu información:</strong> Si la información que tenemos sobre ti es incorrecta, puedes solicitar que la corrijamos.</li>
                <li><strong>Eliminar tu información:</strong> Puedes solicitar que eliminemos tu información de nuestra base de datos.</li>
            </ul>

            <h2>Cambios en esta política</h2>
            <p>Podemos actualizar esta política de privacidad ocasionalmente. Te notificaremos sobre cualquier cambio importante.</p>

            <h2>Contacto</h2>
            <p>Si tienes alguna pregunta sobre esta política de privacidad, puedes contactarnos a través de [dirección de correo electrónico] o [número de teléfono].</p>
        </div>
    );
};

export default PrivacyPolicy;
