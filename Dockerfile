FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN adduser user
RUN chown -R user:user /code/
RUN chmod -R 755 /code/
USER user