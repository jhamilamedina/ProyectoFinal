import React, { useState } from 'react';
import './ListaUrbano.css';
import UrbanoImage from '../assets/Urbano.jpg';

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
      name: "Urbano - Cercado de Lima",
      address: "Avenida Materiales 3049, Cercado de Lima, Lima",
      hours: "Horario de atención: 9:00am a 6:30pm"
    },
    {
      name: "Urbano - Rimac",
      address: "Calle San German 205, Rimac, Lima",
      hours: "Horario de atención: 9:00am a 6:30pm"
    },
    {
      name: "Urbano - La Victoria",
      address: "Jirón Lucanas 671, La Victoria, Lima",
      hours: "Horario de atención: 9:00am a 6:30pm"
    },
    {
      name: "UPS - Breña",
      address: "Avenida Arica 150, Breña",
      hours: "Horario de atención: 9:00am a 7:00pm"
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={UrbanoImage} alt="Fachada de Urbano" className="company-photo" />
        <div className="company-details">
          <h2>Urbano</h2>
          <p><strong>Urbano</strong> es una empresa dedicada a ofrecer soluciones integrales de transporte y logística, con un enfoque en mejorar la eficiencia y cobertura en áreas urbanas y rurales.</p>
          <ul>
            <li>Fundada para ofrecer soluciones de transporte y logística, con un enfoque en mejorar la eficiencia y la cobertura en áreas urbanas y rurales.</li>
            <li>La empresa ha crecido para abarcar una red amplia de agencias y servicios, adaptándose a las necesidades cambiantes del mercado.</li>
          </ul>
          <h3>Servicios</h3>
          <ul>
            <li><strong>Transporte de Mercancías:</strong> Ofrece servicios de transporte para paquetes y encomiendas, con opciones para envíos urgentes y estándar.</li>
            <li><strong>Logística:</strong> Proporciona soluciones logísticas integrales que incluyen gestión de inventarios, distribución y cadena de suministro.</li>
            <li><strong>Red de Agencias:</strong> Cuenta con una red de agencias en varias localidades para facilitar la entrega y recepción de mercancías.</li>
          </ul>
          <h3>Sede Principal</h3>
          <p><strong>Dirección:</strong> Av. Elmer Faucett 1234, Callao, Lima, Perú</p>
          <h3>Horario de Atención</h3>
          <ul>
            <li><strong>Lunes a Viernes:</strong> 8:00 AM - 6:00 PM</li>
            <li><strong>Sábados:</strong> 9:00 AM - 1:00 PM</li>
            <li><strong>Domingos y festivos:</strong> Cerrado</li>
          </ul>
          <p><strong>Sitio Web:</strong> <a href="https://www.urbano.com" target="_blank" rel="noopener noreferrer">https://www.urbano.com</a></p>
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
                  <span key={i} className={i < example.rating ? 'star on' : 'star off'}>&#9733;</span>
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
