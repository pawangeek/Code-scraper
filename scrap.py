import requests,os, re,time
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool
from random import random, seed
from check_repeat import check_lines
from reduce_lang import get_req_langs, get_all_links, build_df, get_lang

counts = 100

while (counts!=200):

    links_page_result = requests.get('https://ideone.com/recent')
    links_page_content = links_page_result.content
    links_page_soup = BeautifulSoup(links_page_content, 'html.parser')
    ul_of_links = links_page_soup.find("div", {"class": "span8"})

    req_languages = ul_of_links.find_all('span', text=True)
    languages = get_req_langs(req_languages)

    list_of_href = get_all_links(ul_of_links)
    print(len(list_of_href))

    links_of_href = build_df(list_of_href, languages)
    print(len(links_of_href))

    new_links = check_lines(links_of_href)
    print(len(new_links))

    cd = os.getcwd()

    a = ['1 7']
    b = ['104 96 50']
    c = ['333333336 142857144']
    d = ['6 7 8']
    e = ['6']

    for code_link in new_links:
    
        p = []
    
        code_link_req = requests.get(code_link)
        disease_soup = BeautifulSoup(code_link_req.content, 'html.parser')
        lang = get_lang(disease_soup)

        print(lang)
    
        output = disease_soup.find("pre", {"id": "output-text"})
        p.append(output.text.strip())    
        p = [x.replace('\n', ' ') for x in p]
    
        if (p == d or p==a or p==b or p==c or p==e):
        
            if p == a:
                num = 'a'
            elif p == b:
                num = 'b'
            elif p == c:
                num = 'c'
            elif p == d:
                num = 'd'
            elif p == e:
                num = 'e'
            
            rand = random()
                   
            cnt = []
        
            code = disease_soup.find("pre", {"class": "source"})             
            name = code.find('ol')
        
            directory = lang       
            path = os.path.join(cd, directory)
        
            try:
                os.mkdir(path)
            except FileExistsError:
                print('Directory {} already exists'.format(path))
            else:
                print('Directory {} created'.format(path))
               
            for ul in name:
                cnt.append(ul.text)
            
            if lang=='python3' or lang=='python3nbc':
                lang='py'
            elif lang=='c++14' or lang=='c++':
                lang='cpp'
               
            cname = os.path.join(path, "%s"%(num)+"_%f"%(rand)+".%s"%(lang))
        
            with open(cname, 'w') as f:
                for item in cnt:
                    f.write("%s\n" % item)
    
            f.close

    time.sleep(20)
    counts+=1