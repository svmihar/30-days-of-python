from my_sum import sum, product, add
import pytest


@pytest.mark.parametrize('x,y,result',[
    (7,3,10),
    ('hello','world','helloworld'),
    (10.5,25.5,36)
])
def test_add_parametrize(x,y,result):
    assert add(x,y) == result
    assert type(add(x,y)) == type(x)

@pytest.mark.number
def test_sum():
    assert sum([1,2,3]) == 6
    assert sum([1,2]) == 3
    assert sum([3,4]) == 7

@pytest.mark.number
def test_product():
    assert product(5,5) == 25
    assert product(2) == 4
    assert product(1) == 2

@pytest.mark.string
def test_add_string():
    hasil =add('hello','world')
    assert hasil == 'helloworld'
    assert isinstance(hasil,str)
    assert 'hello' in hasil
@pytest.mark.string
def test_product_string():
    hasil = product('hello',3)
    assert hasil == 'hellohellohello'
    assert isinstance(hasil,str)

