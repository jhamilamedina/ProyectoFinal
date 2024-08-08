import React, { useState } from 'react';
import './ListaDHL.css';
import DHLImage from '../assets/DHL.jpg';

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
    { name: "Rogelio Díaz", rating: 5, comment: "He solicitado un envio la semana pasada y me llego a tiempo" },
    { name: "Rosa Vazques", rating: 3, comment: "Buen servicio" }
  ];

  const agencies = [
    {
      name: "Shalom - La Victoria",
      address: "Jirón Antonio Bazo 613, La Victoria, Lima",
      hours: "Horario de atención: 9:00am a 6:30pm - lunes a sábado"
    },
    {
      name: "Shalom - Breña",
      address: "Jirón Huaraz 1592, Breña, Lima",
      hours: "Horario de atención: 8:30am a 6:30pm - lunes a sábado"
    },
    {
      name: "Shalom - Miraflores",
      address: "Avenida Alfredo Benavides 708, Miraflores, Lima",
      hours: "Horario de atención: 9:00am a 7:00pm - lunes a sábado"
    },
    {
      name: "Shalom - San Luis",
      address: "Avenida San Luis 2211, San Luis",
      hours: "Horario de atención: 9:00am a 6:30pm - lunes a sábado"
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={DHLImage} alt="Fachada de DHL" className="company-photo" />
        <div className="company-details">
          <h2>DHL</h2>
          <p><strong>DHL</strong> es una empresa global de logística y mensajería que se dedica al transporte rápido y seguro de paquetes y documentos a nivel mundial. Ofrece una amplia gama de servicios, incluyendo envíos exprés internacionales, transporte terrestre, marítimo y aéreo, así como soluciones de cadena de suministro y logística para empresas. Con operaciones en más de 220 países y territorios, DHL es una de las compañías líderes en el sector, facilitando el comercio y la conectividad global.</p>
          <h3>Sede Principal</h3>
          <p><strong>DHL International GmbH</strong><br />
            Apartado de correos 100 239 - 53145 Bonn<br />
            Alemania</p>
          <h3>Horario de Atención</h3>
          <ul>
            <li><strong>Lunes a Viernes:</strong> 9:00 AM a 5:00 PM</li>
          </ul>
          <p><strong>Sitio Web:</strong> <a href="https://www.dhl.com/pe-es/home.html" target="_blank" rel="noopener noreferrer">https://www.dhl.com/pe-es/home.html</a></p>
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
          placeholder="solo si estas logueado"
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
