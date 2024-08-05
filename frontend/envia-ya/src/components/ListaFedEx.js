import React, { useState } from 'react';
import './ListaFedEx.css';
import FedExImage from '../assets/FedEx.jpeg';

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
      name: "FedEx - Miraflores",
      address: "Calle Alcanfores 350, Miraflores, Lima",
      hours: "Horario de atención: 8:30am a 7:30pm - lunes a sábado"
    },
    {
      name: "FedEx - San Luis",
      address: "Avenida Ricardo Basilio 1382, San Luis, Lima",
      hours: "Horario de atención: 9:00am a 6:00pm - lunes a sábado"
    },
    {
      name: "FedEx - Cercado de Lima",
      address: "Calle Los Cedros 350, Cercado de Lima, Lima",
      hours: "Horario de atención: 8:30am a 6:30pm - lunes a sábado"
    },
    {
      name: "FedEx - Rimac",
      address: "Calle Lomas de Almancaes 548, Rimac, Lima",
      hours: "Horario de atención: 7:00am a 6:00pm - lunes a sábado"
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={FedExImage} alt="Fachada de FedEx" className="company-photo" />
        <div className="company-details">
          <h2>FedEx</h2>
          <p><strong>FedEx</strong> es una empresa global de logística y mensajería conocida por su servicio de entrega rápida y eficiente. Ofrece soluciones de transporte terrestre, aéreo y marítimo, así como servicios de logística y cadena de suministro en todo el mundo.</p>
          <h3>Sede Principal</h3>
          <p><strong>Dirección:</strong> 3875 Airways Blvd, Memphis, TN 38116, Estados Unidos</p>
          <h3>Horario de Atención</h3>
          <ul>
            <li><strong>Lunes a Viernes:</strong> 8:00 AM - 6:00 PM</li>
            <li><strong>Sábados:</strong> 9:00 AM - 1:00 PM</li>
            <li><strong>Domingos y festivos:</strong> Cerrado</li>
          </ul>
          <p><strong>Sitio Web:</strong> <a href="https://www.fedex.com" target="_blank" rel="noopener noreferrer">https://www.fedex.com</a></p>
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
