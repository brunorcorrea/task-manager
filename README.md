# Task Management API (To-Do List)

This task manager is a project to utilize Python, FastAPI and pytest.

## Main Features:

- Create a new task: Endpoint to create a new task with details such as title, description, and due date.
- List all tasks: Endpoint to retrieve a list of all existing tasks.
- Get details of a specific task: Endpoint to retrieve details of a specific task using an ID.
- Update a task: Endpoint to update details of an existing task.
- Delete a task: Endpoint to delete an existing task using an ID.

## Definition of Done (DoD):

### Environment Setup:

- Install Python and FastAPI.
- Set up a virtual environment.
- Install necessary dependencies (fastapi, uvicorn, pydantic).

### Project Structure:

- Create the basic project structure with directories for routes, models, and configurations.

### Data Modeling:

- Define data models using Pydantic to represent tasks.

### Endpoints:

- Implement all necessary endpoints (Create, Read, Update, Delete).
- Ensure all endpoints return appropriate responses and HTTP status codes.

### Validation and Errors:

- Add data validation for user input.
- Implement error handling and return appropriate error messages.

### Documentation:

- Utilize FastAPI's automatic documentation to describe endpoints and their functionalities.

### Testing:

- Write unit tests for each endpoint using pytest.
- Ensure all tests pass successfully.

### Execution and Deployment:

- Set up the development server execution using uvicorn.

## How to run the project:

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Go to the src directory using `cd src`.
4. Run the server using `uvicorn main:app --reload`.

## How to run the tests:

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Go to the src directory using `cd src`.
4. Run the server using `pytest`.
