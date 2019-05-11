import json, requests

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
    client_id = 'JZIEH03E2DX13EHU3LY1B1UDF5FBQJAICXXUIEOD12TZ4COV',
    client_secret = 'CQCZKKI253VSX53QWJ3CU0F5OPXXRKWSOFZ2GAJ1ENQP21IY',
    v = '20180323',
    ll = '37.392971, -122.076044',
    query = 'pizza',
    limit = 3
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
