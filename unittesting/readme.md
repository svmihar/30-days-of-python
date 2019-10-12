# unittesting
jangan lupa, tiap prefix `test_*`!
## unit test vs integration test
- unit test --> satu komponen
  - cek komponen kecil pada aplikais
- integration test --> multiple komponen
  - cek interaksi antara komponen bekerja sesuai kondisi atau tidak
## contoh: `assert`
```python
assert sum([1,2,3]) == 6, 'seharusnya enam'
# kondisi benar
assert sum([1,1,1]) == 6, 'seharusnya enam'
# kondisi salah akan keluar:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```
## test runner
- `unittest`
  - test harus masuk ke dalam sebuah class
    - `TestCase` instead of `assert`
    - `self.assertEqual()`
        ```python
        import unittest

        class TestZSm(unittest.TestCase):
            def test_sum(self):
                self.assertEqual(sum([1,2,3]),6,'seharusnya 6')
            def test_sum_tuple(self):
                self.assertEqual(sum((1,2,2)),6,'seharusnya 6')

        if __name__ == "__main__":
            unittest.main()
        ```
- `nose`
  - sama kaya unittest cuman file nya harus nama `test*.py`, disadur dari unittest nya sendiri
- `pytest`
  - `pytest.mark.something` biar bisa pake argumen `-m` terus tunjuk `something` yang mau di test
  - pytest bisa ngeskip test
    - pake decorator `@pytest.mark.skip(reason='apa alasan test ini di skip')`
    - dengan kondisi tertentu `@pytest.mark.skipif((pythonic condition here) reason='apa alasan test ini di skip)`
  - `parametrize`: running multiple test at one function
    - biar gak usah ngulang-ngulang manggil fungsi
  - biar lebih detail pake `pytest {nama file test}.py -v`
  - setiap file harus mulai dengan `test_*`
  - support banyak `assert`, bahkan ada yang spesial buat test semua kondisi assert pake `self.assert*()` method
  - filtering test case(?)
  - rerun from last failing test
  - punya banyak plugin
  - bisa bikin "global condition" pada pytest
    ```python
    def setup_module(module): #selalu mulai di awal
    print('------setup------')
    global db
    db = StudentDB()
    db.connect('data.json')

    def teardown_module(module): #selalu diakhiri dengan fungsi ini
        print('------teardown------')
        db.close()
    ```
    - atau pake `@pytest.fixture()`
    -


## structuring test
- tentukan mau buat
  - unit test
  - integration test
- workflow:
  - create input
  - execute code yang mau di test, capture output
  - test output pada kondisi yang diinginkan
  - auto discovery!!
- pada contoh di atas kaya di `sum()` ada beberapa kondisi yang harus di cek
  - menjumlahkan list_of_integers?
  - menjumlahkan set atau tuple?
  - menjumlahkan tipe data float?
  - menjumlahkan tipe data yang bukan berbasis angka?
  - menjumlahkan nilai yang negatif

## assertion
|nama method|ekivalen|
|----|---|
|`.assertEqual(a,b)`|`a==b`|
|`.assertTrue(x)`|`bool(x) is True`|
|`.assertFalse(x)`|`bool(x) is False`|
|`.assertIs(a,b)`|`a is b`|
|`.assertIsNone(x)`|`x is None`|
|`.assertIn(a,b)`|`a in b`|
|`.assertIsInstance(a,b)`|`isinstance(a,b)`|

# single responsibility principle!