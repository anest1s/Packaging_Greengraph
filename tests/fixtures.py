from greengraph_module import Greengraph
import yaml
import os


graph = Greengraph('Athens', 'Lamia')

places = ['Athens', 'Lamia']
steps = [2, 4]


#geolocate fixture
fixtures = {}
with open(os.path.join(os.path.dirname(__file__), 'fixtures.yaml'), 'w') as fixtures_file:
    for place in places:
        latitude, longitude = graph.geolocate(place)
        fixtures[place] = {'latitude': latitude, 'longitude': longitude}
    yaml.dump({'geolocate': fixtures}, fixtures_file)
