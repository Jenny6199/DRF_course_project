import React from 'react';
import './App.css';
import MainMenu from './components/menu';
import PageFooter from './components/footer';
import axios from 'axios';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todo': []
    }
  }

  get_path() {
    const api = 'http://127.0.0.1:8000/api/'
    this.setState = {
      api_path: api
    }
  }

  load_data() {
    const api_path = this.api_path

    axios.get(api_path + 'users/').then(response => {
      this.setState({users: response.data})
    }).catch(error => console.log(error))

    axios.get(api_path + 'projects/').then(response => {
      this.setState({projects: response.data})
    }).catch(error => console.log(error))

    axios.get(api_path + 'todos/').then(response => {
      this.setState({todo: response.data})
    }).catch(error => console.log(error))
  }

  get_token(username, password) {

    const api_path = this.api_path
    
    axios.post(api_path + 'api-token-auth/', {username: username, password: password}).then(response => {
      console.log(response.data)
    }).catch(error => alert('Ошибка ввода логина или пароля!'))
  }

  componentDidMount() {
    this.load_data()
  }

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
