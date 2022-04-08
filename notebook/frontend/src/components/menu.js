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
            'token': '',
        }
    }

    get_path(){
        return 'http://127.0.0.1:8000/'
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    set_token(token) {
        localStorage.setItem('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post(this.get_path() + 'api-token-auth/', {username: username, password: password}).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Ошибка ввода логина или пароля!'))
    }

    get_token_from_storage() {
        const token = localStorage.getItem('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) 
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()

        axios.get(this.get_path() + 'api/users/', {headers}).then(response => {
            this.setState({users: response.data})
        }).catch(error => console.log(error))

        axios.get(this.get_path() + 'api/projects/', {headers}).then(response => {
            this.setState({projects: response.data})
        }).catch(error => console.log(error))

        axios.get(this.get_path() + 'api/todo/', {headers}).then(response => {
            this.setState({todo: response.data})
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
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
                            {this.is_authenticated() ? <button onClick={() => this.logout()}>Выйти</button> : <Link to='/login'>Авторизация</Link>}
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
