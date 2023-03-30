FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install pytz
RUN pip3 install python-dotenv
RUN pip3 install pynamodb
RUN pip3 install Django
RUN pip3 install pipenv
RUN pip3 install django-cors-headers
RUN pip3 install django-storages
RUN pip3 install djangorestframework
RUN pip3 install djongo
RUN pip3 install dnspython
RUN pip3 install pymongo
RUN pip3 install pynamodb
RUN pip3 install python-dotenv
RUN pip3 install requests
RUN pip3 install websockets
COPY . .

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
#CMD ["python3", "manage.py", "runserver"]
