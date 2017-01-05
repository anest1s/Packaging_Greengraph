from greengraph_module import Greengraph
import yaml
import os


graph = Greengraph('Athens', 'Lamia')

places = ['Athens', 'Lamia']
steps = [2, 4]

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
    for steps in steps:
        fixtures[steps] = (graph.location_sequence(graph.geolocate('Athens'), graph.geolocate('Lamia'), steps)).tolist()
    yaml.dump({'location_sequence': fixtures}, fixtures_file)
