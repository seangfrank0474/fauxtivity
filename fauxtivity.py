#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fauxtivity

import configparser
import requests
import sys
from os import startfile
from pyautogui import alert, hotkey, moveTo, moveRel, PAUSE, press, scroll, write 
from random import randrange, shuffle
from re import findall
from time import sleep
from webbrowser import open_new_tab

def who_dat_mousey_moven():
    print("MOUSE MOVING FUNCTION")
    for i in range(20):
        moveTo(randrange(0, 1000), randrange(0, 1000), duration=2)
        scroll(randrange(-10, 10))
        sleep(randrange(1, 10, 2))
        moveRel(randrange(0, 1000), randrange(0, 1000), duration=2)
        scroll(randrange(-10, 10))
        sleep(randrange(1, 10, 2))

def who_dat_web_browsen(browse_dat_thing):        
    print("WEB BROWSING FUNCTION")
    requests.packages.urllib3.disable_warnings()
    faux_scrape_url = browse_dat_thing
    faux_scrape_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    faux_request_response = requests.get(faux_scrape_url, headers=faux_scrape_headers, verify=False)
    faux_response_text = faux_request_response.text
    faux_response_url_list = findall('href\=\"(http\S+)\"', faux_response_text)
    faux_response_len = len(faux_response_url_list) - 1
    sleep(randrange(10, 60, 3))   
    open_new_tab(faux_scrape_url)    
    sleep(randrange(10, 60, 3))
    press('pagedown', randrange(1, 5))
    sleep(randrange(10, 60, 3))
    for i in range(10):
        open_new_tab(faux_response_url_list[randrange(0, faux_response_len)])
        sleep(randrange(10, 60, 3))
        press('pagedown', randrange(1, 5))
        sleep(randrange(10, 60, 3))
        hotkey('ctrl', 'w')
    sleep(randrange(10, 60, 3))
    hotkey('ctrl', 'w')
    
def who_dat_googlen(google_dat_thing):
    print("GOOGLE SEARCH FUNCTION")
    requests.packages.urllib3.disable_warnings()
    faux_scrape_url = google_dat_thing
    faux_scrape_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    faux_request_response = requests.get(faux_scrape_url, headers=faux_scrape_headers, verify=False)
    faux_response_text = faux_request_response.text
    faux_response_url_list = findall('href\=\"(http\S+)\"', faux_response_text)
    faux_response_len = len(faux_response_url_list) - 1
    sleep(randrange(10, 60, 3))   
    open_new_tab(faux_scrape_url)    
    sleep(randrange(10, 60, 3))
    press('pagedown', randrange(1, 5))
    sleep(randrange(10, 60, 3))
    for i in range(10):
        open_new_tab(faux_response_url_list[randrange(0, faux_response_len)])
        sleep(randrange(10, 60, 3))
        press('pagedown', randrange(1, 5))
        sleep(randrange(10, 60, 3))
        hotkey('ctrl', 'w')
    sleep(randrange(10, 60, 3))
    hotkey('ctrl', 'w')
    
def who_dat_typen(typen_dat_thing, faux_typing_file):
    print("KEYBOARD TYPING FUNCTION")
    with open(typen_dat_thing, encoding='utf-8') as write_from_logging:
        startfile(faux_typing_file)
        sleep(10)
        write(write_from_logging.read(), interval = 0.07)
    hotkey('alt', 'f4')
    press('enter')
    with open(faux_typing_file, 'w'):
        pass
    
def main(faux_config):
    try:
        faux_search_path = faux_config['SEARCHTERMS']['faux_search']
        faux_search_engine = faux_config['SEARCHTERMS']['faux_search_engine']
        faux_url_path = faux_config['WEBBROWSING']['faux_url']
        faux_typing_list = faux_config['TYPINGTEXT']['faux_text'].split()
        faux_typing_file = faux_config['TYPINGTEXT']['faux_type_to']
        faux_funk = ['mouse', 'browser', 'google', 'type']
        with open(faux_search_path, encoding='utf-8') as path_list_read:
            faux_search_list = path_list_read.read().splitlines()
        with open(faux_url_path, encoding='utf-8') as path_list_read:
            faux_url_list = path_list_read.read().splitlines()         
        while True:
            print("MAIN SCRIPT FUNCTION")
            PAUSE = randrange(3, 6)
            shuffle(faux_funk)
            for faux_list_result in faux_funk:
                sleepytime = randrange(120, 600, 6)
                if faux_list_result == 'mouse':
                    who_dat_mousey_moven()
                elif faux_list_result == 'browser':
                    f_web_len = len(faux_url_list) - 1
                    f_web_rand = randrange(0, f_web_len)
                    browse_dat_thing = faux_url_list[f_web_rand]
                    # print('BROWSER FUNCTION -\n    Variables that will be pass to the function-\n        URL Browse: {0}\n        Browser List: {1}\n        Browse Len: {2}\n        Browse Rand: {3}'.format(browse_dat_thing, faux_url_list, f_web_len, f_web_rand))
                    who_dat_web_browsen(browse_dat_thing)
                elif faux_list_result == 'google':
                    f_srch_len = len(faux_search_list) - 1
                    f_srch_rand = randrange(0, f_srch_len)
                    google_dat_thing = '{0}{1}'.format(faux_search_engine, faux_search_list[f_srch_rand]) 
                    # print('GOOGLE FUNCTION -\n    Variables that will be pass to the function-\n        Search Terms: {0}\n        Search Engine: {1}\n        Search List Len: {2}\n        Search #Rand List: {3}\n        Search All Together: {4}'.format(faux_search_list, faux_search_engine, f_srch_len, f_srch_rand, google_dat_thing))
                    who_dat_googlen(google_dat_thing)
                elif faux_list_result == 'type':
                    f_type_len = len(faux_typing_list) - 1
                    f_type_rand = randrange(0, f_type_len)
                    typen_dat_thing = faux_typing_list[f_type_rand]
                    # print('TYPE FUNCTION -\n    ariables that will be pass to the function-\n        Type List: {0}\n        Type Text: {1}\n        Type List Len: {2}\n        Type Rand: #{3}\n        Type To File: {4}'.format(faux_typing_list, typen_dat_thing, f_type_len, f_type_rand, faux_typing_file))
                    who_dat_typen(typen_dat_thing, faux_typing_file)
                else:
                    pass
                print("Sleeping for: {0} seconds".format(sleepytime))
                sleep(sleepytime)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    faux_config = configparser.ConfigParser()
    faux_config.read('faux.ini')
    sleep(5)
    try:
        faux_configured = faux_config['CONFIGURED']['faux_configured']
        if faux_configured == 'False':
            alert('Fauxtivity is not configured or the configuration value has not been set to True.\n\nPlease configure the faux.ini file and run the application again.')
            sys.exit(1)
        elif faux_configured == 'True':
            main(faux_config)
        else:
            alert('Not sure what happened!\n\nPlease check the faux.ini file to make sure it is configured correctly!')
            sys.exit(2)
    except Exception as e:
        print(e)