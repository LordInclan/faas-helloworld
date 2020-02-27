FROM python
COPY . /usr/src/app
WORKDIR /app
COPY setup.py ./
RUN pip install .
COPY . .
CMD python ./main.py
