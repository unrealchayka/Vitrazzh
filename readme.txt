запуск:

python3 -m venv venv
source venv/bin/activate
pip install -r requarements
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

url

123.0.0.1:8000/home
