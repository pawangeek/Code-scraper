import requests, os, re
import pandas as pd

def get_req_langs(languages):
    all_langs = []

    y = 3
    for i in languages:
        if y%3==0:
        
            clean = re.compile('<.*?>')
            at = re.sub(clean, '', str(i))
            all_langs.append(at)
    
        y+=1  
    
    return(all_langs[:-1])

def get_all_links(ul_of_links):

    list_of_a_tags = ul_of_links.find_all('a')
    list_of_a_tags = list_of_a_tags[:-7]

    list_of_href = [link.attrs['href'] for link in list_of_a_tags]
    list_of_href = ['https://ideone.com/' + link for link in list_of_href]

    return (list_of_href)

def build_df(list_of_href, all_langs):

    links_data = pd.DataFrame({'link' : list_of_href,'language' : all_langs})
    imp_langs = ['C++14', 'C++', 'Java', 'Python 3', 'Python 3 nbc']
    links_of_data = links_data[links_data.language.isin(imp_langs)]

    return(links_of_data['link'].tolist())

def get_lang(disease_soup):

    sections = disease_soup.find("div", {"class": "span3"})
    lang = sections.text.strip()
    lang = "".join(lang.split())
    lang = (re.sub(r'\([^)]*\)', '', lang)).lower()

    return(lang)