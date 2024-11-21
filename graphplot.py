import matplotlib.pyplot as plt

# Graph
class GraphPlot():

    # setting the ranges and no. of intervals
    range = (0, 100)
    bins = 10  
    val = []

    def __init__(self, val):
        self.val = val

    def plotshow(self):
        # plotting a histogram
        plt.hist(self.val, self.bins, self.range, color = 'green',
                histtype = 'bar', rwidth = 0.8)

        # x-axis label
        plt.xlabel('Speed')
        # frequency label
        plt.ylabel('No. of data')
        # plot title
        plt.title('My speed')

        # function to show the plot
        plt.show()

