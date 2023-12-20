import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/'

raw = requests.get(URL)
html = BeautifulSoup(raw.text, 'lxml')

def fetch_html():
    raw = requests.get(URL)
    html = BeautifulSoup(raw.text, 'lxml')
    return html

def get_top_transactions():
    units_up1 = html.select('#_topItems1 > tr')  # 거래상위 가져오기
    
    top_transactions = []

    for unit in units_up1[:16]:
        name = unit.select_one('th > a').text
        price = unit.select_one('td').text
        up = unit.select_one('td:nth-child(3)').text.replace('Upper price', '↑')
        percent = unit.select_one('td:nth-child(4)').text
        
        top_transaction = {
            '종목 이름': name,
            '한 주당 가격': f"{price} 원",
            '전날 대비 가격 변동': up,
            '전날 대비 등락': percent
        }

        top_transactions.append(top_transaction)

    return top_transactions


def top_price():
    units_up = html.select('#_topItems2 > tr')  # 상한가 가져오기

    top_prices = []

    for unit in units_up[:16]:
        name = unit.select_one('th > a').text
        price = unit.select_one('td').text
        up = unit.select_one('td:nth-child(3)').text.replace('Upper price', '↑')
        percent = unit.select_one('td:nth-child(4)').text
        
        top_price = {
            '종목 이름': name,
            '한 주당 가격': f"{price} 원",
            '전날 대비 가격 변동': up,
            '전날 대비 등락': percent
        }

        top_prices.append(top_price)

    return top_prices


def low_price():
    units_up = html.select('#_topItems3 > tr')  # 하한가 가져오기

    low_prices = []

    for unit in units_up[:16]:
        name = unit.select_one('th > a').text
        price = unit.select_one('td').text
        up = unit.select_one('td:nth-child(3)').text.replace('Upper price', '↑')
        percent = unit.select_one('td:nth-child(4)').text
        
        low_price = {
            '종목 이름': price,
            '한 주당 가격': f"{price} 원",
            '전날 대비 가격 변동': up,
            '전날 대비 등락': percent
        }

        low_prices.append(low_price)

    return low_prices


def market_cap():
    units_up1 = html.select('#_topItems4 > tr')  # 시가총액 상위 가져오기
    
    market_caps = []

    for unit in units_up1[:16]:
        name = unit.select_one('th > a').text
        price = unit.select_one('td').text
        up = unit.select_one('td:nth-child(3)').text.replace('Upper price', '↑')
        percent = unit.select_one('td:nth-child(4)').text
        
        market_cap = {
            '종목 이름': name,
            '한 주당 가격': f"{price} 원",
            '전날 대비 가격 변동': up,
            '전날 대비 등락': percent
        }

        market_caps.append(market_cap)

    return market_caps


def main():
    while True:
        html = fetch_html()
        print("1. 거래 상위\n2. 상한가\n3. 하한가\n4. 시가총액 상위")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            result = get_top_transactions()
        elif choice == '2':
            result = top_price()
        elif choice == '3':
            result = low_price()
        elif choice == '4':
            result = market_cap()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            return

        print("\nResults:")
        for item in result:
            for key, value in item.items():
                print(f'{key}: {value}')
            print()
        
        repeat = input("Press 'q' to quit, any other key to continue: ")
        if repeat.lower() == 'q':
            break

if __name__ == "__main__":
    main()
