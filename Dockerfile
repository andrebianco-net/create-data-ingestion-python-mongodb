FROM python:3

WORKDIR /app

COPY . /app

RUN python -m venv .venv

RUN sh .venv/bin/activate

RUN pip install --upgrade pip

RUN python -m pip install -r requirements.txt

CMD ["python", "core/data_ingestion_products.py"]