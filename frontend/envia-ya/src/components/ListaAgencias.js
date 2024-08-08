import React, { useState } from 'react';
import './ListaAgencias.css';
import olvaImage from '../assets/olva1.png';

const ConocenosMas = ({ userName }) => {
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
    { name: "Luis Sanchez", rating: 4, comment: "Pude enviar de forma exitosa mi encomienda pero tardó un poco." },
    { name: "Sara Vega", rating: 5, comment: "Ya he hecho más de 15 envíos, y todos han llegado muy bien. Lo recomiendo al 100%." },
    { name: "Mario Torres", rating: 3, comment: "Excelente servicio." }
  ];

  const agencies = [
    {
      name: "OLVA COURIER - Cercado de Lima",
      address: "Avenida Garcilazo de la Vega 1358, Cercado de Lima",
      hours: "Horario de atención: 9:30am a 7pm - lunes a sábado."
    },
    {
      name: "OLVA COURIER - Rimac",
      address: "Las Tapadas 198, Rimac, Lima",
      hours: "Horario de atención: 9:30am a 7:30pm - lunes a sábado."
    },
    {
      name: "OLVA COURIER - La Victoria",
      address: "Jirón Antonio Bazo 1280, La Victoria, Lima",
      hours: "Horario de atención: 8:00am a 6:30pm - lunes a sábado."
    },
    {
      name: "OLVA COURIER - Miraflores",
      address: "Avenida Comande Espinar 659, Miraflores, Lima",
      hours: "Horario de atención: 8:00am a 7:00pm - lunes a sábado."
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={olvaImage} alt="Fachada de la empresa Olva Courier" className="company-photo" />
        <div className="company-details">
          <h2>Olva Courier</h2>
          <p>En OLVA, nos esforzamos por ofrecer un servicio de calidad que supere las expectativas de nuestros clientes. Trabajamos con actitudes positivas y vivimos nuestros valores en nuestro día a día.</p>
          <p>Olva Courier es una empresa peruana de logística y mensajería que ofrece una amplia gama de servicios para el envío de paquetes y documentos</p>
          <p>La sede principal de Olva Courier se encuentra en:</p>
          <p>Avenida Argentina 4458, Callao 07001, Perú</p>
          <p>Horario de Entrega de Envíos:</p>
          <ul>
            <li>Lunes a Viernes: 8:00 AM a 5:00 PM</li>
            <li>Sábados: 8:00 AM a 3:00 PM</li>
          </ul>
          <p>Sitio Web: <a href="https://www.olvacourier.com/" target="_blank" rel="noopener noreferrer">https://www.olvacourier.com/</a></p>
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
        <p>{userName ? "Deja tu comentario aquí" : "Solo si estás logueado"}</p>
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
          placeholder={`${
            userName ? `Escribe tu comentario aquí, ${userName}` : "Inicia sesión para comentar"
          }`}
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          disabled={!userName}
        />
        <button onClick={handleSubmit} disabled={!userName}>Enviar</button>
        <div className="example-comments">
          {exampleComments.map((c, index) => (
            <div key={index} className="example-comment">
              <div className="comment-header">
                <span className="comment-name">{c.name}</span>
                <div className="comment-rating">
                  {[...Array(5)].map((star, i) => (
                    <span key={i} className={i < c.rating ? "on" : "off"}>
                      &#9733;
                    </span>
                  ))}
                </div>
              </div>
              <div className="comment-text">{c.comment}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ConocenosMas;
