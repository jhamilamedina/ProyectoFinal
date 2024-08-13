import React, {useEffect, useState} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const EmpresaDetail = () => {
    const {id} = useParams();
    const [empresa, setEmpresa] = useState(null);

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

    return (
        <div>
            <h1>{empresa.Empresa.nombre}</h1>
            <img src={`http://localhost:8000/${empresa.Empresa.logo}`} alt={`${empresa.Empresa.nombre} logo`} />
            <p><strong>Sede Principal:</strong> {empresa.Empresa.sede_principal}</p>
            <p><strong>Descripción:</strong> {empresa.Empresa.descripcion}</p>
            <p><a href={empresa.Empresa.sitio_web} target="_blank" rel="noopener noreferrer">Visitar Sitio Web</a></p>

            <h2>Agencias</h2>
            {empresa.Agencias.map(agencia => (
                <div key={agencia.id}>
                    <h3>{agencia.nombre_referencial}</h3>
                    <p><strong>Dirección:</strong> {agencia.direccion}</p>
                    <p><strong>Horario de Atención:</strong> {agencia.horario_de_atencion}</p>
                    <p><strong>Teléfono:</strong> {agencia.telefono}</p>
                </div>
            ))}

            <h2>Valoraciones</h2>
            {/* Mostrar las valoraciones y estrellas aquí */}
            <p>Puntualidad: {empresa.Valoraciones[0].puntualidad}</p>
            <p>Seguridad: {empresa.Valoraciones[0].seguridad}</p>
            {/* Agrega más valoraciones según sea necesario */}

            <h2>Estrellas</h2>
            <p>1 estrella: {empresa.Estrellas[0].estrella_1}</p>
            <p>2 estrellas: {empresa.Estrellas[0].estrella_2}</p>
            {/* Continua con las demás estrellas */}

            <h2>Comentarios</h2>
            {empresa.Comentarios.length > 0 ? (
                empresa.Comentarios.map((comentario, index) => (
                    <div key={index}>
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