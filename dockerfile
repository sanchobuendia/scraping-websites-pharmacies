FROM python:3.10-slim-buster

RUN pip install fastapi uvicorn
RUN apt-get update && apt-get install -y firefox-esr xvfb
RUN apt-get install -y xvfb xauth

COPY requirements.txt .

# Update pip
RUN pip install --upgrade pip

# Install the requirements
RUN pip install -r requirements.txt

# Copy the app folder to the container
COPY ./app .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]

