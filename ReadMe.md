# Lavanda Din Livezi

## Description
Lavanda Din Livezi is a robust FastAPI application designed as an e-commerce platform for selling exquisite lavender products. Whether you’re a fan of soothing lavender-scented candles, luxurious skincare items, or delightful culinary treats, Lavanda Din Livezi has something to offer


## Installation
1. Clone the repository:
```
git clone https://github.com/stanislavCasciuc/Lavanda-Backend.git
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
1. Create a new database in PostgreSQL:
```
CREATE DATABASE lavanda_din_livezi;
```
2. Write .env file with the following content:
```
DATABASE_URL=postgresql+asyncpg://username:password@localhost/lavanda_din_livezi
```
3. Run the database migrations:
```
alembic upgrade head
```
## Usage
1. Start the FastAPI server:
```
uvicorn main:app --reload
```
2. Access the API documentation at `http://localhost:8000/docs` to explore available endpoints and interact with the application.

3. Access admin panel at `http://localhost:8000/admin/login` to manage products and categories.

## API Endpoints
You can see the API documentation at `http://localhost:8000/docs` to explore available endpoints and interact with the application.

## Contributing
Contributions are welcome! If you'd like to contribute to Lavanda Din Livezi, please fork the repository and submit a pull request with your changes.


## Credits
Lavanda Din Livezi was created by Casciuc Stanislav. Special thanks to the FastAPI team for providing an excellent framework for building APIs.


