import pytest
import yaml


class TestDataDriven:

    @pytest.mark.parametrize('env', yaml.safe_load(open('../data/env.yaml')))
    def test_datadriven(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP是", env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的IP是", env["dev"])
