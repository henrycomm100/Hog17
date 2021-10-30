import yaml


class TestYaml:
    def test_yaml(self):
        data = yaml.safe_load(open("../data/dataForCalculator.yaml"))
        print(data)
        print(data['add']['number'])
        print(data['add']['id'])
        print(data['divide'])
        return data
