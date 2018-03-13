# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mysqlpjt.items import MysqlpjtItem
import operator
import re



class WeiweiSpider(CrawlSpider):
    name = 'weiwei'
    start_urls = ['http://www.ygdy8.net']
    rules = (
        Rule(LinkExtractor(allow=('html/gndy/'),
                           allow_domains=('www.ygdy8.net')), callback='parse_movieitem', follow=True),
    )

    # def parse_item(self, response):
    #     next_url = response.xpath('''//div[@class="x"]/td/a[6]/@href''').extract()
    #     next_url = "".join(next_url)
    #     if next_url != "":
    #         header = response.url
    #         header = header[: header.rfind("/") + 1]
    #         yield scrapy.Request(url=header + next_url, callback=self.parse_movieitem)

    def parse_movieitem(self, response):
        item = MysqlpjtItem()
        result1 = response.xpath('''//*[@id="read_tpc"]//*/text()''').extract()
        result2 = response.xpath('''//*[@id="Zoom"]//*/text()''').extract()
        result = result1 + result2
        rawResultStr = "".join(result)
        resultStr = rawResultStr.replace('\r', '').replace('\n', '')
        dictionary = {"movie_name": "◎译　　名", "real_name": "◎片　　名",
                      "time": "◎年　　代", "area": "◎产　　地",
                      "type": "◎类　　别", "language": "◎语　　言",
                      "sub": "◎字　　幕", "rating": "◎豆瓣评分",
                      "duration": "◎片　　长", "director": "◎导　　演",
                       "starting": "◎主　　演", "abstract": "◎简　　介",
                       "download_url": "【下载地址】"
                      }
        indexHelper = []
        index = {"movie_name": "", "real_name": "",
                      "time": "", "area": "",
                      "type": "", "language": "",
                      "sub": "", "rating": "0",
                      "duration": "", "director": "",
                       "starting": "", "abstract": "",
                       "download_url": ""}
        for key in dictionary.keys():
            indexHelper.append(resultStr.find(dictionary[key]))

        indexHelper = sorted(indexHelper)

        itemTmp = []
        for i in range(len(indexHelper) - 1):
            itemTmp.append(resultStr[indexHelper[i]: indexHelper[i + 1]])

        for i in itemTmp:
            for tag in dictionary.keys():
                if i.find(dictionary[tag]) != -1:
                    if i.rfind("◎") != 0:
                        endIndex = i.find("◎", 1)
                    else:
                        endIndex = len(i)
                    startIndex = len(dictionary[tag]) + 1
                    index[tag] = i[startIndex: endIndex].replace("'", " ")

        if index["rating"] != "":
            index["rating"] = index["rating"][:3]
        index["download_url"] = response.url
        img_url = response.xpath('''//div[@id="Zoom"]//img/@src''').extract()
        if len(img_url) != 0:
            index["image_url"] = "".join(img_url[0])
        else:
            index["image_url"] = ""
        index["starting"] = index["starting"].replace("\u3000\u3000\u3000\u3000\u3000\u3000", ",")
        if index["type"].find("/") != -1:
            index["type"] = index["type"][:index["type"].find("/")]

        if index["movie_name"] == "":
            item["movie_name"] = None
        else:
            print(index)
            for i in index.keys():
                item[i] = index[i]
            yield item

        next_url = response.xpath('''//div[@class="x"]/td/a[6]/@href''').extract()
        next_url = "".join(next_url)
        if next_url != "":
            header = response.url
            header = header[: header.rfind("/") + 1]
            yield scrapy.Request(url=header + next_url, callback=self.parse_movieitem)
