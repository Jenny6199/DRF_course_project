import React from 'react'

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
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>Фамилия</th>
            <th>Имя</th>
            <th>Отчество</th>
            <th>Дата рождения</th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList