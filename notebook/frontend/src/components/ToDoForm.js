import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            todo_project: props.projects[0]?.id,
            todo_creator: props.creators[0]?.id,
            todo_short_description: '', 
            todo_text: '', 
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.id]: event.target.value
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
            <form onSubmit={(event) => this.handleSubmit(event)}>
                
                <div className="form-group">
                    <label for="todo_project">todo_project</label> 
                    <select 
                        className="form-control" 
                        id="todo_project" 
                        onChange={(event) => this.handleChange(event)}>
                            {this.props.projects.map((item) => <option value={item.id}>{item.project_name}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label for="todo_creator">todo_creator</label>
                    <select 
                        className="form-control" 
                        id="todo_creator" 
                        onChange={(event) => this.handleChange(event)}>
                            {this.props.creators.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>
                
                <div className="form-group">
                    <label for="todo_short_description">todo_short_description</label>
                    <input type="text" className="form-control" id="todo_short_description" value={this.state.short_description} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="todo_text">todo_text</label>
                    <input type="text" className="form-control" id="todo_text" value={this.state.user} onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default ToDoForm;