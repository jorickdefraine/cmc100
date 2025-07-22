from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import datetime


def fetch_cmc_data():
    """Fetch data from CoinMarketCap API and save to JSON file"""
    url = 'https://pro-api.coinmarketcap.com/v3/index/cmc100-historical'
    parameters = {
        'time_start': os.getenv('TIME_START'),
        'time_end': os.getenv('TIME_END')
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('CMC_PRO_API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        json_filename = "cmc_data.json"
        with open(f'output/{json_filename}', 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Data successfully saved to {json_filename}")
        return data
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"API request failed: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def process_and_visualize(data, top_n):
    """Process the API data and create visualizations"""
    try:
        constituents = data['data'][0]['constituents']
        print("Constituents successfully retreived from data.")
    except (KeyError, IndexError) as e:
        print(f"Error processing data: {e}")
        return

    df = pd.DataFrame(constituents)
    df = df.sort_values('weight', ascending=False).reset_index(drop=True)

    top = df.head(top_n)
    others_weight = df['weight'][top_n:].sum()
    others_count = len(df) - top_n

    pie_data = pd.concat([
        top,
        pd.DataFrame([{
            'name': f'Others ({others_count} coins)',
            'symbol': 'OTH',
            'weight': others_weight
        }])
    ])

    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(
        pie_data['weight'],
        labels=pie_data['name'] + ' (' + pie_data['symbol'] + ')',
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.85,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1}
    )

    plt.setp(autotexts, size=8, weight="bold")
    plt.setp(texts, size=8)

    plt.title(f'CMC100 Index Composition (Top {top_n} + Others)\nDate: {data["data"][0]["update_time"]}', pad=20)
    plt.annotate(
        f"Total constituents: {len(df)}\nData source: CoinMarketCap",
        xy=(0.5, 0), xytext=(0, -20),
        xycoords='axes fraction', textcoords='offset points',
        ha='center', va='top', fontsize=8
    )

    chart_filename = f'cmc100_pie_chart.png'
    plt.savefig(f'output/{chart_filename}', bbox_inches='tight', dpi=300)

    csv_filename = f'cmc100_constituents.csv'
    df.to_csv(f'output/{csv_filename}', index=False)


def main():
    top_n = 5 # Edit Top N constituents to show in the pie chart here.
    data = fetch_cmc_data()
    
    if data:
        process_and_visualize(data, top_n)

if __name__ == "__main__":
    main()