import unittest
import requests
import json
import os,sys

file_obj = open(sys.path[0] + '\host.txt','rU')
url = file_obj.readline()
file_obj.close()

f = open(sys.path[0] + '\id.txt','rU')
id = f.readline()
f.close()

class Req_menu(unittest.TestCase):

    def test_first_level(self):
        self.url = url + 'menu/findUserRoleMenuByUserId.do?id=' + id
        r = requests.get(self.url)
        result = ''
        file = open(sys.path[0] + '\menuId.txt', 'w')
        for x in json.loads(r.text)['rows']:
            result += str(x['id']) + ','
        file.write(result[:-1])
        file.close()
        assert json.loads(r.text)['code']== '200'

    def test_second_level(self):
        menu_txt = open(sys.path[0] + '\menuId.txt','rU')
        menuId = menu_txt.readline()
        menu_txt.close()
        menuIdSon = menuId.split(',')
        for x in menuIdSon:
            self.url = url + 'menu/findLeftMenu.do?id=' + id + '&menuId=' + x
            r = requests.get(self.url)
            assert json.loads(r.text)['code'] == '200'

if __name__ == '__main__':
    unittest.main()
