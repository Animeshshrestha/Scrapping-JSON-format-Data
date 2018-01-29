import requests
import json
import csv
import os

url='https://www.honda.com.br/concessionarias/api/'
filename='hondaDealer.csv'

response = requests.get(url) # load the url         
content = response.content   # takes the content  overall it gives the page source content

print("Searching Dealers from Honda......")
dealersContent = response.content.decode("utf8") # globally supported unicode to decode
dealers = json.loads(dealersContent)
totalDealers = len(dealers)
if totalDealers>0:
    print("Total Dealers Found: ",totalDealers)
    #print("\n Dealers [0]: ",dealers[0]) #gives the information of first position 
    
    with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'w+',newline='') as f:#Writing the obtained data to the filenamed hondaDealer.csv
        writer = csv.writer(f)#csv.writer using file
        #Providing Column Names for Selected Data
        writer.writerow(['ID', 'Title','Dealer ID', 'City', 'State','Latitude','Longitude','Email ID'])# columns name 
        for i in range(0,totalDealers):
            if i==0:
                print("\n Writing Data to CSV starting...")
            #preparing row of Data for CSV
            row = [
                i + 1,
                dealers[i]['title'],
                dealers[i]['field_dealer_cidade'],
                dealers[i]['field_cod_dealer'],
                dealers[i]['field_dealer_estado'],
                dealers[i]['field_geolocation'],
                dealers[i]['field_geolocation_1'],
                dealers[i]['field_mail']
                ]
            writer.writerow(row)
        if i==totalDealers:
            print("\n Writing Data to CSV ending now...")
            
