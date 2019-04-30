# multiprocessing
this essentially distribute all computation to all processors
hasil komputasi yang harus nyambung satu sama lain dapat menggunakan.... 

## what this py does
- menguadratkan angka per prosesor pada pc yang digunakan untuk ngerun
- digunakan untuk bypass GIL(global interpreter lock)-nya python 

process: buat pooling
current_process: buat ngecek status per process-nya (worker)
```python
Process(target=square, args=(number,))
```
where parameter `target` isinya function, dan parameter `args` isinya adalah tuple yang berisi argumen yang ingin dimasukkan ke dalam function yang ada di dalam target

**jangan lupa kalau args butuh**: 
- set
- (number **,** ) --> butuh koma setelah argumen pertama (this i don't know why, but still a keharusan tho.)
  - koma dibutuhkan jika argumen hanya satu


process dimulai dengan membuat `Process` object dan call `start()` method. jangan lupa dimasukkan ke dalam list setiap `Process` objeknya 

untuk mendapat current process yang sedang diproses di dalam prosesor bisa pake `os.getid()`

```python 
for process in processes: 
    process.join()
```
this guy checks if all the processes in the processes list is completed

# locks
using locks in multiprocessing modules: 
In computer science, a lock or mutex (from mutual exclusion) is a **synchronization mechanism for enforcing limits on access to a resource** in an environment where there are many threads of execution. A lock is designed to enforce a mutual exclusion concurrency control policy.

dengan menggunakan `Value` library dari multiprocessing, sehingga mempunyai shared value untuk seluruh process yang terjadi 

so without the lock the list of process gets jumbled together. Makannya setiap hasil dari functionya pasti berbeda karena tergantung siapa duluan yang ke run. Makannya digunakan `lock.acquire()` dan `lock.release()` biar proses berjalan bersamaan tapi sekuensial (tergantung siapa yang di acquire dan di release duluan.)

## logging
```python
    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO)
```
prints whatever the logging method in the multiprocessing library

## pool 
distributes the function to all available processors

- async
- all the processor will execute a subset of the function given (:beer:)
- serial vs multiprocessing
    - serial: 
        - `Processing 10000 took 5.036634683609009 time using serial processing`
    - multiprocessing: 
        - `Processing 10000 took 4.030598163604736 time using multiprocessing`
- making gede multiprocessing scales better than serial

## queue
maek seperate processes that 'communicate' with each other