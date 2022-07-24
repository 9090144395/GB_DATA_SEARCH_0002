import scrapy
from scrapy.http import HtmlResponse
from leroyparser.items import LeroyparserItem
from scrapy.loader import ItemLoader


class LeroymerlinruSpider(scrapy.Spider):
    name = 'leroymerlinru'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/catalogue/kondicionery/']
    # дает 401 ошибку (стоит подзащитой Qrator)
    # чтобы работало нужны токены в куки, подсунул куки на время для выполнения задания (костыль)

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.start_urls = [f'https://leroymerlin.ru/catalogue/-{kwargs.get("search")}/']
    # так добавили параметры в запрос (это для примера)

    def parse(self, response):
        print()

        next_page = response.xpath("//a[contains(@aria-label,'Следующая страница')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//div[@class="phytpj4_plp largeCard"]/a/@href')
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

        # pagination

    def parse_ads(self, response: HtmlResponse):
        print()
        loader = ItemLoader(item=LeroyparserItem(), response=response)
        loader.add_xpath('name', '//h1[@itemprop="name"]/span/text()')
        loader.add_xpath('price', '//div[@itemprop="offers"]/meta[@itemprop="price"]/@content')

        loader.add_xpath('photos','//img [@slot="thumbs"]/@data-src')
        # loader.add_xpath('photos',
        #                  "//div[@class='swiper-zoom-container']/img/@src | "
        #                  "//div[@class='swiper-zoom-container']/img/@data-src")

        loader.add_value('url', response.url)
        yield loader.load_item()

        # name = response.xpath('//h1[@itemprop="name"]/span/text()').get()

        # name = response.xpath("//h1/text()").get()
        # price = response.xpath("//h3/text()").get()    # response.xpath("//div[@data-testid='ad-price-container']/h3/text()").getall()
        # photos = response.xpath("//div[@class='swiper-zoom-container']/img/@src | //div[@class='swiper-zoom-container']/img/@data-src ").getall()
        # yield OlxparserItem(name=name, price=price, photos=photos)