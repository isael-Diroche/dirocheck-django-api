FROM python:3.10.16-slim-bullseye

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY . .

RUN pip install --no-cache-dir --timeout=120 -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000