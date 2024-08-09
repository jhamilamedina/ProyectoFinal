import React, { useState } from 'react';
import './ListaServientrega.css';
import servientregaImage from '../assets/servientrega.png';

const ConocenosMas = () => {
  const [rating, setRating] = useState(0);
  const [hover, setHover] = useState(0);
  const [comment, setComment] = useState("");

  const handleRating = (rate) => {
    setRating(rate);
  };

  const handleSubmit = () => {
    if (comment.trim()) {
      alert(`Rating: ${rating}\nComment: ${comment}`);
      setComment("");
    } else {
      alert("Por favor deja tu comentario");
    }
  };

  const exampleComments = [
    { name: "Maria Gonzales", rating: 4, comment: "Muy buena la atención" },
    { name: "Rogelio Díaz", rating: 5, comment: "He solicitado un envío la semana pasada y me llegó a tiempo" },
    { name: "Rosa Vazques", rating: 3, comment: "Buen servicio" }
  ];

  const agencies = [
    {
      name: "Servientrega - Breña",
      address: "Avenida Argentina 515, Breña, Lima",
      hours: "Horario de atención: 8:30am a 6:30pm - lunes a sábado"
    },
    {
      name: "Servientrega - Miraflores",
      address: "Avenida Javier Prado, Miraflores, Lima",
      hours: "Horario de atención: 8:30am a 6:30pm - lunes a sábado"
    },
    {
      name: "Servientrega - San Luis",
      address: "Avenida Agustín de la Rosa Toro 490, San Luis, Lima",
      hours: "Horario de atención: 9:00am a 7:00pm - lunes a sábado"
    },
    {
      name: "Servientrega - Cercado de Lima",
      address: "Jirón de la Torre Ugarte 155, Cercado de Lima, Lima",
      hours: "Horario de atención: 8:30am a 7:00pm - lunes a sábado"
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={servientregaImage} alt="Fachada de Servientrega" className="company-photo" />
        <div className="company-details">
          <h2>Servientrega</h2>
          <p><strong>Servientrega</strong> es una empresa colombiana de mensajería y logística, fundada en 1982. Con una amplia experiencia en el sector, Servientrega se especializa en la prestación de servicios de envío y logística a nivel nacional e internacional. La compañía ha crecido considerablemente y se ha posicionado como uno de los líderes en el mercado de mensajería en América Latina.</p>
          <h3>Servicios Ofrecidos</h3>
          <ul>
            <li><strong>Envíos Nacionales:</strong> Servicios de mensajería y paquetería a nivel nacional en Colombia, con opciones de entrega express y estándar. Servicios de logística para grandes volúmenes y cargas especiales.</li>
            <li><strong>Envíos Internacionales:</strong> Soluciones de mensajería y logística para envíos internacionales. Coordinación con operadores globales para garantizar tiempos de entrega eficientes y seguros.</li>
            <li><strong>Logística Integral:</strong> Gestión de cadena de suministro que incluye almacenamiento, distribución y optimización de procesos logísticos. Servicios personalizados para empresas, adaptados a sus necesidades específicas.</li>
            <li><strong>Envíos Internacionales de Paquetes y Documentos:</strong> Envíos rápidos y seguros de paquetes y documentos a nivel mundial. Soluciones para comercio electrónico y devoluciones internacionales.</li>
            <li><strong>Servicio de Mensajería Express:</strong> Entregas urgentes y rápidas para paquetes y documentos. Opciones de seguimiento en tiempo real y servicios de entrega en el mismo día.</li>
          </ul>
          <h3>Infraestructura y Cobertura</h3>
          <p>Servientrega cuenta con una extensa red de sucursales y puntos de atención en Colombia, así como una red de agentes y operadores internacionales. La empresa tiene presencia en varios países de América Latina, facilitando envíos internacionales y operaciones logísticas regionales.</p>
          <h3>Sede Principal</h3>
          <p><strong>Dirección:</strong> Carrera 72 # 25-22, Bogotá, Colombia</p>
          <h3>Horario de Atención</h3>
          <ul>
            <li><strong>Lunes a Viernes:</strong> 8:00 AM - 6:00 PM</li>
            <li><strong>Sábados:</strong> 9:00 AM - 1:00 PM</li>
            <li><strong>Domingos y festivos:</strong> Cerrado</li>
          </ul>
          <p><strong>Sitio Web:</strong> <a href="https://www.servientrega.com/" target="_blank" rel="noopener noreferrer">https://www.servientrega.com/</a></p>
        </div>
      </div>
      <div className="agencies">
        <h2>Conoce algunas de nuestras Agencias</h2>
        <ul>
          {agencies.map((agency, index) => (
            <li key={index}>
              <div className="agency-details">
                <span className="agency-name">{agency.name}</span>
                <div className="agency-address">{agency.address}</div>
                <div className="agency-hours">{agency.hours}</div>
              </div>
            </li>
          ))}
        </ul>
      </div>
      <div className="comments-section">
        <h2>Comentarios</h2>
        <p>Deja tu comentario (solo si estás logueado)</p>
        <div className="rating">
          {[...Array(5)].map((star, index) => {
            index += 1;
            return (
              <button
                type="button"
                key={index}
                className={index <= (hover || rating) ? "on" : "off"}
                onClick={() => handleRating(index)}
                onMouseEnter={() => setHover(index)}
                onMouseLeave={() => setHover(rating)}
              >
                <span className="star">&#9733;</span>
              </button>
            );
          })}
        </div>
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="solo si estás logueado"
          className="comment-box"
        />
        <button onClick={handleSubmit} className="submit-button">Enviar</button>

        {/* Comentarios de ejemplo */}
        <div className="example-comments">
          {exampleComments.map((example, index) => (
            <div key={index} className="comment">
              <strong>{example.name}</strong>
              <div className="rating">
                {[...Array(5)].map((star, i) => (
                  <span key={i} className={`star ${i < example.rating ? 'on' : 'off'}`}>&#9733;</span>
                ))}
              </div>
              <p>{example.comment}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ConocenosMas;
