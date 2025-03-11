import requests
from bs4 import BeautifulSoup
import lxml
import csv

url = "https://www.booking.com/searchresults.html?ss=Pune&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AtLy5r0GwAIB0gIkNDkzNDE3OTAtN2QxNi00ODM2LWIwMTQtNGQ1YTY2Mjk1MWI12AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2108361&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=310852e972e403f7&ac_meta=GhAzMTA4NTJlOTcyZTQwM2Y3IAAoATICZW46BFB1bmVAAEoAUAA%3D&checkin=2025-03-01&checkout=2025-03-02&group_adults=2&no_rooms=1&group_children=0"
Header = {'User-Agent':"", 'Accept-Language': 'en-US, en;q=0.5"}
page = requests.get(url, headers =Header)

if page.status_code == 200:
    print("Page loaded successfully")
    soup = BeautifulSoup(page.text, 'lxml')

    hotel_divs = soup.find_all('div', role = "listitem")

    with open("hotel_booking_data.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)

        #adding header 
        writer.writerow(['Hotel Name', 'Location', 'Price', 'Rating', 'Score', 'Review', 'Link'])

        for hotel in hotel_divs:
            hotel_name = hotel.find('div', class_='f6431b446c a15b38c233').text.strip()

            location = hotel.find('span', class_='aee5343fdb def9bc142a').text.strip()

            price = hotel.find('span',class_='f6431b446c fbfd7c1165 e84eb96b1f').text.strip().replace('₹','')

            rating = hotel.find('div', class_='a3b8729ab1 e6208ee469 cb2cbb3ccb').text.strip()

            score = hotel.find("div",class_= 'a3b8729ab1 d86cee9b25').text.strip().split(' ')[-1]

            review = hotel.find('div', class_='abf093bdfe f45d8e4c32 d935416c47').text.strip()

            link = hotel.find('a', href=True).get('href')
            
            #saving file into csv
            writer.writerow([hotel_name, location, price, rating, score, review, link])

else:
    print("Error loading the page", page.status_code) 
