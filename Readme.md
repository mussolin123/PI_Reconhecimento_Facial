HTML: http://127.0.0.1:8000/alunos/

python -m venv ambiente
ambiente\Scripts\activate
pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
python manage.py createsuperuser