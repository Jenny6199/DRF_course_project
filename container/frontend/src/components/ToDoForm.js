import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            todo_project: props.projects[0],
            todo_creator: props.creators[0],
            todo_short_description: '', 
            todo_text: '', 
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }  
        );
    }

    handleSubmit(event) {
       this.props.createToDo(
           this.state.todo_project, 
           this.state.todo_creator, 
           this.state.todo_short_description, 
           this.state.todo_text
        )
        event.preventDefault()
    }

    render() {
        return (
            <form  key={'ToDoForm'} onSubmit={(event) => this.handleSubmit(event)}>
                
                <div className="form-group" key={'project_field'}>
                    <label> Cоздать заметку в проекте: 
                        <select 
                            className="form-control" 
                            name="todo_project"
                            value={this.state.todo_project}
                            onChange={(event) => this.handleChange(event)}>
                                {this.props.projects.map((item) => <option value={item.project_name}>{item.project_name}</option>)}
                        </select>
                    </label>
                </div>

                <div className="form-group" key={'user_field'}>
                    <label key={'todo_creator'}> Автор заметки:
                        <select 
                            className="form-control" 
                            name="todo_creator"
                            value={this.state.todo_creator} 
                            onChange={(event) => this.handleChange(event)}>
                                {this.props.creators.map((item) => <option value={item.username}>{item.username}</option>)}
                        </select>
                    </label>
                </div>
                
                <div className="form-group" key={'short_description_field'}>
                    <label> Краткое описание, хэштэги: 
                        <input 
                            type="text" 
                            className="form-control" 
                            name="todo_short_description" 
                            value={this.state.short_description} 
                            onChange={(event) => this.handleChange(event)}
                        />
                    </label>
                </div>

                <div className="form-group" key={'todo_text_field'}>
                    <label> Текст заметки: 
                        <input 
                            type="text" 
                            className="form-control" 
                            name="todo_text" 
                            value={this.state.user} 
                            onChange={(event) => this.handleChange(event)}
                        />
                    </label>
                </div>
                <input 
                    key={'submit_todo'} 
                    type="submit" 
                    className="btn btn-primary top_50" 
                    value="Сохранить заметку" />
            </form>
        );
    }
}

export default ToDoForm;