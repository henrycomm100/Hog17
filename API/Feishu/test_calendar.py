import random

import pytest

from API.Feishu.calendar import FeishuCalendar


class TestCalendar:

    def setup_class(self):
        self.calendar = FeishuCalendar()
        self.summary = 'testsummary'
        self.description = 'testDescription'

    def test_add_calendar(self):
        r = self.calendar.add_calendar(self.summary, self.description)

        print(r['data'])
        assert r['code'] == 0
        assert r['msg'] == 'success'

        # # 数据检查
        # r = self.calendar.get_contact(self.userid)
        # assert r['name'] == self.name
