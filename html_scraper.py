"""
    Author: Perucy Mussiba
    Date: August 2024
    Project: VulGPT
    Purpose: Scrape HTML pages
"""

from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from urllib.parse import urlparse
import html2text
from bs4 import BeautifulSoup

"""
    Gets the markdown for a webpage and creates a metadata field for each page
    
    Args:
        url (string): URL of the webpage
        
    Returns:
        text (string): Text of the webpage
        metadata (dict): Dictionary of metadata about the webpage
        
"""
def get_html_to_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/536.36 ('
                                              'KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})

    try:
        response = urlopen(req)
        html = response.read().decode("utf-8")
        if response.getcode() == 401:  # Unauthorized
            return "error", url
        elif response.getcode() == 403:  # Forbidden
            return "error", url
    except HTTPError as e:
        if e.code == 401 or e.code == 403:
            return "error", url
        return "error", url
    except URLError as e:
        return "error", url
    except Exception as e:
        return "error", url

    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()

    html = str(soup)
    html2text_instance = html2text.HTML2Text()
    html2text_instance.images_to_alt = True
    html2text_instance.body_width = 0
    html2text_instance.single_line_break = True
    text = html2text_instance.handle(html)

    try:
        page_title = soup.title.string.strip()
    except:
        parsed_url = urlparse(url)
        page_title = parsed_url.path[1:].replace("/", "-")
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    if meta_description:
        description = meta_description.get('content')
    else:
        description = page_title

    if meta_keywords:
        meta_keywords = meta_keywords.get('content')
    else:
        meta_keywords = ""

    metadata = {'title': page_title,
                'url': url,
                'description': description,
                'keywords': meta_keywords}

    return text, metadata