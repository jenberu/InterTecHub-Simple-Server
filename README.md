InterTecHub Simple Server live at https://jemberu.pythonanywhere.com/

Follow the instructions below to set up and run the server locally.
## Prerequisites

1. **Python Installed**: Ensure you have Python 3.7+ installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Pip Installed**: Pip is usually included with Python. Verify by running:
   
   pip --version

Setup Instructions
1.Clone the repository:   

git clone https://github.com/jenberu/InterTecHub-Simple-Server.git

2.Navigate to the project directory:

cd simple-web-server

3.Install the required Python packages using the requirements.txt file:

pip install -r requirements.txt

4.Apply migrations to set up the database:

python manage.py makemigrations

python manage.py migrate


5.Start the Django development server:

python manage.py runserver

You should see output like this in the terminal:

Starting development server at http://127.0.0.1:8000/

Quit the server with CONTROL-C.


Access the Server

Open your browser and visit the following on your local machine:

Name Route: http://127.0.0.1:8000/messages/name/

Response: "Jemberu Kassie"

Hobby Route: http://127.0.0.1:8000/messages/hobby/

Response: {"hobby": "Exploring technology related things"}

Dream Route: http://127.0.0.1:8000/messages/dream/

Response: "My dream is to build impactful technology solutions."

or you can click the link that displays on the home page
Additional Notes
If you encounter any issues, ensure all dependencies are installed correctly.
For any database-related errors, delete the db.sqlite3 file and rerun the migrations:







