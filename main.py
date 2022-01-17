# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    import requests
    import json

    response = requests.get('https://www.alphavantage.co/query?'
                     'function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=JVFZL3JJZY4IBYFS')
    print(response.status_code)
    data = response.json()
    print(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
