import React from 'react';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';
import ProjectList from './project';
import UserList from './user';
import ToDoList from './todo';
import LoginForm from './Auth';
import axios from 'axios';
import Cookies from 'universal-cookie';

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
            'todos': [],
            'token': '',
        }
    }

    deleteToDo(id) {
        const headers = this.get_headers()
        headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        console.log(headers)
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers: headers})
          .then(response => {
            this.setState({todo: this.state.todos.filter((item) => item.id !== id)})
        }).catch(error => console.log(error))
    }


    get_path(){
        return 'http://127.0.0.1:8000/'
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('', '')
    }

    set_token(token, username) {
        // localStorage.setItem('token', token)
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('username', username)
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post(this.get_path() + 'api-token-auth/', {username: username, password: password}).then(response => {
            this.set_token(response.data['token'], username)
        }).catch(error => alert('Ошибка ввода логина или пароля!'))
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        // const token = localStorage.getItem('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_username_from_storage() {
        const cookies = new Cookies()
        const username = cookies.get('username')
        return username
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
            this.setState({users: response.data.results})
        }).catch(error => {
            console.log(error)
            this.setState({users: []})
        })

        axios.get(this.get_path() + 'api/projects/', {headers}).then(response => {
            this.setState({projects: response.data.results})
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })

        axios.get(this.get_path() + 'api/todo/', {headers}).then(response => {
            this.setState({todos: response.data.results})
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
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
                            <li key={'users'}>
                            <Link to='/users/'>Пользователи</Link>
                            </li>
                            <li key={'projects'}>
                            <Link to='/projects/'>Проекты</Link>
                            </li>
                            <li key={'todos'}>
                            <Link to='/todo/'>Заметки</Link>
                            </li>
                            <li key={'login'}>
                            {this.is_authenticated() ? <button onClick={() => this.logout()}>Выйти</button> : <Link to='/login'>Авторизация</Link>}
                            </li>
                        </ul>
                    </nav>
                    {this.is_authenticated() ? <div>{this.get_username_from_storage()}</div> : <div>-Гость-</div>}
                    <Switch>
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos} deleteToDo={(id) => this.deleteToDo(id)} />} />
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
