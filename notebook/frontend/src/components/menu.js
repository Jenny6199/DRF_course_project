import React from 'react';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';
import Projects from './project';
import Users from './user';
import ToDo from './todo';
import LoginForm from './Auth';

const NotFound404 =({ location }) => {
    return (
      <div>
        <h3>Страница по адресу '{location.pathname}' не найдена.</h3>
      </div>
    )
  }

const MainMenu = () => {
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

export default MainMenu;
