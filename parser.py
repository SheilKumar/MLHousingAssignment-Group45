import bs4
from bs4 import BeautifulSoup
import requests 
import numpy as np 
import pandas as pd

"""
function: getHTMLResults 
    ---------------------
    input: num of desired results
    output: list of html results 
    ---------------------
    Loop: for each page (20 results)
        Find each results in page and add to a list
    return List of html results 

function: parseHTML 
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

funtion: parseDocs
    -----------------------
    input: "li" html contents 
    output: title block
        "div" attrs: "data-testid":"title-block", class_ = "Card__CardWrapper-x1sjdn-0 gnintI"
    -----------------------

function: getAttributes
    -----------------------
    input: title block 
    output: wanted attributes:
        List<str> [price, address, beds, bathrooms, area]
    -----------------------
"""

class Parser: 
    main_url = "https://www.daft.ie/property-for-sale/dublin-city?pageSize=20&from="

    def __init__(self):
        pass

    def getHTMLResults(num_results: int=2000) -> list: 
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
        return results

    def parseHTML(htmlList: list) -> pd.DataFrame:
        df = pd.DataFrame(columns=["Price", "Address", "Bedrooms", "Baths"])
        for li_html in htmlList:
            cardTitleBlock = Parser.parseDoc(li_html)
            Parser.getAttributes(cardTitleBlock)
            break
        pass 

    def parseDoc(li_html: bs4.element.Tag):
        soup = li_html 
        #need to get cardwrapper;
        cardWrapper = soup.find(attrs={"data-testid":"card-wrapper"}, class_="Card__CardWrapper-x1sjdn-0 gnintI")\
            .find("div",attrs={"data-testid":"card-content"} ,class_="Card__Content-x1sjdn-9 iEbIAZ")\
                .find("div", attrs={"data-testid":"title-block"})
        return cardWrapper

    def getAttributes(div_html: bs4.element.Tag):
        soup = div_html
        cardPrice = soup.find("span",
                             class_="TitleBlock__StyledSpan-sc-1avkvav-4 gDBFnc").get_text()
        cardAddress = soup.find("p",
                             attrs={"data-testid":"address"},
                             class_="TitleBlock__Address-sc-1avkvav-7 knPImU").get_text()
        cardBedrooms = soup.find("p",
                             attrs={"data-testid":"beds"},
                             class_="TitleBlock__CardInfoItem-sc-1avkvav-8 jBZmlN").get_text()
        cardBaths = soup.find("p",
                             attrs={"data-testid":"baths"},
                             class_="TitleBlock__CardInfoItem-sc-1avkvav-8 jBZmlN").get_text()
        cardArea = soup.find("p",
                             attrs={"data-testid":"floor-area"},
                             class_="TitleBlock__CardInfoItem-sc-1avkvav-8 jBZmlN").get_text()
        cardResults = [cardPrice, cardAddress, cardBedrooms, cardBaths, cardArea]
        return cardResults


def main():
    HTMLList = Parser.getHTMLResults(100);
    Parser.parseHTML(HTMLList)
    return 0;

if __name__ == '__main__':
    main()