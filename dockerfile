FROM python:3
WORKDIR /code
COPY requirements.txt .
RUN apt install sqlitebrowser
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN echo "password@3\npassword@3\" | python3 manage.py createsuperuser --username admin --email admin@mail.com


COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
