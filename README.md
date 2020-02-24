Tekwill - Python Course - Final Project:

A web-app that crawls all the ads from an ads site (999.md) and adds them to the SQL database (Django model). After that, user can search a car and the app shows him analysis about this car, such as: average market price, min, max price, total number of ads, top 5 ads, plot vizualization. Has sign up/login/logout system. Also has an API view.

This project uses:
- Python 3.7
- Django (web framework)
- Django REST Framework (DRF) (API)
- Scrapy (web crawling framework)
- Pandas (data analysis framework)
- Matplotlib/Plotly (data vizualization)
- SQLite3

```
python_course_project-master
├─ auto_price
│  ├─ auto_price
│  │  ├─ settings.py
│  │  ├─ urls.py
│  ├─ car_crawler
│  │  ├─ car_crawler
│  │  │  ├─ items.py
│  │  │  ├─ pipelines.py
│  │  │  ├─ settings.py
│  │  │  ├─ spiders
│  │  │  │  ├─ car_spider.py
│  ├─ db.sqlite3
│  ├─ main
│  │  ├─ admin.py
│  │  ├─ forms.py
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ templates
│  │  │  ├─ detail.html
│  │  │  ├─ index.html
│  │  │  ├─ login.html
│  │  │  ├─ no_ads.html
│  │  │  └─ signup.html
│  │  ├─ urls.py
│  │  ├─ views.py
│  ├─ manage.py
├─ README.md
├─ requirements.txt