import scrapy

class IndeedModel(scrapy.Item):
	company = scrapy.Field()
	location = scrapy.Field()
	summary = scrapy.Field()
	date = scrapy.Field()
	jobtitle = scrapy.Field()
	joblink = scrapy.Field()


