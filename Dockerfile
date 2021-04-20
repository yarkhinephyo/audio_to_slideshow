FROM python:3.8-slim

COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader stopwords && \
  python -m nltk.downloader punkt && \
  python -m nltk.downloader averaged_perceptron_tagger

COPY ./app /app/

RUN mkdir /app/output && mkdir /app/input && chmod 777 /app/output /app/input

ENTRYPOINT ["python", "main.py"]