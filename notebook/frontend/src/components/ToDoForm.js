import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {short_description: '', user: 0 }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.id]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.short_description)
        console.log(this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="short_description">short_description</label>
                    <input type="text" className="form-control" id="short_description" value={this.state.short_description} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="user">user</label>
                    <input type="number" className="form-control" id="user" value={this.state.user} onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default ToDoForm;