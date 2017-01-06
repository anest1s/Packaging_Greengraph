from nose.tools import assert_almost_equal
from greengraph_module import Greengraph
import geopy
from unittest.mock import patch
import yaml
import os
import numpy as np


# import fixtures data
fixtures = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures.yaml')))

# use fixtures for geolocate data
geolocate_fixtures = fixtures['geolocate']


def mock_geocode(place):

    '''
    this function uses the fixtures to extract the latitude and the longitude of the selected place
    '''

    code = [[[], []]]
    code[0][1] = [geolocate_fixtures[place]['latitude'], geolocate_fixtures[place]['longitude']]
    return code


def test_geolocate():
    for place_from in geolocate_fixtures:
        for place_to in geolocate_fixtures:
            with patch.object(geopy.geocoders.GoogleV3, 'geocode', return_value=mock_geocode(place_from)) as mocked_geocode:
                graph = Greengraph(place_from, place_to)
                lat, lng = graph.geolocate(place_from)
                mocked_geocode.assert_called_with(place_from, exactly_one=False)
                assert_almost_equal(geolocate_fixtures[place_from]['latitude'], lat)
                assert_almost_equal(geolocate_fixtures[place_from]['longitude'], lng)

test_geolocate()


# use fixtures for location sequence data
location_sequence_fixtures = fixtures['location_sequence']


def test_location_sequence():
    graph = Greengraph('Athens', 'Lamia')
    for steps in location_sequence_fixtures:
        with patch.object(geopy.geocoders.GoogleV3, 'geocode', side_effect=[
        mock_geocode('Athens'), mock_geocode('Lamia')]) as mocked_geocode:
            out = graph.location_sequence(graph.geolocate('Athens'),
            graph.geolocate('Lamia'), steps)
            np.testing.assert_almost_equal(out, location_sequence_fixtures[steps])

test_location_sequence()
