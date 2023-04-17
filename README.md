# webscrape_oracle

#steps

1.change mongodb database string in ws2/settings.py

2.docker-compose up --build



things to note--

line 47 in settings.py CORS_ORIGIN_ALLOW_ALL = True

line 29 in settings.py ALLOWED_HOSTS = ['*']

if u are changing models you need to 
python manage.py makemigrations - to change migreation files
python manage.py migrate  -to populate db
