scrapy project 
```
demo05_scp/
    scrapy.cfg            # deploy configuration file

    demo05_scp/             # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
            quotes_spider.py    # first demo spider
```