FROM python:3
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python3 manage.py migrate



COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
