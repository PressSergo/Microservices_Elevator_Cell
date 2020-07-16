FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD code/Example  /code/
CMD ["python"," manage.py runserver 0.0.0.0:8000"]