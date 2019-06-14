# genetic algorithm 
in reference to cs50's genetic algorithm stream in twitch    

interesting concept. 


> evolve, mutate, repeat

## how it works 
- figure what is the threshold/target/end/desired ouptut
- create random population to start
- compare every char to the target string. every single char. hitung tiap character yang bener. 
  - threshold ini yang bisa diganti tergantung pada poin 1. 
- creating *mating pool*, lead to desired output/target/threshold
  - di contoh ini mating pool diambil dari fitness score (yang di assign random) pada tiap char, berapa kali masuk ke dalam mating pool tergantung pada fitness scorenya. 
- crossover/breed pairs yang ada di mating pool jadi populasi baru, *possibly mutating* 
  - you need mutation to create a new "batch" / breed biar masuk ke threshold/target/desired output. 
  - dicontoh ini targeted mutation, jadi biar mutasinya lebih ke arah yang diinginkan ke dalam target / outputnya. 
![](img/Screen&#32;Shot&#32;2019-06-14&#32;at&#32;5.47.58&#32;PM.png)
![](img/Screen&#32;Shot&#32;2019-06-14&#32;at&#32;10.23.44&#32;PM.png)
 
 > good parents doesn't mean you have good children. 
 > mutation

## usage
```python 
python genetic.py
```
profit.
