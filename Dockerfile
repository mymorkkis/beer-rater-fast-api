FROM python:3.11.1-slim-bullseye

WORKDIR /project

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"] 
