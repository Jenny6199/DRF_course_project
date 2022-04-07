import React from 'react';
import './App.css';
import MainMenu from './components/menu';
import PageFooter from './components/footer';



class App extends React.Component {

  render ()  {
    return (
      <div>
        <MainMenu />
        <hr></hr>
        <PageFooter />
      </div>      
    )
  }
}

export default App;
