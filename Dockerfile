FROM python:3.11.3-bullseye

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8051
CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.address=0.0.0.0"]