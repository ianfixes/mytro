
# Based on:
# Automatic Metro Map Layout Using Multicriteria Optimization
# Jonathan Stott et. al.

class Metroize(object):

    def __init__(self):
        self.ideal_edge_length = 10 # some number of grid points
                                    # must allow all lines to fit in one station, in parallel
        self.diagram = None
        
        
    
    def solve(self, diagram):
        
        mt0 = diagram.calcStationCriteria() + diagram.calcLabelCriteria()
        
        running = true
        
        while running:
            for vertex in diagram.stations:
                mn0 = diagram.calcStationCriteria()
                mn  = diagram.findLowestStationCriteria()

                if mn < mn0:
                    diagram.moveStation(vertex)
        
            p = sum([diagram.clusterOverlengthEdges(),
                     diagram.clusterBends(),
                     diagram.clusterPartitions()])

            for point in p:
                mn0 = diagram.calcStationCriteria()
                mn  = diagram.findLowestStationCriteria()
                if mn < mn0:
                    diagram.moveCluster(p)

            for label in [s.label for s in diagram.stations]:
                ml0 = diagram.calcLabelCriteria()
                ml  = diagram.findLowestLabelCriteria()
                if ml < ml0:
                    diagram.moveLabel(label)

            mt = sum([diagram.calcStationCritera(),
                      diagram.calcLabelCriteria()])

            if mt < mt0:
                mt0 = mt
            else:
                running = false

        # retuurn something?
            


