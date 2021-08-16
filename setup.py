from distutils.core import setup
import setuptools
setup(
  name = 'UniprotScraper',         
  packages = ['UniprotScraper'],   
  version = '0.1',     
  license='MIT',        
  description = 'UniprotScraper is a web scraper tool that specialized for Uniprot Database.',
  author = 'team_enicma',                  
  author_email = 'teamenicma@gmail.com',      
  url = 'https://github.com/TEAM-ENICMA/UniprotScraper',
  download_url = 'https://github.com/TEAM-ENICMA/UniprotScraper/archive/refs/tags/v_1.0.tar.gz',
  keywords = ['Python', 'Bioinformatics', 'WebScraping', 'ComputationalBiology', 'Uniprot'],
  install_requires=[
          'bs4',
          'urllib.request',
          'urllib.error'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
