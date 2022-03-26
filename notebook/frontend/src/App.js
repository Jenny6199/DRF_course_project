import React from 'react';
import './App.css';
import UserList from './components/user';
import MainMenu from './components/menu';
import Footer from './components/footer';
import axios from 'axios'
import PageFooter from './components/footer';
import default_footer from './components/footer';

class App extends React.Component {
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
        <MainMenu />

        <UserList users={this.state.users} />

        <PageFooter />
      </div>
    )
  }
}

export default App;
