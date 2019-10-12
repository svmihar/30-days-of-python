import pytest
from loading_data import StudentDB
""" setup and teardown module """
# db = None
# def setup_module(module):
#     print('------setup------')
#     global db
#     db = StudentDB()
#     db.connect('data.json')

# def teardown_module(module):
#     print('------teardown------')
#     db.close()


""" fixture decorator, pengganti setup and module """
@pytest.fixture(scope='module')
def db():
    print('setting up....')
    db = StudentDB()
    db.connect('data.json')
    yield db # di run setelah semua method db dipanggil. (multiple call return), eat that java

    print('teardown...')
    db.close()


def test_scott_data(db):
    scott = db.get_data('Scott')
    assert scott['id'] == 1
    assert scott['name'] == "Scott"
    assert scott['result'] == 'pass'

def test_mark_data(db):
    mark = db.get_data('Mark')
    assert mark['id'] == 2
    assert mark['name'] == "Mark"
    assert mark['result'] == 'fail'
