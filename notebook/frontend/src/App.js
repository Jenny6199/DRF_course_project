import React from 'react';
import './App.css';
import MainMenu from './components/menu';
import PageFooter from './components/footer';
import axios from 'axios';


class App extends React.Component {

  deleteToDo(id) {
    const headers = this.get_headers()
    axios.delete('http://127.0.0.1:8000/api/todo/${id}', {headers, headers})
      .then(response => {
        this.setState({todo: this.state.todo.filter((item) => item.id !== id)})
    }).catch(error => console.log(error))
  }

  render ()  {
    return (
      <div>
        <MainMenu />
        <PageFooter />
      </div>      
    )
  }
}

export default App;
