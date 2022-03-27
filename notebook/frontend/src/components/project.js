import React from "react";
import axios from "axios";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.project_URL}</td>
            <td>{project.members}</td>
            <td>{project.created_at}</td>
            <td>{project.is_active}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <caption>
                <h3>Проекты</h3>
            </caption>
            <th>Название проекта</th>
            <th>Адрес проекта</th>
            <th>Участники</th>
            <th>Дата создания</th>
            <th>Активен</th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

class Projects extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        'projects': []
      }
    }
  
    componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/projects/?limit=10')
      .then(response => {
        const projects = response.data.results
          this.setState(
            {
              'projects': projects
            }
          )
      }).catch(error => console.log(error))
    }
  
    render ()  {
      return (
        <div>
          <ProjectList projects={this.state.projects} />
        </div>
      )
    }
  }

export default Projects;