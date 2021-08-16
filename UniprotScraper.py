import bs4
import urllib.request
from urllib.error import HTTPError, URLError

#__co-authors__: Team_Enicma; Bilgehan Nevruz, Melih Temel, Umut Durak, Özgür Can Arıcan
#__contact__: www.github.com/TEAM-ENICMA, teamenicma@gmail.com
#__version__: UniprotScraper v_1.0

def __scraping_uniprot(UniEntryNumber):
    link = "https://www.uniprot.org/uniprot/" + UniEntryNumber + ".fasta"
    try:
        url = urllib.request.urlopen(link).read()
    except HTTPError:
        text = "HTTP_ERROR: Page not found!\nPlease check your 'Uniprot Entry Number'"
    except URLError:
        text = "URL_ERROR: No network connection!\n Please check your internet connection"
    else:
        scrape = bs4.BeautifulSoup(url, "lxml")
        text = scrape.get_text()
    return text

def get_with_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    return content

def get_without_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:4] == "HTTP" or content[:4] == "URL_":
        return content
    return "\n".join(content.splitlines()[1:])

def get_only_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:4] == "HTTP" or content[:4] == "URL_":
        return content
    return content.splitlines()[0]

def get_first_three_aa(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:4] == "HTTP" or content[:4] == "URL_":
        return content
    return content.splitlines()[1][:3]

def get_first_five_aa(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:4] == "HTTP" or content[:4] == "URL_":
        return content
    return content.splitlines()[1][:5]

def get_first_ten_aa(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:4] == "HTTP" or content[:4] == "URL_":
        return content
    return content.splitlines()[1][:10]
