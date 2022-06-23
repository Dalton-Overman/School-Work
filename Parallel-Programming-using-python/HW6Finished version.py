# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 00:45:20 2020

@author: Dalton
"""

import requests, os, bs4
import concurrent.futures
import time
import asyncio
import aiohttp
import nest_asyncio

nest_asyncio.apply()


def get_urls():
    urls = []
    url = 'https://xkcd.com' # starting url
    for page in range(1,25): 
        # Download the page.
        if page == 404: #404 is not valid number
            continue
        pageURL= url + "/" + str(page)
        print('Downloading page %s...' % pageURL)
        res = requests.get(pageURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')   
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            urls.append(comicUrl)
    return(urls)
    
def download_image(url):
    file_name = url.split('/')[-1]
    #download?
    print('Downloading image %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()
    with open('serial_XKCD_download/' + file_name, 'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


async def download_site_async(session, url):
    async with session.get(url):
        file_name_async = url.split('/')[-1]
        print('Downloading image %s...' % (url))
        res = requests.get(url)
        res.raise_for_status()

        with open('asynchronous_XKCD_download/' + file_name_async, 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

async def download_all_sites_async(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site_async(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)  

def threaded_download(url):
    file_name = url.split('/')[-1]
    #download?
    print('Downloading image %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()
    with open('multithreading_XKCD_download/' + file_name, 'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

def multip_download(url):
    file_name = url.split('/')[-1]
    #download?
    print('Downloading image %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()
    with open('multiprocessing_XKCD_download/' + file_name, 'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size



if __name__ == '__main__':
    cd=os.getcwd()
    
    path='serial_XKCD_download/'
    os.mkdir(path)
    Urls = get_urls()
    

    starting_time = time.time()
    for i in range(len(Urls)):
        url = Urls[i]
        download_image(url)
    serial_time= time.time()-starting_time
    serial_size = (get_size(path))
    
    path='asynchronous_XKCD_download/'
    os.mkdir(path)
    starting_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites_async(Urls))
    async_time= time.time()-starting_time
    async_size = (get_size(path))
    
    max = os.cpu_count()
    
    path='multithreading_XKCD_download/'
    os.mkdir(path)
    starting_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers = max) as executor:
        executor.map(threaded_download, Urls)
    threaded_time= time.time()-starting_time
    threaded_size = (get_size(path))
    
    path='multiprocessing_XKCD_download/'
    os.mkdir(path)
    starting_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers = max) as executor:
        executor.map(multip_download, Urls)
    multip_time = time.time()-starting_time
    multip_size = (get_size(path))
    
    print('\n')
    print(f'Serial downloading took {serial_time}')
    print(f'Asynchronous downloading took {async_time}')
    print(f'Multithreading downloading took {threaded_time}')
    print(f'Multiprocessing downloading took {multip_time}')

    print('\n')    

    print(f'The serial download was {serial_size} bytes')
    print(f'The asynchronous download was {async_size} bytes')
    print(f'The multithreading download was {threaded_size} bytes')
    print(f'The multiprocessing download was {multip_size} bytes')
    
    print('\n')
    
    if serial_size == async_size == threaded_size == multip_size:
        print("All functions downloaded the same files successfully!")
    else:
        print('There was an error and the files were not all the same...')
    
    print('\n')
        
    print(f'If you would like to run this program again in the future please delete the four created subdirectories within {cd}')