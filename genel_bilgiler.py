import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import httpx
import asyncio
import json
import random
df = pd.read_csv(r'C:\Users\şerefcanmemiş\Documents\projects_2\puplica\program_ids.csv')
id_list  = list(df.Column1)


# universite ve bolum id parametreleri
    
sem = asyncio.Semaphore(5)
async def fetch(client, sem, url):
    async with sem:
        response = await client.get(url)
        if response.status_code != 200:
            raise Exception(f"Request failed with status {response.status_code}")
        return response.text
            
def parse_html(html_content):
    program_info = {}
    soup = BeautifulSoup(html_content.replace("---", "0"), 'html.parser')
    tables = soup.find_all('table', {'class':'table table-bordered'})
    program_info["Bölüm Adı"] = tables[0].find('th').text
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 2:
                key = cols[0].get_text(strip=True).replace('*','')
                value =cols[1].get_text(strip=True).replace('*','')
                program_info[key] = value
    return program_info

async def fetch_chunked(id_list, chunk_size):
    all_data = []
    sem = asyncio.Semaphore(5)
    async with httpx.AsyncClient(verify=False) as client:
        for i in range(0, len(id_list), chunk_size):
            chunk = id_list[i:i+chunk_size]
            tasks = [fetch(client, sem, f"https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={url}")
                    for url in chunk]
            results = await asyncio.gather(*tasks)
            parsed_data = [parse_html(html) for html in results]
            all_data.extend(parsed_data)
            print(f"Chunk {i//chunk_size + 1} tamamlandı, {len(parsed_data)} sayfa çekildi.")
            await asyncio.sleep(3 + random.uniform(0,2))
    return all_data
parsed_data = asyncio.run(fetch_chunked(id_list, 100))

with open ("C:\\Users\\şerefcanmemiş\\Documents\\projects_2\\puplica\\yokatlas_data.json", 'w', encoding='utf-8') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=3)
    





