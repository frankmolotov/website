import urllib.request
import json
import ast
import time

from __Templates__ import MySpider
from grab.spider import Task


class SwitchUser(MySpider):
    thread_number = 0
    today_date = time.strftime("%d/%m/%Y")
    initial_urls = [
        "http://www.genevaoption.com/back.php/client/crmCustomersBo/getCustomersCrm?dateDebut=01/01/2013&dateFin=" + today_date + "&filtre=registration&etatClient=&dernierDepotId=&compteId=&campagneId=&isLeads="]

    def task_initial(self, grab, task):
        response = grab.doc.unicode_body()
        response = response.replace('\\', '')
        response = response.replace('"""', '"')
        data = json.loads(response)
        yield Task('find_number', data=data, url=task.url)

    def task_find_number(self, grab, task):  # find items in dict(json)
        for item in task.get('data')['data']:
            for key in item:
                if item[key] == self.caller_number:
                    url = 'http://www.genevaoption.com/back.php/clientB/default/searchAssignSeler?client_id=' + \
                          item['id']
                    print(url)
                    yield Task('get_name', url=url)

    def task_get_name(self, grab, task):
        response = grab.doc.unicode_body()
        print(json.loads(response)[0]['value'])
        print(time.strftime('%H:%M:%S'))


print(time.strftime('%H:%M:%S'))
SwUser = SwitchUser(caller_number="+79109139157", thread_number=2)  # inhernit class
SwUser.run()

# print temp
# print SwitchUser.getNumber(id,usrurl)
# print SwitchUser.makeResList('yo')
