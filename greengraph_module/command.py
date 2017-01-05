from argparse import ArgumentParser
import matplotlib.pyplot as plt
from greengraph_module import Greengraph

def process():

   '''
   This function parses the start point, end point and integer number of steps,
   provided by the user.
   '''

   parser = ArgumentParser(description="Generate a graph that shows \
                    the amount of green pixels between two locations. ")
   parser.add_argument('--fr0m', required=True, help="Type the starting place")
   parser.add_argument('--to', required=True, help="Type the destination")
   parser.add_argument('--steps', type=int, required=True, help="Number the steps")
   parser.add_argument('--out', help="Determine the name and format of the output file")
   arguments = parser.parse_args()

   mygraph = Greengraph(arguments.fr0m, arguments.to)
   data = mygraph.green_between(arguments.steps)
   plt.plot(data)
   plt.savefig(arguments.out)

if __name__ == "__main__":
    process()
