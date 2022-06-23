"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio
import nest_asyncio
import time




nest_asyncio.apply()

async def factorial(number):
    #start_time_factorial_async = time.time()
    fact = 1
    for i in range(2, number + 1):
        #print('Asyncio.Task: Compute factorial(%s)' % i)
        await asyncio.sleep(0)
        fact *= i
    #duration_factorial_async = time.time() - start_time_factorial_async
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))
    #print(f'Async factorial function took {(duration_factorial_async)} seconds')
    async_results.append(fact)
    #return duration_factorial_async

def factorial_serial(number):
    #duration_factorial_serial = 0
    #float(duration_factorial_serial)
    #start_time_factorial_serial = time.time()
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    #duration_factorial_serial = time.time() - start_time_factorial_serial
    print('Serial.Task - factorial(%s) = %s' % (number, fact))
    #print(f'Serial factorial function took {float(duration_factorial_serial)} seconds')
    serial_results.append(fact)
    #return duration_factorial_serial



async def fibonacci(number):
    #start_time_fib_async = time.time()
    a, b = 0, 1
    for i in range(number):
        #print('Asyncio.Task: Compute fibonacci(%s)' % i)
        await asyncio.sleep(0)
        a, b = b, a + b
    #duration_fib_async = time.time() - start_time_fib_async
    print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))
    #print(f'Async fibonacci function took {(duration_fib_async)} seconds')
    async_results.append(a)
    #return duration_fib_async
    
    
def fibonacci_serial(number):
    #duration_fib_serial = 0
    #float(duration_fib_serial)
    #start_time_fib_serial = time.time()
    a, b = 0, 1
    for i in range(number):
        a, b = b, a + b
    #duration_fib_serial = time.time() - start_time_fib_serial
    print('Serial.Task - fibonacci(%s) = %s' % (number, a))
    #print(f'Serial fibonacci function took {float(duration_fib_serial)} seconds')
    serial_results.append(a)
    #return duration_fib_serial


async def binomial_coefficient(n, k):
    #start_time_bi_async = time.time()
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        #print('Asyncio.Task: Compute binomial_coefficient(%s)' % i)
        await asyncio.sleep(0)
    #duration_bi_async = time.time() - start_time_bi_async
    print('Asyncio.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))
    #print(f'Async binomial function took {(duration_bi_async)} seconds')
    async_results.append(result)
    #return duration_bi_async
    
def binomial_coefficient_serial(n, k):
    #duration_bi_serial = 0
    #float(duration_bi_serial)
    #start_time_bi_serial = time.time()
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
    #duration_bi_serial = time.time() - start_time_bi_serial
    print('Serial.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))
    #print(f'Serial binomial function took {float(duration_bi_serial)} seconds')
    serial_results.append(result)
    #return duration_bi_serial
    
    


if __name__ == '__main__':
    
    serial_results = []
    async_results = []
    
    
    start_time_async = time.time()
    task_list_async = [asyncio.Task(factorial(1000)),
                 asyncio.Task(fibonacci(1000)),
                 asyncio.Task(binomial_coefficient(200, 100))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list_async))
    async_time = time.time() - start_time_async


    start_time_serial = time.time()
    factorial_serial(1000)
    fibonacci_serial(1000)
    binomial_coefficient_serial(200, 100)
    serial_time = time.time() - start_time_serial
    
    #serial_time = 0
    #async_time = 0

    #async_time += factorial(10)
    #serial_time += factorial_serial(10)
    #async_time += fibonacci(10)
    #serial_time += fibonacci_serial(10)
    #async_time += binomial_coefficient(20, 10)
    #serial_time += binomial_coefficient_serial(20, 10)
    
    print ('\n')
    print ('\n')
    print (f'All async calculations took a total of {async_time} seconds')
    print (f'All serial calculations took a total of {serial_time} seconds')

    serial_results.sort()
    async_results.sort()
    
    #print (async_results)
    #print (serial_results)
    
    if serial_results == async_results:
        print("Calculations returned the same results for both async and serial functions!")
    else:
        print("Calculations returned different results between serial and async functions...")
    
    


