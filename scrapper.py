import requests
from bs4 import BeautifulSoup

def extract_land(url):
  title = url.find('div',{'class' : 'item_title'}).find_all('span', recrusive=False)
  price = url.find('div',{'class' : 'price_line'}).find('span',{'class' : 'price'})
  #price = price2.find('span',{'class' : 'price'})
  price = price.get_text(strip=True)
  price = float(price)
  print(price)

  landsize, details = url.find('div',{'class' : 'info_area'}).find_all('span', recrusive=False)
  landsize = landsize.get_text(strip=True)
  print(landsize)

  #company, location = html.find('h3').find_all('span', recrusive=False)

  #location = location.get_text(strip=True).strip("-")
  #print(location)

  #company, location = html.find('h3').find_all('span', recrusive=False)
  #company = company.get_text(strip=True).strip("-")
  #location = location.get_text(strip=True).strip("-")
  #job_id = html['data-jobid']
  return {'title':title, 'price':price, 'landsize':landsize}

def extract_lands(last_page, url):
  lands = []
  for page in range(last_page):
    print(f"Scrapping Stackoverflow : page : {page}")
    result = requests.get(f"{url}&pg=page{page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      land = extract_land(result)
      lands.append(land)
    return lands

#def get_lands():
#    url = "https://new.land.naver.com/offices?ms=37.7668564,126.7116667,17&a=TJ&b=A1&e=RETAIL&g=10000&ad=true"
#    lands = extract_lands(url)
#    return lands