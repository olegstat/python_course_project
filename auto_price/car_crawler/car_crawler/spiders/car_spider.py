import scrapy
from car_crawler.items import CarCrawlerItem

class CarsSpider(scrapy.Spider):
    name='cars'
    start_urls  = ["https://999.md/ru/list/transport/cars?applied=1&eo=57&o_2029_593=18668&view_type=short&r_6_2_unit=eur&selected_currency=eur&ef=260&ef=6&ef=4112&ef=1&ef=2029&ef=1279&ef=5&r_6_2_to=&o_1279_775=18592&o_260_1=776&o_4112_795=18895&r_6_2_from=&page="] #url is already with filters
    
    def parse(self, response):
        n = 17 #first 16 elements on the page are paid ads
        name = 0 #is required because last n+=1 count will give us empty iteration
        try:
            while name != []:
                item = CarCrawlerItem()
                #extracting row data
                name = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[3]/div/h3/a/text()").extract()
                price_raw = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[8]/text()").extract()
                year_raw = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[4]/text()").extract()
                engine_raw = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[5]/text()").extract()
                gearbox_raw = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[7]/text()").extract()
                ad_date_raw = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[9]/time/text()").extract()
                ad_url_raw = response.xpath(f"//*[@id='js-ads-container']/table/tbody/tr[{n}]/td[3]/div/h3/a/@href").extract()
                #cleaning the data
                make = name[0].split(" ", 1)[0]
                model = name[0].split(" ", 1)[1]
                price = price_raw[0].replace(" ", "")
                price = price.replace("\xa0€","")
                price = int(price.replace("≈", ""))
                engine = engine_raw[0].replace(" ", "")
                engine = int(engine.replace("см³", ""))
                year = int(year_raw[0].replace(" ", ""))
                gearbox = gearbox_raw[0].replace(" ", "")
                ad_date = ad_date_raw[0]
                ad_url = f"https://999.md{ad_url_raw[0]}"
                #sending the extracted data forward
                item['make'] = make
                item['model'] = model
                item['price'] = price
                item['year'] = year
                item['engine'] = engine
                item['gearbox'] = gearbox
                item['ad_url'] = ad_url
                item['ad_date'] = ad_date
                n+=1
                yield item
        #Using the n+=1 counter as next page indicator. Не баг, а фича :)
        except IndexError:
            print("Going to the next page...") 
        #paginator
        next_page = response.xpath("//*[contains(@class,'current')]/following-sibling::li/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
