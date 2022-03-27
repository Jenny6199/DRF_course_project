import React from "react";

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
            <th>Название проекта</th>
            <th>Адрес проекта</th>
            <th>Участники</th>
            <th>Дата создания</th>
            <th>Активен</th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;