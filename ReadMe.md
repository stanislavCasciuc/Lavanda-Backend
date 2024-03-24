# Lavanda Din Livezi

## Description
Lavanda Din Livezi is a FastAPI application - ecommerce platform for selling lavender products. The application allows users to create, update, and delete tasks, as well as view all tasks and categories. The application is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.



## Installation
1. Clone the repository:
```
git clone https://github.com/your-username/lavanda-din-livezi.git
```
2. Navigate to the project directory:
```
cd src
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Configuration
1. Rename `config.example.py` to `config.py`.
2. Update `config.py` with your desired configurations, such as database settings, secret key, etc.

## Usage
1. Start the FastAPI server:
```
uvicorn main:app --reload
```
2. Access the API documentation at `http://127.0.0.1:8000/docs` to explore available endpoints and interact with the application.

## API Endpoints
- **GET /tasks**: Retrieve all tasks.
- **GET /tasks/{task_id}**: Retrieve a specific task by ID.
- **POST /tasks**: Create a new task.
- **PUT /tasks/{task_id}**: Update an existing task.
- **DELETE /tasks/{task_id}**: Delete a task.
- **GET /categories**: Retrieve all task categories.
- **GET /categories/{category_id}**: Retrieve a specific category by ID.

## Contributing
Contributions are welcome! If you'd like to contribute to Lavanda Din Livezi, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits
Lavanda Din Livezi was created by [Your Name]. Special thanks to the FastAPI team for providing an excellent framework for building APIs.


