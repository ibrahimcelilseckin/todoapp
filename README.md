# Todo App

This is a simple Todo application. Users can add tasks, mark them as completed, and delete them. The application is built using the Flask web framework.

## Features

- Add new Todos (tasks)
- Mark Todos as completed
- Undo completed Todos (mark as incomplete)
- Delete Todos
- Simple and user-friendly interface

## Technologies

- **Flask**: Python-based web framework
- **HTML/CSS**: Structure and styling for the user interface
- **SQLite/PostgreSQL**: Database (optional selection)
- **JavaScript (optional)**: For dynamic content (animations, AJAX, etc.)

## Installation

### Requirements

- Python 3.x
- Pip (Python package manager)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<ibrahimcelilseckin>/todo-app.git
    cd todo-app
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Initialize the database** (based on SQLite or PostgreSQL):
    - If you are using SQLite, the database will be created automatically.
    - If you are using PostgreSQL, configure the database settings in the `config.py` file and run:
      ```bash
      flask db init
      ```

4. **Start the application**:
    ```bash
    flask run
    ```

    This will start the application on your local server, accessible at [http://localhost:5000](http://localhost:5000).

## Usage

- **Add Todo**: Enter a new task in the input field on the home page and click the "Add" button.
- **Mark as Completed**: Click the "Completed" button to mark a task as done.
- **Undo Completed Todo**: Click the "Undo" button to revert a completed task to incomplete.
- **Delete Todo**: Click the trash icon to delete a task.

## Contributing

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/<your_username>/todo-app.git
    ```

2. Create a new branch:
    ```bash
    git checkout -b new-feature
    ```

3. Make your changes and commit them:
    ```bash
    git add .
    git commit -m "Add task creation feature"
    ```

4. Push your changes to GitHub:
    ```bash
    git push origin new-feature
    ```

5. Open a pull request (PR) on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
