FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.douban.com/simple/ -r requirements.txt

EXPOSE 808

ENV NAME World

CMD ["python", "app.py"]
