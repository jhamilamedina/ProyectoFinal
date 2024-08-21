import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Ayuda from './components/Ayuda';
import Home from './components/Home';
import Destinos from './components/Destinos';
import Empresas from './components/Empresas';
import Evaluacion from './components/Evaluacion';
import Nosotros from './components/Nosotros';
import Inicio from './components/Inicio';
import Contacto from './components/Contacto';
import Privacidad from './components/Privacidad';
import Perfil from './components/Perfil';
import EmpresaDetail from './components/EmpresaDetail';
import Registro from './components/Registro';
// import { AuthProvider } from './context/AuthContext';

function App() {
  const [userName, setUserName] = useState(localStorage.getItem('nombre') || '');
  const [userEmail, setUserEmail] = useState(localStorage.getItem('correo') || '');

  const handleLogout = () => {
    localStorage.removeItem('nombre');
    localStorage.removeItem('correo');
    setUserName('');
    setUserEmail('');
  };

  return (
    <Router>
     
      <Header userName={userName} onLogout={handleLogout} />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/destinos" element={<Destinos />} />
          <Route path="/empresas" element={<Empresas />} />
          <Route path="/empresas/:id" element={<EmpresaDetail />} />
          <Route path="/evaluacion" element={<Evaluacion />} />
          <Route path="/nosotros" element={<Nosotros />} />
          <Route path="/registro" element={<Registro />} />
          <Route path="/inicio" element={<Inicio setUserName={setUserName} setUserEmail={setUserEmail} />} />
          <Route path="/ayuda" element={<Ayuda />} />
          <Route path="/contacto" element={<Contacto />} />
          <Route path="/privacidad" element={<Privacidad />} />
          <Route path="/perfil" element={<Perfil userName={userName} userEmail={userEmail} />} />
        
        </Routes>
      </main>
      <Footer />
      
    </Router>
  );
}

export default App;
