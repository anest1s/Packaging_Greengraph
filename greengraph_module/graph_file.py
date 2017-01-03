import numpy as np
import geopy
from greengraph_module.map_file import Map


class Greengraph(object):

    def __init__(self, start, end):

        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    def geolocate(self, place):

        '''
        This function gives a list of the following form:
        [Name, [Latitude, Longitude]].
        '''

        return self.geocoder.geocode(place, exactly_one=False)[0][1]

    def location_sequence(self, start, end, steps):

        '''
        This function gets evenly spaced set of spaces between the two given testpoints.
        '''

        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1], end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):

        '''
        This function loops over each element of the above list of coordinates,
        and gets a map for each place.
        '''

        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start),
                    self.geolocate(self.end),
                    steps)]
