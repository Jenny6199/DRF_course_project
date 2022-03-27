import React from 'react'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'


const MainMenu = () => {
    return (
        <div>
            <BrowserRouter>
                <nav>
                    <ul>
                        <li>
                            <h5>Главная</h5>
                        </li>
                        <li>
                            <Link to='/users'>Пользователи</Link>
                        </li>
                        <li>
                            <h5>Контакты</h5>
                        </li>
                    </ul>
                </nav>
            </BrowserRouter>
        </div>
    )
}

export default MainMenu;
