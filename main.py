import lxml, requests
from bs4 import BeautifulSoup

#1.get_html_file

def get_data(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 "
    }
    # req = requests.get(url, headers)
    #
    # with open("data/coffee_shops.html", "w") as file:
    #     file.write(req.text)

# 2. get_cities_hrefs

    # with open("data/coffee_shops.html") as file:
    #     src = file.read()
    #
    # soup = BeautifulSoup(src, "lxml")
    # figures = soup.find_all("figure", class_="cc-imagewrapper cc-m-image-align-3")
    #
    # for a in figures:
    #     urls = "https://www.dutch-coffeeshops.com/" + a.findNext("a").get("href")
    #     print(urls)
    #
    #     with open("data/cities_urls.txt", "a") as file:
    #         file.write(f"{urls}\n")

# 3. get_data_url_shops

with open("data/cities_urls.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    shop_url_list = []
    for line in lines:
        q = requests.get(line)
        result = q.content
        soup = BeautifulSoup(result, "lxml")
        shop_urls = soup.find_all(class_="cc-imagewrapper cc-m-image-align-3")
        for b in shop_urls:
            shop_url = "https://www.dutch-coffeeshops.com" + b.find("a").get("href")
            shop_url_list.append(shop_url + '\n')
            print(shop_url_list)
        with open("data/coffee_shops_url.txt", "a") as file:
            for line in shop_url_list:
                file.write(line)

get_data("https://www.dutch-coffeeshops.com/")
