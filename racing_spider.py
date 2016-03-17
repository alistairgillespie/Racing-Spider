import scrapy

class RacingItem(scrapy.Item):
    fin = scrapy.Field()
    runner = scrapy.Field()
    number = scrapy.Field()


class RacingSpider(scrapy.Spider):
    name = 'racing'
    name = 'racenet.com.au'
    allowed_domains = ['racenet.com.au']
    start_urls = ['https://www.racenet.com.au/horse-racing-results/Albury/2016-03-17']

    def parse(self, response):
    	for table in response.xpath('//table[@class="tblLatestHorseResults"]'):
		    rows = response.xpath('.//tr[@class="tr_full_res_runner"]')
		    for row in rows:
		        item = RacingItem()
			item['fin'] = row.xpath('.//td[@class="first"]/text()').extract()
			item['runner'] = row.xpath('.//td[3]/a/text()').extract()
			item['number'] = row.xpath('.//td[3]/text()').extract()
			yield item