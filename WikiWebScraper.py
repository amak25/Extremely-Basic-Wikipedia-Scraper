import os
cwd = os.getcwd() #Provides current filepath for to store in filepath variable later
print(f'Current Directory is {cwd}') 
print('-----------------')

import requests

from bs4 import BeautifulSoup

from datetime import datetime

import csv


filepath = ('') 
filename = 'Wikipedia Web Scraping Output.csv'

#URL = "https://en.wikipedia.org/wiki/Charlotte_Hornets" #Test URL 1 Charlotte Hornet
#URL = "https://en.wikipedia.org/wiki/Washington_Wizards" #Test URL 2 Washington Wizards
#URL = "https://en.wikipedia.org/wiki/Memphis_Grizzlies"  #Test URL 3 Memphis Grizzlies
URL = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(URL) #Uses Requests to form connection to URL through the 'Response' Variable
print(f'Status code is {response.status_code}')  #Checks for status code 200 to ensure web page is responsive
print()
print('-----------------')

soup = BeautifulSoup(response.content, 'html.parser') #Feeds Response into BeatifulSoup

MainPageTitle = soup.find('span',attrs={'class':'mw-page-title-main'}) #Stores Article Title into Soup Object
print(f'The Wikipedia page title is {MainPageTitle.text}')
print()
print('-----------------')

MainText = soup.find('div',attrs={'class':'mw-content-ltr mw-parser-output'}) #Subsections off Main Content of Page and stores it as a list of Soup Objects
BodyContent = MainText.find_all('p') #Pulls all paragraphs from the main content div
print(BodyContent[1].text) #Prints the content of the first paragrapgh on the page which has an index of 1 in MainText
print() 
print('-----------------')

FooterText = soup.find('div',attrs={'class':'mw-footer-container'}) #Subsections off the footer area of the page and stores it as a list of Soup Objects
LastUpdated = FooterText.find('li',attrs={'id':'footer-info-lastmod'}) #Stores the last time the page was updated from FooterText
print(LastUpdated.text)
print()
print('-----------------')

DateScraped = datetime.now() #Gets the current date and time and stores it in 'DateScraped'
print(f'This data was collected on {DateScraped}')

def OutputData(): #Function to quickly append scraped data into existing file
    with open(filepath + filename,'a') as CsvData:
        datawriter = csv.writer(CsvData, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        datawriter.writerow([MainPageTitle.text,BodyContent[1].text,LastUpdated.text,DateScraped])
    

if os.path.exists(filepath+filename): #Checks to see if the 'Wikipedia Web Scraping Output.csv' exists in the current directory
    OutputData()
    
else:
    with open(filepath + filename,'w') as CsvData: #Creates newfile using preset filepath and filename
        datawriter = csv.writer(CsvData, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        datawriter.writerow(['Page Title','First Paragraph','Last Page Update','Date Data Scraped']) #Header for new file
    OutputData()
    
