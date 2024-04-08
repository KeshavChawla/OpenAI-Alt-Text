#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

random.seed(10)
empty_alt_text = []
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
    df_list = []

    for url in urls:    
        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                img_tags = soup.find_all('img')

                # # uncomment for DEBUG
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


                row_dict = {"total_images": num_imgs,
                            "compliant_imgs": num_alt_texts,
                            "compliant_imgs_pct": round(float(num_alt_texts) / float(num_imgs) * 100,0),
                            "empty_alt_text": num_empty_alt_text,
                            "compliant": False}

                if print_alt_texts:
                    print(f"On {url}, there were {num_imgs} images and {num_alt_texts} alt-texts, {num_empty_alt_text} of which were empty. {row_dict['compliant_imgs_pct']}% of images on this page were compliant (have an alt-text).")
                
                
                if num_alt_texts == num_imgs:
                    row_dict["compliant"] = True
                else:
                    print(f"NON-COMPLIANT! {url}")

                df_list.append(row_dict)

                # gather empty alt text urls and image source
                for i, alt_text in enumerate(all_alt_texts):
                    if alt_text == "":
                        empty_alt_text.append({"url": url, "image_src": img_tags[i]['src']})


        except Exception as e:
            continue   

    df = pd.DataFrame(df_list)
    df.to_csv("output.csv", index=False)

    total_num_urls = len(df.index)
    total_num_compliant_urls = len(df[df["compliant"] == True].index) 
    total_num_imgs = df["total_images"].sum()
    total_num_compliant_imgs = df["compliant_imgs"].sum()
    total_num_empty_alt_text = df["empty_alt_text"].sum()

    print(f"There are {len(urls)} links, {total_num_urls} of which we examined.")
    print(f"Across all {total_num_urls} websites, {float(total_num_compliant_urls) / float(total_num_urls) * 100}% of urls were compliant.")
    print(f"Within all {total_num_imgs} images across {total_num_urls} websites, {round(float(total_num_compliant_imgs * 100) / float(total_num_imgs))}% of images were compliant.")      
    print(f"Within all {total_num_imgs} images across {total_num_urls} websites, {round(float(total_num_empty_alt_text * 100) / float(total_num_imgs))}% of images were had empty alt-text.")      


if __name__ == "__main__":         
    links = get_ca_govt_links()
    alt_text_prevalence(links, False)

    start, end = 0, len(empty_alt_text) - 1

    for i in range(30):
        random_num = random.randint(start, end)
        print(empty_alt_text[i])