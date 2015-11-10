import scrapy
from scrapy.contrib.loader import ItemLoader
from indeed_model import IndeedModel

class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = [
	"http://www.indeed.com/jobs?q=software+engineer&l=California"
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
            #f.write(response.body)
	
	# Lets use 5 arrays
	company_list = response.xpath('//span[@class="company"]')
	location_list = response.xpath('//span[@class="location"]')
	summary_list = response.xpath('//span[@class="summary"]')
	date_list = response.xpath('//span[@class="date"]')
	jobTitle_list = response.xpath('//a[contains(@data-tn-element,"jobTitle")]')

	number = min(len(company_list),len(location_list),len(summary_list),len(date_list),len(jobTitle_list))
	i=0
	while(i<number):
		indeeditem = IndeedModel()
		if company_list[i].xpath('text()').extract()[0].strip():
                    indeeditem['company'] = company_list[i].xpath('text()').extract()[0].strip()
                else:
                    indeeditem['company'] = company_list[i].xpath('span/text()').extract()[0].strip()

		indeeditem['summary'] = summary_list[i].xpath('text()').extract()[0]
		indeeditem['date'] = date_list[i].xpath('text()').extract()[0]
		if location_list[i].xpath('span[@itemprop="addressLocality"]/text()').extract():
                        indeeditem['location'] = location_list[i].xpath('span[@itemprop="addressLocality"]/text()').extract()[0]
                else:
                        indeeditem['location'] = location_list[i].xpath('text()').extract()[0]
		indeeditem['joblink'] = jobTitle_list.xpath('@href').extract()[0]
                indeeditem['jobtitle'] = jobTitle_list.xpath('@title').extract()[0]
		i=i+1
		yield indeeditem

	
# Following logic is commented as it could be reused in future

'''	
	print len(company_list)
	print len(location_list)
	print len(summary_list)
	print len(date_list)
	print len(jobTitle_list)
	
	print "company list in order ---- "
	i = 1
	for c in company_list:
		print i
		if c.xpath('text()').extract()[0].strip():
		    print c.xpath('text()').extract()[0].strip()
		else: 
		    print c.xpath('span/text()').extract()[0].strip()
		i = i + 1

	
	print "Summary list in order ---------------- "
	i = 0
	for s in summary_list:
		print i
		print s.xpath('text()').extract()[0]
		i=i+1

	print "Date list in order ---------------  "
	i=1
	for d in date_list:
		print i
		print d.xpath('text()').extract()[0]
		i=i+1
	
	print "Location list in order -----------"
	for l in location_list:
		if l.xpath('span[@itemprop="addressLocality"]/text()').extract():
			print l.xpath('span[@itemprop="addressLocality"]/text()').extract()[0]
		else:
			print l.xpath('text()').extract()[0]

	print "Jobtitle list in order  ------------"
	for j in jobTitle_list:
		print j.xpath('@href').extract()[0]
		print j.xpath('@title').extract()[0]	
'''
