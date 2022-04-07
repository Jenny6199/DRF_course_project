import React from 'react';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';
import Projects from './project';
import Users from './user';
import ToDo from './todo';
import LoginForm from './Auth';
import axios from 'axios';

const NotFound404 =({ location }) => {
    return (
      <div>
        <h3>Страница по адресу '{location.pathname}' не найдена.</h3>
      </div>
    )
  }

class MainMenu extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todo': [],
        }
    }

    get_path(){
        return 'http://127.0.0.1:8000/'
    } 

    load_data() {
        axios.get(this.get_path() + 'api/users/').then(response => {
            this.setState({users: response.data})
        }).catch(error => console.log(error))

        axios.get(this.get_path() + 'api/projects/').then(response => {
            this.setState({projects: response.data})
        }).catch(error => console.log(error))

        axios.get(this.get_path() + 'api/todo/').then(response => {
            this.setState({todo: response.data})
        }).catch(error => console.log(error))
    }
    
    get_token(username, password) {
        axios.post(this.get_path() + 'api-token-auth/', {username: username, password: password}).then(response => {
            console.log(response.data)
        }).catch(error => alert('Ошибка ввода логина или пароля!'))
    }

    componentDidMount() {
        this.load_data()
    }

    render() {
        return (
            <div>
                <h3>Главное меню</h3>
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
                    <li>
                        <Link to='/login'>Авторизация</Link>
                    </li>
                </ul>
                </nav>
                <hr></hr>
                <Switch>
                <Route exact path='/users' component={() => <Users />} />
                <Route exact path='/projects' component={() => <Projects />} />
                <Route exact path='/todo' component={() => <ToDo />} />
                <Route exoct path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                <Route component={NotFound404} />
                <Redirect from='/' to='/users' />
                </Switch>
            </BrowserRouter>
            </div>
        )
    }

}

export default MainMenu;
