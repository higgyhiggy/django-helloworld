FROM python:3
WORKDIR /code
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
RUN echo pwd
RUN python3 manage.py migrate
RUN echo "password@3\npassword@3\n" | python3 manage.py createsuperuser --username admin --email admin@mail.com



CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
