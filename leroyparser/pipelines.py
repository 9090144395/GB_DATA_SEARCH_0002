# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
# from scrapy.pipelines.files import FilesPipeline # это для общих файлов


class LeroyparserPipeline:
    def process_item(self, item, spider):
        print()
        return item

class LeryaPhotosPipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print()
        # urls_for_image = response.xpath('//img [@slot="thumbs"]/@data-src')
        # urls_for_image_max_resolution = []
        # for url_item in urls_for_image:
        #     old_url = str(url_item)
        #     new_url =  old_url.replace(',h_82,',',h_2000,').replace(',w_82',',w_2000')
        #     urls_for_image_max_resolution.append(new_url)
        # loader.add_value('photos', urls_for_image_max_resolution)

        # Разница в фотках
        # https://res.cloudinary.com/lmru/image/upload/b_white,c_pad,d_photoiscoming.png,f_auto,h_2000,q_auto,w_2000/v1/LMCode/84044041_04.jpg
        # https://res.cloudinary.com/lmru/image/upload/b_white,c_pad,d_photoiscoming.png,f_auto,h_82,q_auto,w_82/v1/LMCode/84044041_04.jpg

        if item['photos']:
            for img_url in item['photos']:
                old_url = str(img_url)
                new_url =  old_url.replace(',h_82,',',h_2000,').replace(',w_82',',w_2000')
                try:
                    yield scrapy.Request(new_url)
                except Exception as e:
                    print(e)

    # переопределяем метод
    def item_completed(self, results, item, info):
        # results это список из кортежей - информация о процессе скачивания файла.
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item