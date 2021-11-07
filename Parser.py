from typing import List
from bs4 import BeautifulSoup
import requests 
import numpy as np 
import pandas as pd

"""
Logic --> 

function: getHTMLResults 
    ---------------------
    input: num of desired results
    output: list of html results 
    ---------------------
    Loop: for each page (20 results)
        Find each results in page and add to a list
    return List of html results 

function: ParseHTML 
    ---------------------
    input: List of HTML results 
    output: dataframe of housing data
    ---------------------
    create df to store parsed data
        Loop: for each result in page
            Parse HTML to find 
                Price
                Address
                Bedrooms 
                Baths
                    Add all of these to df 
    return df 
"""

class Parser: 
    main_url = "https://www.daft.ie/property-for-sale/dublin-city?pageSize=20&from="

    def __init__(self) -> None:
        pass

    def getHTMLResults(num_results=2000) -> List: 
        url_number_attribute = np.linspace(start=0,
                                            stop=num_results,
                                            num=int((num_results)/20))
        results = [] 
        for i in url_number_attribute:
            final_url = f"https://www.daft.ie/property-for-sale/dublin-city?pageSize=20&from={int(i)}"
            doc = requests.get(final_url) 
            soup = BeautifulSoup(doc.content, "html.parser")
            currResult = soup.find(attrs={'data-testid': 'results'})\
                .find_all("li", class_="SearchPage__Result-gg133s-2 itNYNv")
            results.extend(currResult)
        print(len(results))
        return None;

    def ParseHTML() -> pd.DataFrame:
        pass 


Parser.getHTMLResults()