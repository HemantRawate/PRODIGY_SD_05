import pandas as pd
import requests
from bs4 import BeautifulSoup

prod_name = []
prices = []
ratings = []

for i in range(1,5):
    url = "https://www.flipkart.com/search?q=mobile+phone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_6_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+phone&requestId=c590b481-1b85-4e5d-9acb-72daedcaa5ee&as-backfill=on&page="+str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")

    box = soup.find("div",class_ = "DOjaWF gdgoEp")

    names = box.find_all("div",class_ = "KzDlHZ")
    for i in names:
        Name = i.text
        if Name:
            prod_name.append(Name)
        else:
            prod_name.append("N/A")
        

    price = box.find_all("div",class_ = "Nx9bqj _4b5DiR")
    for i in price:
        Price = i.text
        if Price:
            prices.append(Price)
        else:
            prices.append("N/A")
        

    rating = box.find_all("div",class_ = "XQDdHH")
    for i in rating:
        Rating = i.text
        if Rating:
            ratings.append(Rating)
        else:
            ratings.append("N/A")
        
print(len(prod_name))
print(len(prices))
print(len(ratings))
try:
    df = pd.DataFrame({"Product Name": prod_name, "Prices": prices, "Ratings": ratings})
    df.to_csv("A://MCA//Internships//Prodigy//Flipkart_mobiles.csv")
    print("Data has been saved to Flipkart_mobiles.csv")
except Exception as e:
    print(f"Failed to save CSV: {e}")
