#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def get_ca_govt_links():
    url = "https://www.canada.ca/en/government/dept.html"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # get all hyperlinks
        # NOTE: not sure if these links are necessarily all govt links
        links = soup.select('a')

        hrefs = []
        for link in links:
            href = link['href']
            if href.startswith('https://'):
                hrefs.append(href)

        return hrefs
    raise Exception("No links!")


def alt_text_prevalence(urls,print_alt_texts=True):
    total_num_urls = 0
    total_num_compliant_urls = 0 # compliant = for every img tag, there is an alt-text (even if empty)
    total_num_imgs = 0 # across all websites
    total_num_compliant_imgs = 0 # across all websites

    for url in urls:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                img_tags = soup.find_all('img')

                # for tag in img_tags:
                #     print(f"IMG TAG: {tag}")
                
                # can we find a way to differentiate information pics (require non-empty alt-text) vs. decoration pics (use empty alt-text)?
                
                all_alt_texts = [img.get('alt', None) for img in img_tags]
                
                if print_alt_texts:
                    print(all_alt_texts)
                
                num_imgs = len(all_alt_texts)

                valid_alt_texts = [alt for alt in all_alt_texts if alt is not None]

                num_alt_texts = len(valid_alt_texts)
                num_empty_alt_text = len([alt for alt in valid_alt_texts if alt == ""])

                print(f"On {url}, there were {num_imgs} images and {num_alt_texts} alt-texts, {num_empty_alt_text} of which were empty. {float(num_alt_texts) / float(num_imgs) * 100}% of images on this page were compliant (have an alt-text).")
                
                total_num_imgs += num_imgs
                total_num_compliant_imgs += num_alt_texts

                if num_alt_texts == num_imgs:
                    total_num_compliant_urls += 1
                total_num_urls += 1
            # else:
            #     print(f"Failed to retrieve the webpage {url}")
        except Exception as e:
            # print(e)
            # print(f"Failed to call requests.get({url})")
            continue      
    print(f"Across all {total_num_urls} websites, {float(total_num_compliant_urls) / float(total_num_urls) * 100}% of urls were compliant.")
    print(f"Within all {total_num_imgs} images across {total_num_urls} websites, {float(total_num_compliant_imgs * 100) / float(total_num_imgs)}% of images were compliant.")      

            
links = get_ca_govt_links()
print(f"There are {len(links)} links")
alt_text_prevalence(links, False)

