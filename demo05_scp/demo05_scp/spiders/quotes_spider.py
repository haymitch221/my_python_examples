import scrapy

# step1: 定义 spider 类
class QuotesSpider(scrapy.Spider):
    # step2: spider类的名称, 必须是全局的且唯一的
    name = "quotes"

    # step3: spider起始于访问页面, 所在在这里定义访问页面的request
    #  使用scrapy的Request方法定义请求对象
    #   定义处理结果的callback方法, 例如自定义的parse方法
    #  需要返回可迭代的请求对象
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # step4: 自定义的callback方法
    #  参数response即封装的页面响应, 可以以此获取请求体、css等
    #  该方法中还可以调用response.follow继续用该方法抓取处理
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
