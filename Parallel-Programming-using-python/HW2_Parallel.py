# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:39:10 2020

@author: Dalton
"""

import time
import hashlib
import concurrent.futures
import multiprocessing

def encrypt(num): 
    hash_object = hashlib.sha256(str(num).encode())
    #print(hash_object.digest())

def retrieve_serial(numbers):
    for number in numbers:
        encrypt(number)

def retrieve_threaded(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(encrypt, numbers)

def retrieve_mp(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(encrypt, numbers)


if __name__ == "__main__":
    numbers = [x for x in range(5_000)]

    start_time = time.time()
    retrieve_serial(numbers)
    duration_serial = time.time() - start_time

    start_time = time.time()
    retrieve_threaded(numbers)
    duration_threads = time.time() - start_time

    start_time = time.time()
    retrieve_mp(numbers)
    duration_mp = time.time() - start_time
    
    print(f"Serial duration {duration_serial} seconds")

    print(f'Threading duration: {duration_threads}')

    print(f'Multiprocessing duration: {duration_mp}')