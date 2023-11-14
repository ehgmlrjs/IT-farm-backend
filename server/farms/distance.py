from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import quote
import json


def geocoding(address):
    client_id = 'p98qgm9ld6'
    client_pw = 'NxH5cMAaisnvmaKpLjyYsj9fUHjF0qxnoroyPRad'

    api_url = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={quote(address)}'

    request = Request(api_url)
    request.add_header('X-NCp-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)

    try:
        response = urlopen(request)
    except HTTPError as e:
        print('HTTP Error!')
        latitude = None
        longitude = None
    else:
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)
            if response_body['addresses'] == []:
                print('result not exist!')
                latitude = None
                longitude = None
            else:
                latitude = response_body['addresses'][0]['y']
                longitude = response_body['addresses'][0]['x']
                print('Success!')
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None

    return latitude, longitude


def distance(lat,log):
    centerlist = [
        ('정읍', 35.5631, 126.8512),
        ('고창', 35.4354, 126.7108),
        ('익산', 35.9457, 126.9547),
        ('아산', 36.7920, 127.0026),
        ('청주', 36.6418, 127.4855)
    ]
    li = []
    for center in centerlist:
        li.append((center[1]-float(lat))**2 + (center[2]-float(log))**2)
    
    return centerlist[li.index(min(li))][0]
