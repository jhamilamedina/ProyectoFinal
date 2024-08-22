import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './EmpresaDetail.css';

const EmpresaDetail = () => {
    const { id } = useParams();
    const [empresa, setEmpresa] = useState(null);
    const [isExpanded, setIsExpanded] = useState(false);

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

            <h2>Valoraciones</h2>
            <div>
                <p>Puntualidad: {empresa.Valoraciones[0].puntualidad}</p>
                <p>Seguridad: {empresa.Valoraciones[0].seguridad}</p>
            </div>

            <h2>Estrellas</h2>
            <div>
                <p>1 estrella: {empresa.Estrellas[0].estrella_1}</p>
                <p>2 estrellas: {empresa.Estrellas[0].estrella_2}</p>
            </div>

            <h2>Comentarios</h2>
            {empresa.Comentarios.length > 0 ? (
                empresa.Comentarios.map((comentario, index) => (
                    <div key={index} className="comentarios-item">
                        <p>{comentario}</p>
                    </div>
                ))
            ) : (
                <p>No hay comentarios.</p>
            )}
        </div>
    );
};

export default EmpresaDetail;
