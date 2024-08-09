import React, { useState } from 'react';
import './ListaUps.css';
import UpsImage from '../assets/Ups.jpg';

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
      name: "UPS - San Luis",
      address: "Avenida Javier Prado Este 1500, San Luis, Lima",
      hours: "Horario de atención: 7:30am a 6:30pm - lunes a sábado"
    },
    {
      name: "UPS - Cercado de Lima",
      address: "Jirón Huallaga 288, Cercado de Lima, Lima",
      hours: "Horario de atención: 10:00am a 7:30pm - lunes a sábado"
    },
    {
      name: "UPS - Rimac",
      address: "Jirón Santa Cecilia 1502, Rimac, Lima",
      hours: "Horario de atención: 9:30am a 5:30pm - lunes a sábado"
    },
    {
      name: "UPS - La Victoria",
      address: "Avenida Elmer Faucett 158, La Victoria, Lima",
      hours: "Horario de atención: 7:00am a 5:00pm - lunes a sábado"
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={UpsImage} alt="Fachada de UPS" className="company-photo" />
        <div className="company-details">
          <h2>UPS</h2>
          <p><strong>UPS</strong> (United Parcel Service) es una empresa global de logística y mensajería conocida por sus servicios de transporte y distribución. Fundada en 1907 como American Messenger Company y rebautizada como United Parcel Service en 1919, UPS comenzó con una flota de bicicletas y motocicletas antes de expandir su red para incluir camiones y aviones.</p>
          <h3>Servicios</h3>
          <ul>
            <li><strong>UPS Ground:</strong> Servicios de entrega terrestre que abarcan los EE.UU., Canadá, y México, con tiempos de entrega basados en la distancia y el tipo de servicio seleccionado.</li>
            <li><strong>UPS Air:</strong> Ofrece servicios de entrega urgente y programada a nivel nacional e internacional. Incluye opciones de entrega en un día, dos días y otros plazos.</li>
            <li><strong>UPS Freight:</strong> Proporciona servicios de carga de mercancías pesadas y menos que carga (LTL), con cobertura en EE.UU., Canadá y México.</li>
            <li><strong>UPS Supply Chain Solutions:</strong> Ofrece servicios integrales de gestión de la cadena de suministro, que incluyen logística, gestión de inventarios, distribución y soluciones de cadena de suministro personalizadas.</li>
            <li><strong>UPS Store:</strong> Red de franquicias que proporciona servicios de impresión, envío de paquetes y soluciones de oficina a nivel nacional.</li>
            <li><strong>UPS Capital:</strong> Servicios financieros y seguros, incluyendo protección de paquetes y soluciones de financiamiento.</li>
          </ul>
          <h3>Operaciones</h3>
          <ul>
            <li><strong>Red Global:</strong> UPS opera en más de 220 países y territorios, con una red extensa que abarca entregas internacionales y nacionales.</li>
            <li><strong>Hub Principal:</strong> El hub más importante de UPS es el Worldport en Louisville, Kentucky, que es uno de los centros de clasificación de paquetes más grandes del mundo.</li>
          </ul>
         
          <h3>Sede Principal</h3>
          <p><strong>Dirección:</strong> Av. Víctor Andrés Belaúnde 147, Oficina 701, Edificio Center Tower,
          San Isidro, Lima 27, Perú</p>
          <h3>Horario de Atención</h3>
          <ul>
            <li><strong>Lunes a Viernes:</strong> 8:00 AM - 6:00 PM</li>
            <li><strong>Sábados:</strong> 9:00 AM - 1:00 PM</li>
            <li><strong>Domingos y festivos:</strong> Cerrado</li>
          </ul>
          <p><strong>Sitio Web:</strong> <a href="https://www.ups.com" target="_blank" rel="noopener noreferrer">https://www.ups.com</a></p>
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
