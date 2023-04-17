FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /movies
WORKDIR /movies
COPY requirements.txt /movies/
RUN pip install -r requirements.txt
COPY . /movies/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080