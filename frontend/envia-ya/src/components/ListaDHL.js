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
    { name: "Rogelio Díaz", rating: 5, comment: "He solicitado un envío la semana pasada y me llegó a tiempo" },
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
          <p><strong>DHL</strong> es una empresa global de logística y mensajería que opera en más de 220 países y territorios. Fundada en 1969 por Adrian Dalsey, Larry Hillblom y Robert Lynn, sus siglas derivan de los apellidos de los fundadores. DHL comenzó ofreciendo servicios de mensajería aérea, un concepto innovador que revolucionó la logística al permitir la entrega rápida de documentos a nivel internacional.</p>
          <h3>Servicios Ofrecidos</h3>
          <ul>
            <li><strong>DHL Express:</strong> Especializado en envíos urgentes y entregas internacionales rápidas. Ofrece soluciones de transporte para documentos y paquetes con tiempos de entrega garantizados.</li>
            <li><strong>DHL Global Forwarding:</strong> Gestión de fletes aéreos, marítimos y terrestres. Proporciona soluciones de transporte para grandes volúmenes de carga, incluyendo la coordinación y el despacho aduanero.</li>
            <li><strong>DHL Freight:</strong> Transporte terrestre de cargas completas y parciales en toda Europa. Ofrece soluciones personalizadas para empresas que requieren transporte especializado.</li>
            <li><strong>DHL Supply Chain:</strong> Logística de contratación para empresas, que incluye gestión de almacenes, distribución y optimización de la cadena de suministro. Este servicio es fundamental para empresas que buscan externalizar partes críticas de su logística.</li>
            <li><strong>DHL eCommerce:</strong> Soluciones para el comercio electrónico, que incluyen la gestión de devoluciones, entregas a domicilio y opciones de entrega flexible.</li>
            <li><strong>DHL SameDay:</strong> Servicios de entrega urgente el mismo día, ideal para envíos críticos que no pueden esperar.</li>
          </ul>
          <h3>Infraestructura y Cobertura</h3>
          <p>DHL cuenta con una vasta infraestructura global que incluye más de 350,000 empleados y alrededor de 260 aviones dedicados exclusivamente a sus operaciones logísticas. Su red global le permite manejar una gran variedad de envíos, desde pequeños paquetes hasta cargas industriales.</p>
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
