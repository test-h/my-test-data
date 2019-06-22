import pytest
from common import *

@pytest.mark.parametrize(("x","y","z"),[
    [1,2,4],
    [2,2,4],
    [3,6,8]
])
def test_add(x,y,z):
    assert z == add(x,y)



