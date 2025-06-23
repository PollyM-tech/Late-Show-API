# 🎬 Late Show API

A Flask-based RESTful API for managing episodes, guests, and their appearances on the Late Show.

## Project Structure

lateshow_project/
│
├── app.py 
├── models.py 
├── seed.py 
├── resources/ 
│ ├── init.py
│ ├── episodes.py
│ ├── guests.py
│ └── appearances.py
├── migrations/
├── lateshow.db 
└── README.md

### Setup Instructions

1. Clone the repo
[git clone https://github.com/yourusername/lateshow-firstname-lastname.git](https://github.com/PollyM-tech/Late-Show-API.git)
cd lateshow-firstname-lastname

2. Create and activate a virtual environment
pipenv install
pipenv shell

3. Install dependencies
pip install -r requirements.txt
If using pipenv, the packages are installed from Pipfile.

4. Set up the database
export FLASK_APP=app:create_app
export PYTHONPATH=.

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. 5. Run the app
python app.py
App runs at:
👉 http://127.0.0.1:5555

API Endpoints
🔹 Episodes
Method	Endpoint	  Description
GET	   episodes	     Get all episodes
GET	   episodes/<id> Get single episode
POST   episodes	     Create episode
PATCH  episodes/<id> Update episode
DELETE episodes/<id> Delete episode

🔹 Guests
Method	 Endpoint	 Description
GET	     guests	     Get all guests
GET	     guests/<id> Get single guest
POST	 guests	     Create guest
PATCH	 guests/<id> Update guest
DELETE	 guests/<id> Delete guest

🔹 Appearances
Method	 Endpoint	       Description
POST	 appearances	   Create new appearance
GET	     appearances/<id>  Get appearance by ID
PATCH	 appearances/<id>  Update appearance
DELETE	 appearances/<id>  Delete appearance

## Validations
Rating (Appearance): Must be an integer between 1 and 5.

Proper error messages returned for missing or invalid data.

## Sample Request
POST /appearances
json
Copy
Edit
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}
Response:
json
Copy
Edit
{
  "id": 10,
  "rating": 5,
  "guest_id": 2,
  "episode_id": 1,
  "guest": {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  },
  "episode": {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
}
Postman
You can use the provided challenge-4-lateshow.postman_collection.json to test all endpoints.

## Author
PollyM-Tech
Phase 4 - Flatiron School Project
Flask + SQLAlchemy + Flask-Migrate + Flask-RESTful

## Tech Stack
Python 3.8+
Flask
Flask-RESTful
Flask-Migrate
SQLAlchemy
SQLite (dev)


