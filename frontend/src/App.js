import React from 'react';
import './App.css';
import Signin from './SignIn';
import Dashboard from './Dashboard/Dashboard';

function App() {
  const token = localStorage.getItem('access_token');

  if(!token) {
    return <Signin />
  }

  return <Dashboard />
}

export default App;