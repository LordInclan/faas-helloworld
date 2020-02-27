FROM python:alpine3.11
COPY . /usr/src/app
WORKDIR /app
COPY setup.py ./
RUN pip install .
COPY . .
CMD python ./main.py
