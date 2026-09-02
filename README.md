# Stock Market REST API

A RESTful API built with Django REST Framework for managing and retrieving stock market data.

The API allows users to view stocks and their price history, search and filter stock data, create personal watchlists, and access protected endpoints using JWT authentication. The application uses PostgreSQL for data storage and is containerized using Docker and Docker Compose.



## Features

- User registration and JWT authentication
- View a list of available stocks
- View details of a specific stock using its symbol
- View historical stock prices
- Filter stocks by sector
- Search stocks by symbol or name
- Order stocks by name or creation date
- Filter stock prices by date
- Create and view a personal watchlist
- Pagination for API responses
- API throttling
- Application logging
- PostgreSQL logging
- Dockerized application with Docker Compose


## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** SimpleJWT
- **Filtering:** django-filter
- **Testing:** pytest, pytest-django
- **Web Server:** Gunicorn
- **Containerization:** Docker, Docker Compose
- **API Testing:** Postman


## Project Architecture

The application follows Django REST Framework's request-response architecture:

Client (Postman / Browser)
        ↓
URL Routing
        ↓
DRF Views
        ↓
Serializers
        ↓
Django Models
        ↓
PostgreSQL Database

- **URLs:** Route incoming API requests to the appropriate views.
- **Views:** Handle requests and contain the API logic.
- **Serializers:** Convert model data to/from JSON and validate incoming data.
- **Models:** Define the structure and relationships of the application's data.
- **PostgreSQL:** Stores users, stocks, stock prices, and watchlist data.


When running with Docker Compose, the application uses two main services:

**Web:** Runs the Django REST API using Gunicorn.
**Database:** Runs PostgreSQL with persistent storage using a Docker volume.

The web service communicates with PostgreSQL through Docker's internal network.



## Installation and Local Setup

### 1. Clone the repository

```bash
git clone <https://github.com/Satish5806/StockAPI.git>
cd stockAPI
```

### 2. Create and activate a virtual environment

Create the environment:
```bash
python -m venv venv
```

Activate it on Windows:
```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies
``` bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```
Make sure PostgreSQL is running and the database has been created.

### 5. Apply database migrations
``` bash
python manage.py migrate
```

### 6. Run the development server
``` bash
python manage.py runserver
```

Make sure the API is available at:
http://127.0.0.1:8000/

## Docker Setup

Make sure Docker Desktop is installed and running.

### 1. Build and start the containers
``` bash
docker compose up --build
```

To run the containers in the background:
``` bash
docker compose up -d --build
```

### 2. Stop the containers
``` bash
docker compose down
```

### 3. View logs
``` bash
docker compose logs -f
```

### 4. View API
Once the containers are running the API will be availabe at:
http://localhost:8000/

Docker Compose automatically connects the Django web service to the PostgreSQL database using Docker's internal network.



## API Endpoints

### 1. Authentication

- `POST /api/register/` - Reginster a new user
- `POST /api/token/` - Login and get JWT tokens
- `POST /api/token/refresh/` - Get a new access token

### 2. Stocks

- `GET /api/stocks/` - View all stocks
- `GET /api/stocks/<symbol>/` - View a specific stock
- `GET /api/stocks/<symbol>/prices/` - View stock price history

### 3. Watchlist

- `GET /api/watchlist/` - View your watchlist
- `POST /api/watchlist/` - Add a stock to your watchlist


## Authentication

The API uses JWT authentication using SimpleJWT.

### 1. Register a User

Send a POST request to:

```text
/api/register/
```

Example:

```json
{
        "username": "testuser",
        "email": "test@email.com",
        "password": "testpass123"
}
```

### 2. Login

Send a POST request to:

```text
/api/token/
```

with:

```json
{
        "username": "testuser",
        "password": "testpass123"
}
```

The API returns an access token and a refresh token.

### 3. Access Protected Endpoints

Include the access token in the request header:

```text
Authorization: Bearer <access_token>
```
The access token is used to access protected endpoints such as stocks and watchlist.



## Filtering, Search and Ordering

The stocks API supports filtering, searching, and ordering using query parameters.

### 1. Filter by Sector

```text
/api/stocks/?sector=Bank
```
### 2. Search by Symbol or Name

```text
/api/stocks/?search=NABIL
```

### 3. Order Stocks

```text
/api/stocks/?ordering=name
```

Use `-` for descending order:

```text
/api/stocks/?ordering=-created_at
```

### 4. Filter Stock Prices by Date

```text
/api/stocks/NABIL/prices/?date=2026-08-01
```


## Testing

The project uses pytest and pytest-django for testing the API.

### 1. Run Tests

```bash
pytest
```

The test cover:

- Authentication for protected endpoints
- User registration
- Duplicate username validation
- Valid stock detail requests
- Invalid stock symbol requests


## Future Improvements

Possible improvements for the project:

- Add more stock market data and features
- Add update and delete options for the watchlist
- Integrate a real stock market data source
- Add more API tests
- Deploy the API to a cloud platform