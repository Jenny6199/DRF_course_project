import React from "react";
import { Link, } from "react-router-dom";
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
        <div>
            <table class='center'>
                <caption>
                    <h3>Заметки</h3>
                </caption>
                <thead key={'table_ToDo_head'}>
                    <tr>
                        <td>Название проекта</td>
                        <td>Создатель</td>
                        <td>Текст</td>
                        <td>Краткое описание</td>
                        <td></td>
                        <td>Дата обновления</td>
                    </tr>
                </thead>
                <tbody>
                    {todos.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo} />)}                    
                </tbody>
                <tfoot>
                    <tr>
                        <td>
                            <button className="btn btn-primary">
                                <Link to='/todo/create'>Добавить</Link>  
                            </button>
                             
                        </td>
                    </tr>
                                     
                </tfoot>
            </table>
        </div>
    )
}

export default ToDoList;