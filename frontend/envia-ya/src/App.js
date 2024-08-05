import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Ayuda from './components/Ayuda';
import Home from './components/Home';
import Destinos from './components/Destinos';
import Empresas from './components/Empresas';
import Evaluacion from './components/Evaluacion';
import EstrellasRating from './components/EstrellasRating';
import Nosotros from './components/Nosotros';
import Inicio from './components/Inicio';
import Contacto from './components/Contacto';
import Privacidad from './components/Privacidad';
import ListaAgencias from './components/ListaAgencias';
import ListaShalom from './components/ListaShalom';
import ListaDHL from './components/ListaDHL';
import ListaServientrega from './components/ListaServientrega';
import ListaFedEX from './components/ListaFedEx';
import ListaUps from './components/ListaUps';
import ListaUrbano from './components/ListaUrbano';
import ListaTransmar from './components/ListaTransmar';

function App() {
  return (
    <Router>
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path='/destinos' element={<Destinos />} />
          <Route path='/empresas' element={<Empresas />} />
          <Route path='/Evaluacion' element={<Evaluacion />} />
          <Route path='/EstrellasRating' element={<EstrellasRating />} />
          <Route path="/rating-pagina" component={() => <div>Valoración...</div>} />
          <Route path='/mas-evaluaciones' component={() => <div>Más evaluaciones...</div>} />
          <Route path='/Nosotros' element={<Nosotros />} />
          <Route path='/Inicio' element={<Inicio />} />
          <Route path='/Ayuda' element={<Ayuda />} />
          <Route path='/Contacto' element={<Contacto />} />
          <Route path='/Privacidad' element={<Privacidad />} />
          <Route path='/ListaAgencias' element={<ListaAgencias />} />
          <Route path='/ListaShalom' element={<ListaShalom />} />
          <Route path='/ListaDHL' element={<ListaDHL />} />
          <Route path='/ListaServientrega' element={<ListaServientrega />} />
          <Route path='/ListaFedEX' element={<ListaFedEX />} />
          <Route path='/ListaUps' element={<ListaUps />} />
          <Route path='/ListaUrbano' element={<ListaUrbano />} />
          <Route path='/ListaTransmar' element={<ListaTransmar />} />
        </Routes>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
