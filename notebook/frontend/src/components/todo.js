import React from "react";
import { Link } from "react-router-dom";
// import axios from "axios";

const ToDoItem = ({todo, deleteToDo}) => {
    return (
        <tbody>
            <tr key={todo.id}>
                <td>{todo.project}</td>
                <td>{todo.creator}</td>
                <td>{todo.text}</td>
                <td>{todo.short_description}</td>
                <td></td>
                <td>{todo.updated_at}</td>
                <td>
                    <button onClick={() => deleteToDo(todo.id)} type="button">Удалить</button>
                </td>
            </tr>
        </tbody>
    )
}

const ToDoList = ({todos, deleteToDo}) => {
    return (
        <div>
            <table>
                <caption>
                    <h3>Заметки</h3>
                </caption>
                <thead>
                    <tr>
                        <th>Название проекта</th>
                        <th>Создатель</th>
                        <th>Текст</th>
                        <th>Краткое описание</th>
                        <th></th>
                        <th>Дата обновления</th>
                    </tr>
                </thead>
                {todos.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo} />)}
            </table>
            <br></br>
            <Link to='/todo/create'>Добавить</Link>
        </div>
    )
}

export default ToDoList;