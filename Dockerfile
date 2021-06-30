FROM python:3.9.6-slim-buster

RUN pip install 'poetry==1.1.7'

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction

COPY . /app
CMD ["poetry", "run", "python3", "main.py"]