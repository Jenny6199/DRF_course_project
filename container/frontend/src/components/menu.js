import React from 'react';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';
import ProjectList from './project';
import UserList from './user';
import ToDoList from './todo';
import LoginForm from './Auth';
import axios from 'axios';
import Cookies from 'universal-cookie';
import ToDoForm from './ToDoForm';


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
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}/`, {headers})
          .then(response => {
            this.setState({todo: this.state.todos.filter((item) => item.id !== id)})
        }).catch(error => console.log(error))
    }

    createToDo(todo_project, todo_creator, todo_short_description, todo_text) {
        const headers = this.get_headers()
        const data = {
            project: todo_project.id,
            creator: todo_creator.id,
            short_description: todo_short_description, 
            text: todo_text, 
        }
        console.log(data)
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
            .then(response => {
                console.log(response.data)
                let new_todo = response.data
                const user = this.state.users.filter((item) => item.id === new_todo.user)[0]
                new_todo.user = user
                this.setState({short_description: [...this.state.todos, new_todo]})
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
            <header>
                <div className='header_mainblock wrapper'>
                    <BrowserRouter>
                        <nav>
                            <div className='flexbox center bottom_50'>
                                <div className='href border_1 top_50'>
                                    <h4>
                                        <Link to='/users/'>Пользователи</Link>
                                    </h4>
                                </div>
                                <div className='href border_1 top_50'>
                                    <h4>
                                        <Link to='/projects/'>Проекты</Link>
                                    </h4>
                                </div>
                                <div className='href border_1 top_50'>
                                    <h4>
                                        <Link to='/todo/'>Заметки</Link>
                                    </h4>
                                </div>
                            </div>
                        </nav>
                        <div className='flexbox center border_1'>
                            <h4 className='center top_50 bottom_50'>
                                {this.is_authenticated() ? <div>{this.get_username_from_storage()}</div> : <div>Авторизируйтесь</div>}
                            </h4>
                            <div className='center top_50 bottom_50'>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Выйти</button> : <Link to='/login'>Авторизация</Link>}
                            </div>
                        </div>
                        <Switch>
                            <Route exact path='/users' key={'users-list'} component={() => <UserList users={this.state.users} />} />
                            <Route exact path='/projects' key={'project-list'} component={() => <ProjectList projects={this.state.projects} />} />
                            <Route exact path='/todo/create' key={'todo-create'} component={() => <ToDoForm creators={this.state.users} projects={this.state.projects} createToDo={(todo_project, todo_creator, todo_short_description, todo_text) => this.createToDo(todo_project, todo_creator, todo_short_description, todo_text)} />} />
                            <Route exact path='/todo' key={'todo-list'} component={() => <ToDoList todos={this.state.todos} deleteToDo={(id) => this.deleteToDo(id)} />} />
                            <Route exoct path='/login' key={'login-page'} component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                            <Route key={'not-found'} component={NotFound404} />
                            <Redirect key={'redirct'} from='/' to='/users' />
                        </Switch>
                    </BrowserRouter>
                </div>
            </header>
        )
    }

}

export default MainMenu;
