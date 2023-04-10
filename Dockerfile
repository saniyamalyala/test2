FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP app.py
ENV FLASK_ENV production
ENV SECRET_KEY=your_secret_key
CMD ["flask", "run", "--host","0.0.0.0"]
