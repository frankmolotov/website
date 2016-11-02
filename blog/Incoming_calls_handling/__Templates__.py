from grab.spider import Spider
import random
import requests


class MySpider(Spider):
    is_logged = False
    delay = 0
    thread_number = 0
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,de-CH;q=0.6,de;q=0.4',
        'Cache-Control': 'max-age=0, must-revalidate',
        # 'Content-Lenght': '162',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Cookie': '',
        'Host': 'www.genevaoption.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def prepare(self):
        super(MySpider, self).prepare()
        print ("[PARSER] START. NAME: %s. THREADS: %s. DELAY: %s" % (
            self.__class__.__name__,
            self.thread_number,
            self.delay
        ))

    def valid_response_code(self, code, task):
        return code in (403, 408)

    def create_grab_instance(self, **kwargs):
        grab = super(MySpider, self).create_grab_instance(**kwargs)
        grab.setup(hammer_mode=True, hammer_timeouts=((10, 20), (20, 30), (30, 40)))
        if self.is_logged:
            pass
        else:
            grab.setup(headers=self.headers)
            self.headers['Cookie'] = ''
            request = requests.get(
                'http://www.genevaoption.com/back.php/back/connection/form')
            cookies = request.cookies
            items = cookies.items()
            for name, value in items:
                self.headers['Cookie'] += name + '=' + value + '; '
            grab.go('http://www.genevaoption.com/back.php/back/connection/form')
            grab.doc.set_input_by_id('inputUsernameEmail', 'IncomingCallsBot')
            grab.doc.set_input_by_id('inputPassword', 'Incoming1@Calls&3Bot*16')
            grab.submit()
        return grab
