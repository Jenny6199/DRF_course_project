import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            todo_project: 0,
            todo_creator: 0,
            todo_short_description: '', 
            todo_text: '' }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.id]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.todo_project)
        console.log(this.state.todo_creator)
        console.log(this.state.todo_short_description)
        console.log(this.state.todo_text)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="todo_project">todo_project</label>
                    <input type="number" className="form-control" id="todo_project" value={this.state.short_description} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="todo_creator">todo_creator</label>
                    <input type="number" className="form-control" id="todo_creator" value={this.state.short_description} onChange={(event) => this.handleChange(event)}/>
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