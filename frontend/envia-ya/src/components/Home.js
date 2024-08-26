import React from "react";
import Filter from "./Filter";
import './Home.css';

const Home = () => {
    return (
        <div className="home-container">
            <h1>Bienvenidos a Envía Ya</h1>
            <p>Elige tu lugar de origen y destino para encontrar la mejor agencia</p>
            <Filter />
        </div>
    );
};

export default Home;