import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './EmpresaDetail.css';

const EmpresaDetail = () => {
    const { id } = useParams();
    const [empresa, setEmpresa] = useState(null);
    const [comentario, setComentario] = useState('');
    const [isExpanded, setIsExpanded] = useState(false);
    const user = JSON.parse(localStorage.getItem('user'));

    useEffect(() => {
        axios.get(`http://localhost:8000/api/empresas/${id}/`)
            .then(response => {
                setEmpresa(response.data);
            })
            .catch(error => {
                console.error('Error fetching empresa data', error);
            });
    }, [id]);

    if (!empresa) return <div>--- Loading ---</div>;

    const handleComentarioChange = (e) => {
        setComentario(e.target.value);
    };

    const handleComentarioSubmit = (e) => {
        e.preventDefault();

        if (!user) return; // Verifica si el usuario está autenticado

        const nuevoComentario = {
            empresa: id,
            usuario: user.id, // Usa el ID del usuario autenticado
            comentario: comentario,
        };

        axios.post('http://localhost:8000/api/comentarios/', nuevoComentario)
            .then(response => {
                setEmpresa((prevEmpresa) => ({
                    ...prevEmpresa,
                    Comentarios: [...prevEmpresa.Comentarios, response.data.data.comentario]
                }));
                setComentario('');
            })
            .catch(error => {
                console.error('Error al enviar el comentario', error);
            });
    };

    const toggleExpand = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div className="empresa-detail-container">
            <h1>{empresa.Empresa.nombre}</h1>
            <img src={`http://localhost:8000/${empresa.Empresa.logo}`} alt={`${empresa.Empresa.nombre} logo`} />
            <p><strong>Sede Principal:</strong> {empresa.Empresa.sede_principal}</p>
            
            <p>
                <strong>Descripción:</strong>
                <span className={isExpanded ? 'expanded' : 'collapsed'}>
                    {empresa.Empresa.descripcion}
                </span>
                <span className="show-more-link" onClick={toggleExpand}>
                    {isExpanded ? 'Ver menos' : 'Ver más'}
                </span>
            </p>
            
            <p><a href={empresa.Empresa.sitio_web} target="_blank" rel="noopener noreferrer">Visitar Sitio Web</a></p>

            <h2>Agencias</h2>
            {empresa.Agencias.map(agencia => (
                <div key={agencia.id} className="agencia-item">
                    <h3>{agencia.nombre_referencial}</h3>
                    <p><strong>Dirección:</strong> {agencia.direccion}</p>
                    <p><strong>Horario de Atención:</strong> {agencia.horario_de_atencion}</p>
                    <p><strong>Teléfono:</strong> {agencia.telefono}</p>
                </div>
            ))}

            <h2>Estrellas</h2>
            <div>
                <p>1 estrella: {empresa.Estrellas[0].estrella_1}</p>
                <p>2 estrellas: {empresa.Estrellas[0].estrella_2}</p>
            </div>

            <h2>Comentarios</h2>
            {empresa.Comentarios.length > 0 ? (
                empresa.Comentarios.map((comentario, index) => (
                    <div key={index} className="comentarios-item">
                        <p>{comentario.comentario}</p>
                    </div>
                ))
            ) : (
                <p>No hay comentarios.</p>
            )}

            {user ? (
                <div className="comentario-form">
                    <h3>Deja tu comentario</h3>
                    <form onSubmit={handleComentarioSubmit}>
                        <textarea
                            value={comentario}
                            onChange={handleComentarioChange}
                            placeholder="Escribe tu comentario aquí..."
                            required
                        />
                        <button type="submit">Enviar Comentario</button>
                    </form>
                </div>
            ) : (
                <div className="comentario-form no-user">
                <h3>Deja tu comentario</h3>
                    <textarea
                        placeholder="Para dejar un comentario nesecitas registrarte..."
                        readOnly
                    />
            </div>
            )}
        </div>
    );
};

export default EmpresaDetail;
