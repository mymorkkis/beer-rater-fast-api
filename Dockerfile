FROM python:3.13-slim-bullseye

WORKDIR /project

COPY poetry.lock pyproject.toml ./

# TODO Pin poetry version
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
