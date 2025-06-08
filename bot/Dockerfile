FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY ./pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

COPY ./bot ./bot
COPY .env .env

CMD ["poetry", "run", "python", "bot/bot.py"]
