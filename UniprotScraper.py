import requests

#__co-authors__: Team_Enicma; Bilgehan Nevruz, Melih Temel, Umut Durak, Ozgur Can Arican
#__contact__: www.github.com/TEAM-ENICMA, teamenicma@gmail.com
#__version__: UniprotScraper 0.3

def __scraping_uniprot(UniEntryNumber):
    link = "https://www.uniprot.org/uniprot/" + UniEntryNumber + ".txt"
    try:
        url = requests.get(link)
    except:
        text = "ERROR: No network connection! Please check your internet connection"
        return text
    else:
        text = url.text
        if text[:2] == "ID":
            return text.splitlines()
        else:
            text = "ERROR: Page not found! Please check your 'Uniprot Entry Number"
            return text

def get_identification(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        ident = []
        for line in content:
            if line[:2] == "ID":
                ident.append(line)
        return "\n".join(ident)
        
def get_accession(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        acc = []
        for line in content:
            if line[:2] == "AC":
                acc.append(line)
        return "\n".join(acc)

def get_date(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        date = []
        for line in content:
            if line[:2] == "DT":
                date.append(line)
        if date == []:
            error = "The protein does not have a creation or modification date!"
            return error
        return "\n".join(date)

def get_description(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        desc = []
        for line in content:
            if line[:2] == "DE":
                desc.append(line)
        if desc == []:
            error = "The protein does not have a description!"
            return error
        return "\n".join(desc)

def get_species(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        spec = []
        for line in content:
            if line[:2] == "OS":
                spec.append(line)
        if spec == []:
            error = "The protein does not have an organism species!"
            return error
        return "\n".join(spec)

def get_classification(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        clas = []
        for line in content:
            if line[:2] == "OC":
                clas.append(line)
        if clas == []:
            error = "The protein does not have an organism classification!"
            return error
        return "\n".join(clas)

def get_taxonomy_ref(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        tax = []
        for line in content:
            if line[:2] == "OX":
                tax.append(line)
        if tax == []:
            error = "The protein does not have an organism taxonomy cross-reference!"
            return error
        return "\n".join(tax)

def get_information(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        info = []
        for line in content:
            if line[:2] == "CC":
                info.append(line)
        if info == []:
            error = "The protein does not have any free text comments or informations!"
            return error
        return "\n".join(info)

def get_seq_header(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        head = []
        for line in content:
            if line[:2] == "SQ":
                head.append(line)
        return "\n".join(head)

def get_sequence(UniEntryNumber):
    content = __scraping_uniprot(UniEntryNumber)
    if content[:5] == "ERROR":
        return content
    else:
        seq = []
        for line in content:
            if line[:2] == "  ":
                seq.append(line)
        string_seq = "".join(seq)
        return string_seq.replace(" ", "")

def get_first_three_aa(UniEntryNumber):
    entire_seq = get_sequence(UniEntryNumber)
    if entire_seq[:5] == "ERROR":
        return entire_seq
    else:
        return entire_seq[:3]

def get_first_five_aa(UniEntryNumber):
    entire_seq = get_sequence(UniEntryNumber)
    if entire_seq[:5] == "ERROR":
        return entire_seq
    else:
        return entire_seq[:5]

def get_first_ten_aa(UniEntryNumber):
    entire_seq = get_sequence(UniEntryNumber)
    if entire_seq[:5] == "ERROR":
        return entire_seq
    else:
        return entire_seq[:10]

def get_aa_content(UniEntryNumber):
    entire_seq = get_sequence(UniEntryNumber)
    if entire_seq[:5] == "ERROR":
        return entire_seq
    else:
        aa_dict = dict()
        for a in entire_seq:
            aa_dict[a] = aa_dict.get(a, 0) + 1
        return aa_dict
