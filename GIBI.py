import requests

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)

        data = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[City]': response.get('city'),
            '[Org]': response.get('org'),
            '[Country Code]': response.get('countryCode'),
            '[Region]': response.get('region'),
            '[Region Name]': response.get('regionName'),
            '[Status]': response.get('status'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')
    except requests.exceptions.ConnectionError:
        print('Please check your connection')

def main():
    ip = input('Enter IP: ')
    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
