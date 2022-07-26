from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from leroyparser.spiders.leroymerlinru import LeroymerlinruSpider
# from jobparser.spiders.sjru import SjruSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(LeroymerlinruSpider)
    # runner.crawl(LeroymerlinruSpider, search='какой-то параметр в get запросе') # для примера
    # далее нужно в родительском классе дописать - смотри метод init в пауке (закоменчен)
    # runner.crawl(SjruSpider)


    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

