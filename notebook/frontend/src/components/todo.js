import React from "react";

// import axios from "axios";

const ToDoItem = ({todo, deleteToDo}) => {
    return (
        <tr>
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
    )
}

const ToDoList = ({todos, deleteToDo}) => {
    return (
        <table>
            <caption>
                <h3>Заметки</h3>
            </caption>
            <th>Название проекта</th>
            <th>Создатель</th>
            <th>Текст</th>
            <th>Краткое описание</th>
            <th></th>
            <th>Дата обновления</th>
            <th></th>
            {todos.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo} />)}
        </table>
    )
}

export default ToDoList;