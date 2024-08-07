  import React from 'react';
  import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
  import Header from './components/Header';
  import Footer from './components/Footer';
  import Ayuda from './components/Ayuda';
  import Home from './components/Home';
  import Destinos from './components/Destinos';
  import Evaluacion from './components/Evaluacion';
  import EstrellasRating from './components/EstrellasRating';
  import Nosotros from './components/Nosotros';
  import Inicio from './components/Inicio';
  import Contacto from './components/Contacto';
  import Privacidad from './components/Privacidad';
  import './App.css'

  function App() {
    return (
      <Router>
        <div className='app-container'>
        <Header />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path='/destinos' element={<Destinos />} />
              <Route path='/Evaluacion' element={<Evaluacion />} />
              <Route path='/EstrellasRating' element={<EstrellasRating />} />
              <Route path="/rating-pagina" element={<div>Valoracion...</div>} />
              <Route path='/mas-evaluaciones' element={<div>Más evaluaciones...</div>} />
              <Route path='/Nosotros' element={<Nosotros />} />
              <Route path='/Inicio' element={<Inicio />} />
              <Route path='/Ayuda' element={<Ayuda />} />
              <Route path='/Contacto' element={<Contacto />} />
              <Route path='/Privacidad' element={<Privacidad />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    );
  }

export default App;
