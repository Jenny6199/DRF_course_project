import React from 'react';
import './App.css';
import UserList from './components/user';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    const users = [
      {
        'surname': 'Сапунов',
        'first_name': 'Максим',
        'parent_name': 'Сергеевич',
      },
      {
        'surname': 'Вораксо',
        'first_name': 'Иван',
        'parent_name': 'Михайлович',
      },
    ]
    this.setState(
      {
        'users': users
      }
    )
  }

  render ()  {
    return (
      <div>
        <UserList users={this.state.users} />
      </div>
    )
  }
}

export default App;
