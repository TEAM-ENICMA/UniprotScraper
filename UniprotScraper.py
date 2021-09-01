import requests

#__co-authors__: Team_Enicma; Bilgehan Nevruz, Melih Temel, Umut Durak, Özgür Can Arıcan
#__contact__: www.github.com/TEAM-ENICMA, teamenicma@gmail.com
#__version__: UniprotScraper 0.2

def __scraping_uniprot(UniEntryNumber):
    link = "https://www.uniprot.org/uniprot/" + UniEntryNumber + ".fasta"
    try:
        url = requests.get(link)
    except:
        text = "ERROR: No network connection! Please check your internet connection"
        return text
    else:
        text = url.text
        if text[:3] == ">sp":
            return text
        else:
            text = "ERROR: Page not found! Please check your 'Uniprot Entry Number"
            return text

def get_with_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    return content

def get_without_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    return "\n".join(content.splitlines()[1:])

def get_only_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    return content.splitlines()[0]

def get_first_three_aa(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    return content.splitlines()[1][:3]

def get_first_five_aa(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    return content.splitlines()[1][:5]

def get_first_ten_aa(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    return content.splitlines()[1][:10]

def get_aa_content(UniprotEntryNumber):
    content = __scraping_uniprot(UniprotEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        sequence = "\n".join(content.splitlines()[1:])
        aa_dict = dict()
        for a in sequence:
            aa_dict[a] = aa_dict.get(a, 0) + 1
        return aa_dict
