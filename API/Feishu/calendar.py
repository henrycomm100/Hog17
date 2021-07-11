import requests

from API.Feishu.base import Base


class FeishuCalendar(Base):
    def teardown(self):
        pass

    def add_calendar(self, summary: str, description: str):
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        data = {
            "summary": summary,
            "description": description
        }
        r = self.send('POST', url, json=data)
        return r.json()
    #
    # def get_calendar_list(self, userid: str):
    #     url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars'
    #     r = self.send('GET', url)
    #
    #     return r.json()
    #
    # def get_calendar(self, userid: str):
    #     url = f'https://open.feishu.cn/open-apis/contact/v3/departments/:department_id'
    #     params = {
    #         "userid": userid
    #     }
    #     r = self.send('GET', url, params=params)
    #
    #     return r.json()
    #
    # def update_calendar(self, userid: str, name: str):
    #     url = f'https://open.feishu.cn/open-apis/contact/v3/departments/:department_id'
    #     data = {
    #         "userid": userid,
    #         "name": name
    #     }
    #     r = self.send('POST', url, json=data)
    #     return r.json()
    #
    # def delete_calendar(self, userid: str):
    #     url = f'https://open.feishu.cn/open-apis/contact/v3/departments/:department_id'
    #     params = {
    #         "userid": userid
    #     }
    #     r = self.send('GET', url, params=params)
    #
    #     return r.json()
