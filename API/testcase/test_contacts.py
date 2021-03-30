import random

import pytest

from API.Wework.WeworkContacts import WeworkContacts


class TestContacts:
    name = "eric"
    userid = "ericmurphy87"

    def setup_class(self):
        self.contact = WeworkContacts()

        self.mobile = "+86 13800000000"
        self.department = [1]

    def setup(self):
        self.contact.delete_contact(self.userid)

    def teardown(self):
        self.contact.delete_contact(self.userid)

    def test_add_contact(self):
        r = self.contact.add_contact(self.userid, self.name, self.mobile, self.department)

        assert r['errcode'] == 0
        assert r['errmsg'] == 'created'

        # 数据检查
        r = self.contact.get_contact(self.userid)
        assert r['name'] == self.name

    def test_get_contact(self):
        self.contact.add_contact(self.userid, self.name, self.mobile, self.department)

        r = self.contact.get_contact(self.userid)

        assert r['errcode'] == 0
        assert r['errmsg'] == 'ok'
        assert r['userid'] == self.userid

    @pytest.mark.parametrize("userid, new_name", [(userid, name + "tmp")] * 5)
    def test_update_contact(self, userid, new_name):
        userid = userid + str(random.randint(1, 100))
        print(userid)
        print(new_name)
        r = self.contact.add_contact(userid, self.name, self.mobile, self.department)
        print(r)

        r = self.contact.update_contact(userid, new_name)
        print(r)

        # 这一步很重要，将修改过的userid传给self.userid，这样，执行的teardown()方法会将新生成的contact删掉
        self.userid = userid
        
        assert r['errcode'] == 0
        assert r['errmsg'] == 'updated'

        # 数据检查
        r = self.contact.get_contact(userid)
        assert r['name'] == new_name

    def test_delete_contact(self):
        self.contact.add_contact(self.userid, self.name, self.mobile, self.department)

        r = self.contact.delete_contact(self.userid)

        assert r['errcode'] == 0
        assert r['errmsg'] == 'deleted'

        # 数据检查
        r = self.contact.get_contact(self.userid)
        print(r)
        assert r['errcode'] == 60111
