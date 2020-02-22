from scrapy_djangoitem import DjangoItem
from main.models import CarBase

class CarCrawlerItem(DjangoItem):
    django_model = CarBase
