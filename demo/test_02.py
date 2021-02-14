import pytest

def add_function(a,b):
    return a+b
data = [(1,2,3),(3,4,7),(2,4,6)]
@pytest.mark.parametrize("a,b,expected",data,ids=["int","minus","bigint"])
def testlogin(a,b,expected):
    assert add_function(a,b) == expected
    print("login")


@pytest.mark.parametrize("a",[1,2])
@pytest.mark.parametrize("b",[3,4])
def testlogin(a,b):
    print("测试组合: a->%s,b->%s"%(a,b))