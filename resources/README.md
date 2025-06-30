# Late Show API
A RESTful API for managing TV show episodes, guest appearances, and ratings.

## Features

- **Episode Management**: Track show dates and episode numbers
- **Guest Database**: Store guest names and occupations
- **Appearance Tracking**: Rate guest performances (1-5 scale)

## Project Structure
lateshow/
├── app.py 
├── models.py 
├── seed.py 
├── requirements.txt 
│
├── resources/
│ ├── init.py 
│ ├── episodes.py 
│ ├── guests.py 
│ └── appearances.py 
└── migrations/ 



## Setup Instructions

1. **Clone the repository**:
   git clone https://github.com/PollyM-tech/Late-Show-API.git
   cd Late-Show-API

- Install dependencies:
pipenv install
pipenv shell

- Initialize database:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py

Run the server:
python app.py

API Documentation
Endpoints
Method	Endpoint	        Description
GET	   episodes	            List all episodes
GET	   episodes/<int:id>	Get specific episode with appearances
GET	   guests	            List all guests
POST   appearances	        Create new appearance


- Example Requests
Get all episodes:
curl http://localhost:5555/episodes

Create appearance:
curl -X POST http://localhost:5555/appearances \
  -H "Content-Type: application/json" \
  -d '{"rating":5,"episode_id":1,"guest_id":2}'

  # LICENSE
MIT License


