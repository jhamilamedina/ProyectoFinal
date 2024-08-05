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
          <p><strong>Servientrega</strong> es una empresa líder en el sector de mensajería y logística en América Latina. Ofrece una amplia gama de servicios que incluyen transporte y distribución de paquetería y documentos a nivel nacional e internacional.</p>
          <p>La compañía se destaca por su capacidad para proporcionar soluciones logísticas integrales, que abarcan desde el envío exprés de paquetes hasta la gestión completa de la cadena de suministro. Su red de operaciones se extiende por numerosos países en América Latina, con una presencia destacada en Colombia.</p>
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
