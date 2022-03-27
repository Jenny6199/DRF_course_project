import React from "react";
import axios from "axios";

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.creator}</td>
            <td>{todo.text}</td>
            <td>{todo.short_description}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return (
        <table>
            <caption>
                <h3>Заметки</h3>
            </caption>
            <th>Название проекта</th>
            <th>Создатель</th>
            <th>Текст</th>
            <th>Краткое описание</th>
            <th>Дата создания</th>
            <th>Дата обновления</th>
            <th>Заметка активна</th>
            {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

class ToDo extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        'todos': []
      }
    }
  
    componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/todo/?limit=10')
      .then(response => {
        const todos = response.data.results
          this.setState(
            {
              'todos': todos
            }
          )
      }).catch(error => console.log(error))
    }

    render ()  {
        return (
          <div>
            <ToDoList todos={this.state.todos} />
          </div>
        )
      }
}

export default ToDo;