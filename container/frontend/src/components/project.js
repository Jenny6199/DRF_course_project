import React from "react";
// import axios from "axios";

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
        <table className='center'>
            <caption>
                <h3>Проекты</h3>
            </caption>
            <thead key={'thead_projects'}>
                <tr>
                    <th>Название проекта</th>
                    <th>Адрес проекта</th>
                    <th>Участники</th>
                    <th>Дата создания</th>
                    <th>Активен</th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem project={project} />)}
            </tbody>

        </table>
    )
}

export default ProjectList;