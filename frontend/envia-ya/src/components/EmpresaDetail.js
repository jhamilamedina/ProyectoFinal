import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './EmpresaDetail.css';

const EmpresaDetail = () => {
    const { id } = useParams();
    const [empresa, setEmpresa] = useState(null);
    const [comentario, setComentario] = useState('');
    const [isExpanded, setIsExpanded] = useState(false);
    const [ratingAverage, setRatingAverage] = useState(0); // Para almacenar la valoración promedio
    const user = JSON.parse(localStorage.getItem('user'));

    useEffect(() => {
        axios.get(`http://localhost:8000/api/empresas/${id}/`)
            .then(response => {
                const data = response.data;
                setEmpresa(data);

                // Calcular la valoración promedio
                const totalStars = data.Estrellas.reduce((acc, estrella) => 
                    acc + estrella.estrellas_1 * 1 + estrella.estrellas_2 * 2 + estrella.estrellas_3 * 3 + 
                    estrella.estrellas_4 * 4 + estrella.estrellas_5 * 5, 0);

                const totalReviews = data.Estrellas.reduce((acc, estrella) => 
                    acc + estrella.estrellas_1 + estrella.estrellas_2 + estrella.estrellas_3 + 
                    estrella.estrellas_4 + estrella.estrellas_5, 0);

                setRatingAverage(totalStars / totalReviews || 0);
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
                const comentarioCreado = response.data.data.comentario;
                setEmpresa((prevEmpresa) => ({
                    ...prevEmpresa,
                    Comentarios: [...prevEmpresa.Comentarios, comentarioCreado]
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

    const renderStarRatings = () => {
        const { estrella_1, estrella_2, estrella_3, estrella_4, estrella_5 } = empresa.Estrellas[0];

        const starCounts = [
            { stars: 1, count: estrella_1 },
            { stars: 2, count: estrella_2 },
            { stars: 3, count: estrella_3 },
            { stars: 4, count: estrella_4 },
            { stars: 5, count: estrella_5 }
        ];

        return starCounts.map(({ stars, count }) => (
            <p key={stars}>
                {'⭐'.repeat(stars)} {count} {count === 1 ? 'voto' : 'votos'}
            </p>
        ));
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

            <h2>Estrellas <span>({ratingAverage.toFixed(1)})</span></h2>
            <div>
                {renderStarRatings()}
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

            {user && (
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
            )}
        </div>
    );
};

export default EmpresaDetail;
