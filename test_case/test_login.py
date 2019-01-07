import unittest
import requests
import json
import os,sys

file_obj = open(sys.path[0] + '\host.txt','rU')
url = file_obj.readline()
file_obj.close()
class Req_login(unittest.TestCase):

    def test_login(self):
        self.url = url +  'user/loginOn.do'
        self.payload = {'name': 'admin','password':'123'}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(self.url,params=self.payload,headers = self.headers)
        f = open(sys.path[0] + '\id.txt', 'w')
        f.write(str(json.loads(r.text)['rows'][0]))
        f.close()
        assert json.loads(r.text)['code']== '200'

    def test_login_withoutname(self):
        self.url = url + 'user/loginOn.do'
        self.payload = {'name': '', 'password': '123'}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post( self.url, params=self.payload, headers=self.headers)
        assert json.loads(r.text)['code'] == '500'

    def test_login_withnamenone(self):
        self.url = url + 'user/loginOn.do'
        self.payload = {'name': None, 'password': '123'}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(self.url, params=self.payload, headers=self.headers)
        assert json.loads(r.text)['code'] == '500'

    def test_login_withpwdnull(self):
        self.url = url + 'user/loginOn.do'
        self.payload = {'name': 'admin','password':''}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(self.url,params=self.payload,headers = self.headers)
        assert json.loads(r.text)['code'] == '500'

    def test_login_withpwdnone(self):
        self.url = url + 'user/loginOn.do'
        self.payload = {'name': 'admin','password':None}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(self.url,params=self.payload,headers = self.headers)
        assert json.loads(r.text)['code'] == '500'

    def test_login_withnull(self):
        self.url = url + 'user/loginOn.do'
        self.payload = {'name': '', 'password': ''}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(self.url, params=self.payload, headers=self.headers)
        assert json.loads(r.text)['code'] == '500'

    def test_login_withnone(self):
        self.url = url + 'user/loginOn.do'
        self.payload = {'name': None, 'password': None}
        self.headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(self.url, params=self.payload, headers=self.headers)
        assert json.loads(r.text)['code'] == '500'

if __name__ == '__main__':
    unittest.main()