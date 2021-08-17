# UniprotScraper

UniprotScraper is a web scraping tool that specialized for Uniprot Database. It requires only
the uniprot entry number of relevant protein. The included methods can return the fasta file,
only the header, only the sequence, first three, five and ten amino acids of protein.

## Installation

with pip:

```bash
pip install UniprotScraper
```

## Requirements

Uniprotscraper uses some modules that need to be installed to your system;

1) bs4(BeautifulSoup)
2) urllib.request
3) urllib.error

with pip:

```bash
pip install bs4
```

```bash
pip install urllib.request
```

```bash
pip install urllib.error
```

## Usage

Get FASTA file of protein that entered Uniprot Entry Number,

Input:
```python
import bs4
import urllib.request
from urllib.error import HTTPError, URLError
import UniprotScraper as us

fasta = us.get_with_header("P04418")
print(fasta)
```

Output:
```python
>sp|P04418|END5_BPT4 Endonuclease V OS=Enterobacteria phage T4 OX=10665 PE=1 SV=1
MTRINLTLVSELADQHLMAEYRELPRVFGAVRKHVANGKRVRDFKISPTFILGAGHVTFF
YDKLEFLRKRQIELIAECLKRGFNIKDTTVQDISDIPQEFRGDYIPHEASIAISQARLDE
KIAQRPTWYKYYGKAIYA
```
Get only the protein sequence,

Input:
```python
sequence = us.get_without_header("P04418")
print(sequence)
```

Output:
```python
MTRINLTLVSELADQHLMAEYRELPRVFGAVRKHVANGKRVRDFKISPTFILGAGHVTFF
YDKLEFLRKRQIELIAECLKRGFNIKDTTVQDISDIPQEFRGDYIPHEASIAISQARLDE
KIAQRPTWYKYYGKAIYA
```

Get only the header of FASTA file,

Input:
```python
header = us.get_only_header("P04418")
print(header)
```

Output:
```python
>sp|P04418|END5_BPT4 Endonuclease V OS=Enterobacteria phage T4 OX=10665 PE=1 SV=1
```

Get first three amino acids,

Input:
```python
three_aa = us.get_first_three_aa("P04418")
print(three_aa)
```

Output:
```python
MTR
```

Get first five amino acids,

Input:
```python
five_aa = us.get_first_five_aa("P04418")
print(five_aa)
```

Output:
```python
MTRIN
```

Get first ten amino acids,

Input:
```python
ten_aa = us.get_first_ten_aa("P04418")
print(ten_aa)
```

Output:
```python
MTRINLTLVS
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
