# container = [x for x in range(1, 117)]
import copy
from pprint import pprint

def buat_container(jumlah): 
    container = {}
    head = 0
    for x in range(0,jumlah): 
        if x%28==0: 
            head+=1
            container[x] = '---'
        else: 
            container[x]=0
    return container, head

def isi_head(input, container, jumlah_head=0):
    diganti = [0]
    hasil_input = [x*28 for x in range(input)]
    hasil_head = [x*28 for x in range(jumlah_head)]
    hasil_bool = [False for x in range(len(container))]


    container_baru = copy.deepcopy(container)
    for key, value in container_baru.items(): 
        if key%28 == 0: 
            container_baru[key] = '--HEAD--'
            hasil_bool[key] = True
    for value in hasil_input: 
        cek_value = value%len(container_baru) 
        print(cek_value)
        if cek_value != value: 
            hasil_bool[cek_value] = True
            container_baru[cek_value] = '--_HEAD_--'
            
    return container_baru, hasil_head, hasil_bool

if __name__ == "__main__":

    # pprint(container) 
    container, head = buat_container(100)
    container_isi, hasil_head, hasil_input = isi_head(10,container, jumlah_head=head)
    for key, value in container_isi.items():
        print(key, ':', value)
    print(hasil_input.count(True))
    # pprint(container_isi)