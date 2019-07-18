# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time

def scrape_all():
    # Create the exe path for chrome to open chrome page
    # Will open a chrome window
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    print (f'\n-------------------------------------------------------------------------------------\nScraping Started')
    print (f'\n-------------------------------------------------------------------------------------\n')  

    # Visit the site to scrape
    # Will go to the website and extract the browser url
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Find the actual website path we are going to scrape and read/show the data using BeautifulSoup
    news_html = browser.html
    soup = bs(news_html, 'lxml')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    print (f'\n-------------------------------------------------------------------------------------\n')  
    print (f'\nNews Title: {news_title}')
    print (f'\nNews Para: {news_p}')
    print (f'\n-------------------------------------------------------------------------------------\n')  

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Visit the site to scrape
    # Will go to the website and extract the browser url
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    time.sleep(1)

    # Find the actual website path we are going to scrape and read/show the data using BeautifulSoup
    jpl_html = browser.html
    soup = bs(jpl_html, 'lxml')
    #print(soup.prettify())

    image_link = soup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']
    featured_image_url_medium = f'https://www.jpl.nasa.gov{image_link}'

    time.sleep(1)
    full_image_elem = browser.find_by_id("full_image")
    full_image_elem.click()

    time.sleep(1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    html = browser.html
    img_soup = bs(html, 'lxml')

    img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    featured_image_url_large = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    print (f'Featured Image: {featured_image_url_large}')
    print (f'\n-------------------------------------------------------------------------------------\n')  
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Visit the site to scrape
    # Will go to the website and extract the browser url
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(1)

    # Find the actual website path we are going to scrape and read/show the data using BeautifulSoup
    weather_html = browser.html
    soup = bs(weather_html, 'lxml')

    weather_all = soup.find_all('div', class_='js-tweet-text-container')

    weather_list = []
    for x in weather_all:
        y = x.find('p', class_= 'js-tweet-text').text
        if "InSight" in y:
                weather_list.append(y)

    mars_weather = weather_list[0]

    print (f'Mars Weather: {mars_weather}')
    print (f'\n-------------------------------------------------------------------------------------\n')  
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Visit the site to scrape
    # Will go to the website and extract the browser url
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    # Find the actual website path we are going to scrape and read/show the data using BeautifulSoup
    facts_html = browser.html
    soup = bs(facts_html, 'lxml')

    facts_str = pd.read_html(facts_url)

    # https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.to_html.html
    facts_html = facts_str[1].to_html(index = False, header = False)
    #facts_str[1].to_html("facts.html", index = False, header = False)
    
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Visit the site to scrape
    # Will go to the website and extract the browser url
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    # Find the actual website path we are going to scrape and read/show the data using BeautifulSoup
    hemisphere_html = browser.html
    soup = bs(hemisphere_html, 'lxml')

    # Find the links
    image_urls = [(a.text, a['href']) for a in browser.find_by_css('div[class="description"] a')]

    hemisphere_image_urls = []

    for title,url in image_urls:
        temp = {}
        temp['title'] = title
        browser.visit(url)
        img_url = browser.find_by_css('img[class="wide-image"]')['src']
        temp['img_url'] = img_url
        hemisphere_image_urls.append(temp)

    print (f'Dict: {hemisphere_image_urls}')
    print (f'\n-------------------------------------------------------------------------------------\n')  

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    data = {
        "news_title":news_title,
        'news_paragraph':news_p,
        "featured_image":featured_image_url_large,
        "weather":mars_weather,
        "facts_html":facts_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    
    return data

#test = scrape_all()