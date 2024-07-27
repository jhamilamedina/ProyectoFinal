import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';
import Destinos from './components/Destinos';
import Empresas from './components/Empresas';
import Nosotros from './components/Nosotros';
import Inicio from './components/Inicio';

function App() {
  return (
    <Router>
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path='/destinos' element={<Destinos />} />
          <Route path='/empresas' element={<Empresas />} />
          <Route path='/Nosotros' element={<Nosotros />} />
          <Route path='/Inicio' element={<Inicio />} />
        </Routes>
      </main>
      <Footer />
    </Router>
  );
}

export default App;