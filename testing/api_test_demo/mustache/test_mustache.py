import pystache


class TestMustache:
    def test_mustache(self):
        print(pystache.render('Hi {{person}}!', {'person': 'Henry'}))

    def test_first_last_name(self):
        with open("say_hello.mustache", encoding="utf8") as f:
            r = pystache.render(f.read(), {
                "name": {
                    "first": "Michael",
                    "last": "Jackson"
                },
                "age": "40"
            })
        print(r)

    def test_sports_list(self):
        data = {
            "sportsNames": [
                {"name": "football"},
                {"name": "basketball"},
                {"name": "hiking"},
            ]
        }

        print(pystache.Renderer().render_name('sports', data))
