# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:43:20 2020

@author: Dalton
"""

### Importing libraries ###
from bs4 import BeautifulSoup
import requests
import time
import asyncio
import aiohttp
import nest_asyncio
import os

nest_asyncio.apply()
Current_Direct = os.getcwd()
path_Asynch = 'asynch/'
path_serial = 'serial/'

os.mkdir(path_Asynch)
os.mkdir(path_serial)


def get_urls(urls):
    page = requests.get(urls)
    #soup = BeautifulSoup(page.content, 'html.parser')
    #results = soup.find_all(".txt")
    #start_time1 = time.time()
    #duration1 = time.time() - start_time1

    soup = BeautifulSoup(page.content, 'html.parser')
    results = [i.get("href") for i in soup.find_all('a')]
    #soup.find_all(href = True)
    #<div id="main-content" class="grid_10 push_2">
    #links = [i.get("href") for i in soup.find_all('a', attrs={'class': 'view'})]

    #print(results[55:462])
    #print (len(results))
    resultsReal = results[55:462]
    #print(resultsReal)
    #print(len(resultsReal))
    return resultsReal




    #for i in range(55):
    #    del results[i]
    #print (len(results))
    #print (results)
    #for j in range(407, 420):
    #    del results[j]
    #print(results)
    
    
def append_urls(subdirects):
    baseUrl = "https://www.sec.gov"
    #appendedSubs[len(subdirects)]
    appendedSubs = [baseUrl + i for i in subdirects]
    #print (appendedSubs)
    return appendedSubs


#def get_texts(full_Urls):
    #for i in full_Urls:
        #page = requests.get(full_Urls)
        #soup = BeautifulSoup(page.content, 'html.parser')
        #links = soup.find_all('a')
        #text_links =  [full_Urls + link['href'] for link in links if link['href'].endswith('txt')]
    #print (text_links)







def listFD(url, ext=''):
    page = requests.get(url).text
    base_url = 'https://www.sec.gov'
    #print (page)
    soup = BeautifulSoup(page, 'html.parser')
    return [base_url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]




def list_files(full_Urls): 
    print('Beginning creation of file list, this may take awhile...')
    test_url = "https://www.sec.gov"
    test_ext = "txt"
    file_list = []
    for i in range(len(full_Urls)):
        test_url = full_Urls[i]
        for file in listFD(test_url, test_ext):
            file_list.append(file)
            print(file)
    return file_list
    



async def download_site_async(session, url):
    async with session.get(url) as response:
        #print("Read {0} from {1}".format(response.content_length, url))
        contents = await response.read()
        file_name_async = url.split('/')[-1]
        with open('asynch/' + file_name_async, 'wb') as f:
            f.write(contents)

async def download_all_sites_async(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site_async(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)











if __name__ == '__main__':
    urls = "https://www.sec.gov/Archives/edgar/data/20/"
    

    
    subdirects = get_urls(urls)
    full_Urls = append_urls(subdirects)
    file_list = list_files(full_Urls)
    print ("\n")
    print ("\n")


    #print (file_list)
    

    print ('Beginning asynchronous file downloading')
    print ('Downloading files to "' +str(Current_Direct) +'\\asynch"')
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites_async(file_list))
    duration = time.time() - start_time
    

    print(f"Asynchronous Downloaded {len(file_list)} sites in {duration} seconds")
    
    print ("\n")

    print('Beginning serial file downloading')
    print ('Downloading files to "' + str(Current_Direct) +'\\serial"')
    print("This may take some time...")
    start_time_serial = time.time()
    for i in range(len(file_list)):
        url = file_list[i]
        file_name = url.split('/')[-1]
        r = requests.get(url)
        
        with open('serial/' + file_name, 'wb') as f:
            f.write(r.content)
    duration_serial = time.time() - start_time_serial
    print(f"Serial Downloaded {len(file_list)} sites in {duration_serial} seconds")
    
    print("\n")
    
    print("If you would like to run this again, please delete the directories so it can redownload the files")
    
    
    
    #get_texts(full_Urls)
    
    
    
    #href="/Archives/edgar/data/20/000031506694000681