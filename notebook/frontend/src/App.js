import React from 'react';
import './App.css';
import MainMenu from './components/menu';
import PageFooter from './components/footer';
/*
import Users from './components/user';
import Projects from './components/project';
import ToDo from './components/todo';
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom';
*/
import axios from 'axios';

/*
const NotFound404 = ({location}) => {
  return (
    <div>
      <h3>Страница по адресу '{location.pathname}' не найдена</h3>
    </div>
  )
}
*/


class App extends React.Component {
  constructor(props) {
    super(props)
    this.stat = {
      'users': [],
      'projects': [],
      'todo': []
    }
  }

  load_data() {
    const api_path = 'http://127.0.0.1:8000/api/'

    axios.get(api_path + 'users').then(response => {
      this.setState({users: response.data})
    }).catch(error => console.log(error))

    axios.get(api_path + 'projects').then(response => {
      this.setState({projects: response.data})
    }).catch(error => console.log(error))

    axios.get(api_path + 'todos').then(response => {
      this.setState({todo: response.data})
    }).catch(error => console.log(error))
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
/*    <div className="App">
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/users/'>Пользователи</Link>
              </li>
              <li>
                <Link to='/projects/'>Проекты</Link>
              </li>
              <li>
                <Link to='/todo/'>Заметки</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/users' component={() => <Users />} />
            <Route exact path='/projects' component={() => <Projects />} />
            <Route exact path='/todo' component={() => <ToDo />} />
            <Route component={NotFound404} />
            <Redirect from='/' to='/users' />
          </Switch>
        </BrowserRouter>
      </div>
*/      
    )
  }
}

export default App;
