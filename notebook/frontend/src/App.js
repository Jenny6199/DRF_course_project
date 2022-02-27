import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  render () {
    return(
      <div>
        <h3>
          Главное приложение
        </h3>
      </div>
    )
  }
}

export default App;
