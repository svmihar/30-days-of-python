#! .venv/bin/python
import argparse
from fancy import fancy_generator

p = argparse.ArgumentParser()

p.add_argument('-a', action='store', nargs='+') # + kayak *args, tapi minimal satu, very nic c c e.

args = p.parse_args()
hasil = vars(args)['a']
print(fancy_generator(hasil))