# Real-Time-Web-Scraping-of-Booking.com-Live-Data-Extraction-and-Analysis

Output:
![image](https://github.com/user-attachments/assets/ebcf96ad-9d27-46da-ad9c-c383c04857a8)

# Real-Time Web Scraping of Booking.com

## Overview
This project is a real-time web scraper for **Booking.com**, extracting hotel information such as name, location, price, rating, score, review, and a direct link to the hotel page. The data is saved into a CSV file for further analysis.

## Features
- Scrapes hotel details from Booking.com
- Extracts essential information:
  - Hotel Name
  - Location
  - Price
  - Rating
  - Score
  - Review
  - Direct Booking Link
- Saves the extracted data into a **CSV file** (`hotel_booking_data.csv`)
- Uses **BeautifulSoup** and **Requests** for web scraping

## Prerequisites
Ensure you have Python installed along with the necessary libraries:
```bash
pip install requests beautifulsoup4 lxml
```

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. Run the script:
   ```bash
   python scrape_booking.py
   ```
3. After execution, the extracted data will be saved in `hotel_booking_data.csv`.

## Code Explanation
The script performs the following steps:
1. **Send a Request**: Uses `requests.get()` to fetch the Booking.com search results page.
2. **Parse the HTML**: Uses `BeautifulSoup` to process the response.
3. **Extract Data**: Finds hotel details using class attributes and stores them in variables.
4. **Save to CSV**: Writes extracted details into a CSV file.
5. **Handle Errors**: Prints an error message if the request fails.

## Code
```python
import requests
from bs4 import BeautifulSoup
import lxml
import csv

url = "https://www.booking.com/searchresults.html?..."
Header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."}
page = requests.get(url, headers=Header)

if page.status_code == 200:
    print("Page loaded successfully")
    soup = BeautifulSoup(page.text, 'lxml')
    hotel_divs = soup.find_all('div', role="listitem")
    
    with open("hotel_booking_data.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Hotel Name', 'Location', 'Price', 'Rating', 'Score', 'Review', 'Link'])
        
        for hotel in hotel_divs:
            hotel_name = hotel.find('div', class_='f6431b446c a15b38c233').text.strip()
            location = hotel.find('span', class_='aee5343fdb def9bc142a').text.strip()
            price = hotel.find('span', class_='f6431b446c fbfd7c1165 e84eb96b1f').text.strip().replace('₹','')
            rating = hotel.find('div', class_='a3b8729ab1 e6208ee469 cb2cbb3ccb').text.strip()
            score = hotel.find("div", class_='a3b8729ab1 d86cee9b25').text.strip().split(' ')[-1]
            review = hotel.find('div', class_='abf093bdfe f45d8e4c32 d935416c47').text.strip()
            link = hotel.find('a', href=True).get('href')
            writer.writerow([hotel_name, location, price, rating, score, review, link])
else:
    print("Error loading the page", page.status_code)
```

## Potential Issues & Solutions
- **403 Forbidden / Captcha Issues**: Booking.com may block automated requests. Use:
  - **Rotating User-Agents**
  - **Proxies**
  - **Headless Browsing (Selenium)**
- **Missing Data**: Some elements may not always exist. Use `try-except` blocks to handle missing values.

## Disclaimer
This script is for educational purposes only. Scraping Booking.com may violate its **Terms of Service**. Use responsibly and consider API alternatives if available.

## License
This project is licensed under the MIT License.

