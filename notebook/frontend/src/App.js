import React from 'react';
import './App.css';
import MainMenu from './components/menu';
import Users from './components/user';
import Projects from './components/project';
import ToDo from './components/todo';
import PageFooter from './components/footer';


class App extends React.Component {
  render ()  {
    return (
      <div>
        <MainMenu />
        <Users/>
        <Projects />
        <ToDo />
        <PageFooter />
      </div>
    )
  }
}

export default App;
