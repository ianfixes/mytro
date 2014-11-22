
class Diagram(object):

    def __init__(self):
        self.stations = [] # name, x, y
        self.edges = [] # color
        self.labels = []


class OptimizableDiagram(Diagram):

    def normalize(self):
        self.stations # snap this to an integer grid.
        # probably find the bounding box of all stations,
        # then normalize to that grid (just use lat/lon & multiply)


        
    def findLowestStationCriteria(self):
        # define a radius (rectangle)
        #    for each point
        #        move station to that point, measure criteria
        # return the lowest criteria and the move that caused it
        pass

    def findLowestLabelCriteria(self):
        pass

    
    def moveStation(self, move):
        # apply the new x,y to the station given in move
        # TODO: does this drag the label along?
        pass


    def moveCluster(self, movelist):
        for move in movelist:
            self.moveStation(move)

    def moveLabel(self, move):
        # apply the new position to the label given in the move
        pass

    def clusterOverlengthEdges(self):
        pass

    def clusterBends(self):
        pass

    def clusterPartitions(self):
        pass

    
    def calcStationCriteria(self):
        return sum([
                self.angularResolutionCriterion(),
                self.edgeLengthCriterion(),
                self.balancedEdgeLengthCriterion(),
                self.lineStraightnessCriterion(),
                self.octilinearityCriterion(),
                ])


    def calcLabelCriteria(self):
        pass
