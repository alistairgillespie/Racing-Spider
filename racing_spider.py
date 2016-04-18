import scrapy

class RacingItem(scrapy.Item):
    fin = scrapy.Field()
    runner = scrapy.Field()
    odds = scrapy.Field()


class RacingSpider(scrapy.Spider):
    name = 'racenet.com.au'
    allowed_domains = ['racenet.com.au']
    start_urls = ['https://www.racenet.com.au/horse-racing-results/']
    
    def parse(self, response):
    	for table in response.xpath('.//table[@class="tblLatestHorseResults"]'):
		    rows = table.xpath('.//tr[@class="tr_res_runner"]')
		    for row in rows:
		        item = RacingItem()
		        item['fin'] = row.xpath('.//td[@class="first"]/text()').extract()
		        item['runner'] = row.xpath('.//td[2]/a[@class="link_red bold"]/text()').extract()
		        item['odds'] = row.xpath('.//td[@class="res_odds sb res_td_light last"]/span/text()').extract()
		        yield item