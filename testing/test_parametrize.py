import pytest
import yaml


class TestParametrize:

    # @pytest.mark.parametrize('a, b', [(10,20),(222,333),(2222,3333)]) # string
    # @pytest.mark.parametrize(('a', 'b'), [(10,20),(222,333),(2222,3333)]) # string
    @pytest.mark.parametrize(['a', 'b'], [(10, 20), (222, 333), (2222, 3333)])  # string
    def test_parametrize(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open('../data/dataForAdd.yaml')))  # YAML file
    def test_parametrize2(self, a, b):
        print(a + b)

    def test_add(self):
        a = 10
        b = 20
        print(a + b)

    def test_add2(self):
        a = 222
        b = 333
        print(a + b)

    def test_add3(self):
        a = 2222
        b = 3333
        print(a + b)
