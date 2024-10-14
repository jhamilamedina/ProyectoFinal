import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ user, children }) => {
  return user.id ? children : <Navigate to="/inicio" />;
};

export default ProtectedRoute;
