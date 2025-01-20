# OpenAI Alt-Text Chrome Extension
Using OpenAI's GPT4-Vision-Preview to Add Alt-Text to Images Missing Them &amp; Increasing Web Accessibility

[![Chrome Web Store Screenshot of Published Chrome Extension](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/21203253/55f01370-4964-4929-9e88-acc7cc89b788)](https://chromewebstore.google.com/detail/alt-text-filler/lhjopjegmkjjljgealjmckdblmmekjki)


## Loading the Chrome Extension through the Google Chrome Web Store
1. Visit [https://chromewebstore.google.com/detail/alt-text-filler/lhjopjegmkjjljgealjmckdblmmekjki](https://chromewebstore.google.com/detail/alt-text-filler/lhjopjegmkjjljgealjmckdblmmekjki) and 
2. Click "Add to Chrome"
3. From the Extensions dropdown in chrome pin the extension and open the extension's menu to add your OpenAI API Key (see the section below on obtaining a key if you do not have one)

![Chrome Extension Drop Down Menu Options and Entry Box to Add OpenAI API Key](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/21203253/d5092b79-5759-49c5-9cf9-6a340f06ed8c)

## Loading the Chrome Extension Locally
1. Go to [chrome://extensions](chrome://extensions)
2. Turn on the Developer mode switch in the upper right
3. Click on "Load unpacked"
4. Select the alt-text folder within our repo

## Obtaining and Loading an OpenAI API Key
1. Visit [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) and sign up/log in
2. Generate a new API key with (at minimum) model capabilities access (we specifically need /v1/chat/completions)
3. Copy and paste the new API key into the Chrome extension toolbar/settings pane and save

---

## Survey and Anonymized Results
[![Screenshot of a survey of different alt-text provided by OpenAI's GPT 4 Vision Preview, ChatGPT 4, and existing alt-text](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/21203253/cb695f0a-4a1a-4aca-a48d-ed63b16d9ba8)](https://forms.gle/1poeXuf556G8oz6P6)

The survey our team conducted to assess whether responses generated by OpenAI's GPT4 Vision Preview and ChatGPT 4 were any bit comparable to existing alt-text can be found here [https://forms.gle/1poeXuf556G8oz6P6](https://forms.gle/1poeXuf556G8oz6P6)

Anonymized results of the survey can be found in this repo under the [survey folder](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/blob/main/survey/CS_492_Alt_Text_Survey_Anonymized.xlsx).

## Canadian Govermental Website Analysis
Another component of research conducted was regarding the compliance of Canadian governmental websites' compliance with WCAG 2.0, a legal requirement as of 2011. Research based on our small-scale, non-intrusive polling of websites to determine the lack of existing alt-text can be found in the [research](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/tree/main/research) folder along with the [code](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/blob/main/research/webscrape.py) and the [raw data results](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/blob/main/research/output.csv).

In total, we examined 75 websites. We deem “compliant images” to be those that have an alt tag (even if empty), and “compliant websites” to be those where all images are compliant. We collected the following statistics:
* Across all 75 websites, 88.0% of URLs were compliant.
* Within all 1133 images across 75 websites, 96% of images were compliant.
* Within all 1133 images across 75 websites, 44% of images had empty alt-text.

However, there was a reasonable assumption that our webscraper may be overcounting the number of compliant images because our webscraper's definition of compliance is limited. Namely, it has the following shortcomings:
* Only decorative images are allowed to have empty alt text. Our webscraper didn't check whether or not images with empty alt text were decorative in nature. Thus, it would incorrectly identify non-decorative images with empty alt text as compliant.
* Images with non-empty alt text must have adequately descriptive alt text. Our webscraper didnt' check whether this was true, and thus would have incorrectly identified non-empty images that weren't adequately descriptive as compliant.
Automating checking for these qualities is difficult, and so we sought to estimate the error of our webscraper by analyzing a sample by hand. We randomly sampled 60 images (30 with an empty alt text, 30 with a non-empty alt text) among all images our webscraper identified as compliant. For each of these 60 images, we manually verified whether or not our webscraper correctly identified compliant images based on the additional requirements for compliance (images with empty alt text must be decorative, and non-empty alt text must be adequately descriptive). In our sample, we saw a few examples of noncompliance that weren't captured by our webscraper, namely inadequately descriptive alt texts:

   The image below had an alt-text attribute of “Nicholas Forget tile”.
  
  ![unnamed (1)](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/18638226/ad9f8465-bf73-40ed-b95a-bebd6b74e78a)

  This image below had an alt-text attribute of "tab-1".
  ![unnamed (2)](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/18638226/30eabb3a-e99e-4a05-90df-7a9b0401a53c)

  This image below had an alt-text attribute of "play-icon", suggesting it was something named for/by developers.
  ![unnamed (4)](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/18638226/ff6b50ea-c8f5-4ee8-8434-608bda046715)


Among the sample of 60 images, 90% of the images we looked at use alt-text attributes correctly. To determine the accuracy of our web scraper, we created a binomial confidence interval (with our calculations below). The $z$-score that we chose was 1.96 (that corresponds to the 95% confidence interval). With $\hat{p} = \frac{54}{60}$ and $n = 60$, we plugged it into the formula below to calculate our interval.    


![unnamed](https://github.com/KeshavChawla/CS492-OpenAI-Alt-Text/assets/18638226/dac99f8e-5a01-4069-9990-578201935e5b)

   We calculated the 95% binomial confidence interval for the accuracy of our web scraper to be [82.4%, 97.6%]. Given our webscraper's original estimate of 96% compliance among all images, we are 95% confident that, after accounting for the error of our web scraper, 79.1% to 93.6% of images on Canadian governmental websites follow WCAG 2.0 guidelines.
