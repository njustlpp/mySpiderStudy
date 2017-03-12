import requests
import re


def downloadurl(url):
    print "DownLoad " + url
    html = requests.get(url)
    return html.text


def getlinks(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


def crawer(seedurl):
    crawerqueue = [seedurl]
    seen = set(crawerqueue)  # keep track which URL's have seen before

    while crawerqueue:
        url = crawerqueue.pop()
        html = downloadurl(url)
        links = getlinks(html)
        for link in links:
            link.encode('utf-8')
            print link
            if link not in seen:
                seen.add(link)
                crawerqueue.append(link)


if __name__ == "__main__":
    seed_url = "http://www.sohu.com/" #种子网站
    crawer(seed_url)
