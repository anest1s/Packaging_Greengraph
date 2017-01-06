import requests
from unittest.mock import patch


# the following code downloads a map from the internet
def map_at(lat, long, satellite=False, zoom=10,
           size=(400, 400), sensor=False):
    base = "http://maps.googleapis.com/maps/api/staticmap?"
    params = dict(
        sensor=str(sensor).lower(),
        zoom=zoom,
        size="x".join(map(str, size)),
        center=",".join(map(str, (lat, long))),
        style="feature:all|element:labels|visibility:off")
    if satellite:
        params["maptype"] = "satellite"
    return requests.get(base, params=params)

# longitude and latitude of Athens, Greece
athens_map = map_at(37.9838096, 23.72753883)


# mocking the requests object
with patch.object(requests, 'get') as mock_get:
    athens_map = map_at(37.9838096, 23.72753883)
    print(mock_get.mock_calls)


# this function tests that the map_at function is building the parameters correctly
def test_build_default_params():
    with patch.object(requests, 'get') as mock_get:
        default_map=map_at(51.0, 0.0)
        mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
                'sensor': 'false',
                'zoom': 10,
                'size': '400x400',
                'center': '51.0,0.0',
                'style': 'feature:all|element:labels|visibility:off'
            }
        )

test_build_default_params()
