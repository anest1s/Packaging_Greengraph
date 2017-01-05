from greengraph_module import Greengraph
from itertools import chain
import yaml
import os
import numpy as np


graph = Greengraph('Athens', 'Lamia')
places = ['Athens', 'Lamia']
steps = [2, 10]


# geolocate fixtures
fixtures = {}
with open(os.path.join(os.path.dirname(__file__), 'fixtures.yaml'), 'w') as fixtures_file:
    for place in places:
        latitude, longitude = graph.geolocate(place)
        fixtures[place] = {'latitude': latitude, 'longitude': longitude}
    yaml.dump({'geolocate': fixtures}, fixtures_file)


# location_sequence fixtures
fixtures = {}
with open(os.path.join(os.path.dirname(__file__), 'fixtures.yaml'), 'a') as fixtures_file:
    for step in steps:
        fixtures[step] = (graph.location_sequence(graph.geolocate('Athens'), graph.geolocate('Lamia'), step)).tolist()
    yaml.dump({'location_sequence': fixtures}, fixtures_file)


# green_between fixtures
fixtures = {}
with open(os.path.join(os.path.dirname(__file__), 'fixtures.yaml'), 'a') as fixtures_file:
    for step in steps:
        number = graph.green_between(step)
        fixtures[step] = list(chain.from_iterable(np.vstack(number).tolist()))
    yaml.dump({'green_between': fixtures}, fixtures_file)
