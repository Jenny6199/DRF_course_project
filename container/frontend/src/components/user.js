import React from 'react';

  const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.surname}</td>
            <td>{user.first_name}</td>
            <td>{user.parent_name}</td>
            <td>{user.birthday}</td>
            <td>{user.email}</td>
            <td>{user.role}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className='center'>
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

export default UserList;