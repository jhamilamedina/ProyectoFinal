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
          <p><strong>FedEx</strong>, o Federal Express, es una empresa multinacional de logística y servicios de mensajería con sede en Memphis, Tennessee, Estados Unidos. Fundada en 1971, FedEx comenzó sus operaciones en 1973 bajo el nombre original de Federal Express.</p>
          <h3>Servicios</h3>
          <ul>
            <li><strong>FedEx Express:</strong> Servicios de mensajería y entrega exprés a nivel global.</li>
            <li><strong>FedEx Ground:</strong> Entregas terrestres económicas en los EE.UU. y Canadá.</li>
            <li><strong>FedEx Freight:</strong> Servicios de carga y transporte de mercancías pesadas.</li>
            <li><strong>FedEx Office:</strong> Servicios de impresión y oficina, anteriormente conocido como Kinko's.</li>
            <li><strong>FedEx Supply Chain:</strong> Soluciones de cadena de suministro y logística.</li>
          </ul>
          <h3>Operaciones</h3>
          <p>FedEx opera en más de 220 países y territorios, con una de las flotas aéreas más grandes del mundo, que cuenta con más de 600 aviones. Su hub principal es el aeropuerto de Memphis (MEM), conocido como el "Superhub".</p>
          <h3>Sede Principal</h3>
          <p><strong>Dirección:</strong> Av. Tomás Valle 313, Independencia, Lima 15314, Perú</p>
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
