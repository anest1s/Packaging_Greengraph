import numpy as np
from io import BytesIO
from matplotlib import image as img
import requests


class Map(object):

    def __init__(self, lat, long, satellite=True, zoom=10,
                 size=(400, 400), sensor=False):

        '''
        This function builds up a google map URL given a latitude and a longitude
        '''

        base = "http://maps.googleapis.com/maps/api/staticmap?"

        params = dict(
            sensor=str(sensor).lower(),
            zoom=zoom,
            size="x".join(map(str, size)),
            center=",".join(map(str, (lat, long))),
            style="feature:all|element:labels|visibility:off"
        )

        if satellite:
            params["maptype"] = "satellite"

        self.image = requests.get(base, params=params).content  # Fetch our PNG image data
        content = BytesIO(self.image)
        self.pixels = img.imread(content)  # Parse our PNG image as a numpy array

    def green(self, threshold):

        '''
        This function defines what we count as green in the RGB image,
        by comparing element by element the middle (green, num:1) layer
        to the top (red, num:0) and bottom (blue, num:2).
        It returns the green pixels determined from the above algorithm.
        '''

        # Use NumPy to build an element-by-element logical array
        greener_than_red = self.pixels[:, :, 1] > threshold*self.pixels[:, :, 0]
        greener_than_blue = self.pixels[:, :, 1] > threshold*self.pixels[:, :, 2]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green

    def count_green(self, threshold=1.1):

        '''
        This function sums the number of green pixels found, and returns the number of the sum.
        '''

        return np.sum(self.green(threshold))

    def show_green(self, threshold=1.1):

        '''
        This function displays the green content in a black-green image,
        based on the above threshold criteria.
        '''

        green = self.green(threshold)
        out = green[:, :, np.newaxis]*np.array([0, 1, 0])[np.newaxis, np.newaxis, :]
        buffer = BytesIO()
        result = img.imsave(buffer, out, format='png')
        return buffer.getvalue()
