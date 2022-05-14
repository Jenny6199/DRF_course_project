import React from 'react';

  const UserItem = ({user}) => {
    return (
        <tr key={user.id}>
            <td key={user.id + user.surname}>{user.surname}</td>
            <td key={user.id + user.first_name}>{user.first_name}</td>
            <td key={user.id + user.parent_name}>{user.parent_name}</td>
            <td key={user.id + user.birthday}>{user.birthday}</td>
            <td key={user.id + user.email}>{user.email}</td>
            <td key={user.id + user.role}>{user.role}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className='center'>
            <caption key={'users_caption'}>
                <h3>Пользователи</h3>
            </caption>
            <thead key={'users_thead'}>
                <tr key={'users_columns_info'}>
                    <th key={'th_user_surname'}>Фамилия</th>
                    <th key={'th_user_name'}>Имя</th>
                    <th key={'th_user_parent_name'}>Отчество</th>
                    <th key={'th_user_birthday'}>Дата рождения</th>
                    <th key={'th_user_email'}>Электронная почта</th>
                    <th key={'th_user_role'}>Должность</th>
                </tr>
            </thead>
            <tbody key={'users_tbody'}>
                {users.map((user) => <UserItem user={user} />)}               
            </tbody>
        </table>
    )
}

export default UserList;