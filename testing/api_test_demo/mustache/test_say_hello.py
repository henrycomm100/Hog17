import pystache

from testing.api_test_demo.mustache.say_Hello import SayHello


class TestSayHello:
    def test_say_hello(self):
        hello = SayHello()
        r = pystache.Renderer()
        print(r.render(hello))
