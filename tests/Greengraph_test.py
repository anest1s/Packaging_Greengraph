from nose.tools import assert_almost_equal
from greengraph_module import Greengraph
import geopy
from unittest.mock import patch
import yaml
import os


# use fixtures
fixtures = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures.yaml')))
fixtures = fixtures['geolocate']

def mock_geocode(place):

    '''

    this function uses the fixtures to extract the latitude and the longitude of the selected place
    '''

    code = [[[], []]]
    code[0][1] = [fixtures[place]['latitude'], fixtures[place]['longitude']]
    return code


def test_geolocate():
    for place_from in fixtures:
        for place_to in fixtures:
            with patch.object(geopy.geocoders.GoogleV3, 'geocode', return_value=mock_geocode(place_from)) as mocked_geocode:
                graph = Greengraph(place_from, place_to)
                lat, lng = graph.geolocate(place_from)
                mocked_geocode.assert_called_with(place_from, exactly_one=False)
                assert_almost_equal(fixtures[place_from]['latitude'], lat)
                assert_almost_equal(fixtures[place_from]['longitude'], lng)

test_geolocate()
