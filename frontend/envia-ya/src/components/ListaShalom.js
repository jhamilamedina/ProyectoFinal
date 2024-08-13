import React, { useState } from 'react';
import './ListaShalom.css';
import shalomImage from '../assets/shalom.png';

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
      name: "Shalom - Rimac",
      address: "Avenida Amancaes 644, Rimac, Lima",
      hours: "Horario de atención: 8:30am a 7:00pm - lunes a sábado."
    },
    {
      name: "Shalom - La Victoria",
      address: "Jirón Luna Pizarro, La Victoria, Lima",
      hours: "Horario de atención: 7:00am a 5:30pm - lunes a sábado."
    },
    {
      name: "Shalom - Breña",
      address: "Avenida República de Venezuela 1670, Breña, Lima",
      hours: "Horario de atención: 9:00am a 7:00pm - lunes a sábado."
    },
    {
      name: "Shalom - Miraflores",
      address: "Avenida José Pardo 533, Miraflores, Lima",
      hours: "Horario de atención: 8:00am a 6:30pm - lunes a sábado."
    }
  ];

  return (
    <div className="conocenos-mas">
      <div className="company-info">
        <img src={shalomImage} alt="Fachada de la empresa Shalom" className="company-photo" />
        <div className="company-details">
          <h2>Shalom</h2>
          <p><strong>Shalom Transportes y Encomiendas</strong> es una empresa peruana especializada en el envío de paquetes y mercancías a nivel nacional.</p>

          <p>Shalom nació en Lima, Perú, con la misión de proporcionar un servicio de transporte seguro, eficiente y accesible. Con el tiempo, la empresa ha crecido exponencialmente, ampliando su cobertura a lo largo y ancho del país, así como estableciendo alianzas estratégicas que le permiten operar en el ámbito internacional.</p>
          
          <h3>Servicios Ofrecidos</h3>
          <ul>
            <li><strong>Envíos Nacionales:</strong> Paquetes y Documentos, Encomiendas Especiales.</li>
            <li><strong>Transporte de Carga Pesada:</strong> Transporte de maquinaria industrial, vehículos y equipos especializados.</li>
            <li><strong>Logística Integral para Empresas:</strong> Gestión de Inventarios, Distribución y Almacenamiento.</li>
            <li><strong>Servicios Internacionales:</strong> Envíos internacionales, gestión aduanera, y seguimiento en tiempo real.</li>
          </ul>
          <h3>La sede principal de Shalom se encuentra en:</h3>
          <p>Carretera Central Km. 16.5, Lt. 5 Paradero, al costado del grifo Repsol, Ent A Huaycán, Ate, Lima 15476, Perú.</p>
          
          <h3>Horario de Atención:</h3>
          <ul>
            <li><strong>Lunes a Viernes:</strong> 10:00 AM a 8:00 PM</li>
            <li><strong>Sábados:</strong> 10:00 AM a 8:00 PM</li>
          </ul>
          
          <p><strong>Sitio Web:</strong> <a href="https://www.shalom.com.pe/" target="_blank" rel="noopener noreferrer">https://www.shalom.com.pe/</a></p>
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
        <p>Deja tu comentarios (solo si estás logueado)</p>
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
