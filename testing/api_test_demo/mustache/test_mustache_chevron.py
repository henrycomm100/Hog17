import chevron


class TestMustacheChevron:
    def test_mustache_chevron(self):
        print(chevron.render('Hello {{person}}', {'person': 'Henry'}))

    def test_chevron_file(self):
        data = {
            "from_who": "Henry",
            "to_who": "Eric",
            "name": {
                "first": "Michael",
                "last": "Jackson"
            },
            "age": "40"
        }
        with open('say_hello.mustache', 'r') as f:
            print(chevron.render(f, data))
