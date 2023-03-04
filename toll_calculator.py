import json
import os

class TollCalculator:
    def __init__(self):
        self.filePath = os.getcwd() + '/interchanges.json'
        self.ratePerKilometre = 0.25
        
        try:
            with open(self.filePath, 'r') as fileReader:
                self.interchangeData = json.loads(fileReader.read())
        except FileNotFoundError:
            raise Exception('Unable to open interchanges file')

    def calculateDirection(self, enter, exit): 
        '''Takes entry and exit interchanges and determines whether the route is east-bound or west-bound'''
        foundEnterFlag = False
        foundExitFlag = False

        # Default is west to east in json file
        for key in self.interchangeData.get('locations'):
            data = self.interchangeData.get('locations').get(key)

            if data.get('name') == enter:
                # if the exit flag has already been found that means that we are traversing 
                # opposite to the default
                if foundExitFlag:
                    return 'west'

                foundEnterFlag = True
            
            if data.get('name') == exit:
                if foundEnterFlag:
                    return 'east'

                foundExitFlag = True
            
        raise Exception('Unable to calculate direction')

    def calculateDistance(self, enter, exit):
        ''' Given an entry and exit interchange, it will determine the distance between the two in kilometres '''
        # grab ordered list of traversed interchanges
        keys = self.generateList(enter, exit)
        totalDistance = 0.0

        # queue datatype: remove item after it has been summated 
        # continue until there are no items remaining 
        while len(keys) >= 1:
            key = keys.pop(0)

            # grab next list key after the current, when list is empty because we were
            # at len=1 before removing the element at index 0, then just return distance
            try:
                nextKey = keys[0]
            except:
                return round(totalDistance, 2)

            data = self.interchangeData.get('locations').get(key)                
            routes = data.get('routes')

            for route in routes:
                if int(route.get('toId')) == int(nextKey):
                    totalDistance += route.get('distance', 0)
            
        raise Exception("Unable to calculate distance")

    def costOfTrip(self, enter, exit):
        ''' Given an entry and exit interchange, it will calculate the total cost to travel this segment '''
        return round(self.calculateDistance(enter, exit) * self.ratePerKilometre, 2)
    
    def generateList(self, enter, exit): 
        ''' Given an entry and exit interchange, a list will be generated containing only the traversed 
        interchanges ordered in the direction of travel'''
        listIds = []
        
        # flag controls whether we have encountered the first listen item
        enterFlag = False
        interchanges = list(self.interchangeData.get('locations').items())

        if self.calculateDirection(enter, exit) == 'west':
            interchanges.reverse()

        for key, data in interchanges:
            if data.get('name') == enter:
                enterFlag = True
            
            # continue to add list keys after encountering initial entry interchange
            # stop when encountering the exit interchange. 
            if enterFlag:
                listIds.append(key)

                if data.get('name') == exit:
                    break
            
        return listIds

if __name__ == '__main__':
    tollCalculator = TollCalculator()
    print("Cost of the following trips:")
    print("QEW->Salem Road:", tollCalculator.costOfTrip('QEW', 'Salem Road'), ', Salem Road->QEW', tollCalculator.costOfTrip( 'Salem Road', 'QEW'))
    print("QEW->Highway 400", tollCalculator.costOfTrip('QEW', 'Highway 400'), ', Highway 400->QEW', tollCalculator.costOfTrip( 'Highway 400', 'QEW'))