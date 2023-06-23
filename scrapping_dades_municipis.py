# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:28:16 2023

@author: charl
"""

import requests
import pandas as pd

# Fem un request a la pàgina on tenim la informació que ens interessa:
url = 'https://llengua.gencat.cat/ca/serveis/dades_i_estudis/poblacio/catala947/'
response = requests.get(url)
html_content = response.content
print(html_content)

# Utilitzem els pandas per passar la informació de l'HTML a dataframe:
dfs = pd.read_html(html_content)

# Concatenem tots els dataframes de la llista que acabem de crear:
df = pd.concat(dfs)

# Ho guardem en un fitxer CSV:
df.to_csv('municipis_comarques_at.csv', index=False)
