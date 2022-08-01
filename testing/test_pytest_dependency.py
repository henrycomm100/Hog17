import pytest


@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False


@pytest.mark.dependency()
def test_b():
    pass


@pytest.mark.dependency(depends=["test_a"])
def test_c():  # 因为依赖a，但a失败，所以c不会执行
    pass


@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass


@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():  # 因为依赖c，但c没有执行，所以e不会执行
    pass
