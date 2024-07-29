# Django Dynamic Models Project

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AriaEskan98/Django-Server.git
   cd myproject
2.Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3.Install dependencies:

   pip install -r requirements.txt
4.Run migrations:

   python manage.py makemigrations
   python manage.py migrate
5.Run the development server:

   python manage.py runserver

Open Postman and Test the Endpoints:

Import Data:

Create a POST request to http://127.0.0.1:8000/api/import/
Set the body to the example JSON data.
the JSON data can be like this: 
[
  {
    "model_name_1": {
      "column_1": "data",
      "column_2": ["array", "data"]
    }
  },
  {
    "model_name_2": {
      "column_1": "data"
    }
  },
  {
    "model_name_1": {
      "column_1": "data"
    }
  }
]

Click Send.



List Records by Model Name:

Create a GET request to http://127.0.0.1:8000/api/detail/<model_name>/
Replace <model_name> with the desired model name.
Click Send.



Get Record by ID:

Create a GET request to http://127.0.0.1:8000/api/detail/<model_name>/<id>/
Replace <model_name> with the desired model name and <id> with the record ID.
Click Send.






