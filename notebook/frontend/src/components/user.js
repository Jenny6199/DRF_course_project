import React from 'react';
import axios from 'axios';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.surname}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.parent_name}
            </td>
            <td>
                {user.birthday}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                {user.role}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <caption>
                <h3>Пользователи</h3>
            </caption>
            <th>Фамилия</th>
            <th>Имя</th>
            <th>Отчество</th>
            <th>Дата рождения</th>
            <th>Электронная почта</th>
            <th>Должность</th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

class Users extends React.Component {
  constructor(props) {
      super(props)
      this.state = {
        'users': []
      }      
    }
  
    componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/users/?limit=10')
      .then(response => {
        const users = response.data.results
          this.setState(
            {
              'users': users
            }
          )
      }).catch(error => console.log(error))
    }
  
    render ()  {
      return (
        <div>
          <UserList users={this.state.users} />
        </div>
      )
    }
  }

export default Users;