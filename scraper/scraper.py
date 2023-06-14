import requests
from bs4 import BeautifulSoup



"""
this the wikibidia page  url
"""
url='https://en.wikipedia.org/wiki/Nissan_Silvia'






   
def get_citations_needed_count(page_url):
    """
    this function will search for (citation needed) in the page of wikibidia and will count their number 
    and return the number
    """
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_citation=soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    k=0
    for n in all_citation:
       k+=1
    return k 
    


def get_citations_needed_report(page_url):
   """
   this function will search for (citation needed) in the page of wikibidia and will search for thier parent thet 
   is paragraphs then it will return all the paragraphs with (citation needed)
   """
   page = requests.get(page_url)
   soup = BeautifulSoup(page.content,'html.parser')
   all_citation=soup.find_all('sup', class_="noprint Inline-Template Template-Fact")       
       
   all_paragraphs_text=[i.parent.text for i in all_citation]        
   strr=''
   for n in all_paragraphs_text:
      strr+=str(n)+"\n"+"\n"+"\n"
     
   return strr    

print(get_citations_needed_count(url)) 
print(get_citations_needed_report(url))  

