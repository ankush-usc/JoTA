import scrapy
from scrapy.contrib.loader import ItemLoader
from indeed_model import IndeedModel
import _mysql
import sys




class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = ["http://www.indeed.com/jobs?q=software+engineer&l="]

    def parse(self, response):
        listings = response.xpath('//div[@class="pagination"]/a')
        company_list = response.xpath('//span[@class="company"]')
        location_list = response.xpath('//span[@class="location"]')
        summary_list = response.xpath('//span[@class="summary"]')
        date_list = response.xpath('//span[@class="date"]')
        jobTitle_list = response.xpath('//a[contains(@data-tn-element,"jobTitle")]')

        number = min(len(company_list),len(location_list),len(summary_list),len(date_list),len(jobTitle_list))
        i=0
        while i < number:
            indeeditem = IndeedModel()
            if company_list[i].xpath('text()').extract()[0].strip():
                indeeditem['company'] = company_list[i].xpath('text()').extract()[0].strip()
            else:
                indeeditem['company'] = company_list[i].xpath('span/text()').extract()[0].strip()

            indeeditem['summary'] = summary_list[i].xpath('text()').extract()[0]
            indeeditem['date'] = date_list[i].xpath('text()').extract()[0]
            if location_list[i].xpath('span[@itemprop="addressLocality"]/text()').extract():
                loc = location_list[i].xpath('span[@itemprop="addressLocality"]/text()').extract()[0]
            else:
                loc = location_list[i].xpath('text()').extract()[0]

            if len(loc.split(',')) > 1:
                indeeditem['location'] = loc.split(',')[1].split()[0]
            else:
                indeeditem['location'] = loc

            indeeditem['joblink'] = jobTitle_list.xpath('@href').extract()[0]
            indeeditem['jobtitle'] = jobTitle_list.xpath('@title').extract()[0]
            summary="C"
            skills = ["C++","Java", "Kernel Debugging", "Python"]
            for skill in skills:
                if skill in indeeditem['summary']:
                    summary += "," + skill

            i=i+1


            try:
                con = _mysql.connect('localhost', '', '', 'testdb')
                query="INSERT INTO jota VALUES (\""+indeeditem['location']+"\",\""+indeeditem['company']+"\",\""+summary +"\",\""+indeeditem['date']+"\",\""+indeeditem['jobtitle']+"\",\""+indeeditem['joblink']+"\");"
                query.encode('utf-8','ignore')
                print query
                con.query(query)


                print "After inserting"


            except _mysql.Error, e:

                print "Error %d: %s" % (e.args[0], e.args[1])
                pass

            finally:

                if con:
                    con.close()
        for l in listings:
            if l.xpath('span/span/text()').extract():
                nextlink = "http://www.indeed.com" + l.xpath('@href').extract()[0]
                print nextlink
        return scrapy.http.Request(nextlink, callback=self.parse)






    try:
        con = _mysql.connect('localhost', '', '', 'testdb')
        query = "SELECT * FROM jota INTO OUTFILE \'/Users/meerapatil/jobscloud.txt\';"
        con.query(query)



    except _mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        pass

    finally:
        if con:
            con.close()













