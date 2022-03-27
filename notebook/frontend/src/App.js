import React from 'react';
import './App.css';
import Users from './components/user';
import MainMenu from './components/menu';
import ToDo from './components/todo';
import PageFooter from './components/footer';
import axios from 'axios';

class App extends React.Component {
  render ()  {
    return (
      <div>
        <MainMenu />
        <Users/>
        <ToDo />
        <PageFooter />
      </div>
    )
  }
}

export default App;
