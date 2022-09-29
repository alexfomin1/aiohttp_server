FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN export PYTHONPATH=.
RUN alembic revision -m 'create table Message' --autogenerate
RUN alembic upgrade head
CMD ["python", "main.py"]