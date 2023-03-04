import unittest
from toll_calculator import TollCalculator

class TestTollCalculator(unittest.TestCase):

    def test_qew_highway400_direction(self):
        self.assertEqual(TollCalculator().calculateDirection('QEW', 'Highway 400'), 'east')

    def test_highway400_qew_direction(self):
        self.assertEqual(TollCalculator().calculateDirection('Highway 400', 'QEW'), 'west')
    
    def test_qew_highway400_distance(self):
        self.assertEqual(TollCalculator().calculateDistance('QEW', 'Highway 400'), 67.75)

    def test_highway400_qew_distance(self):
        self.assertEqual(TollCalculator().calculateDistance('Highway 400', 'QEW'), 67.75)

    def test_qew_highway400_distance_equal(self):
        self.assertEqual(TollCalculator().calculateDistance('QEW', 'Highway 400'), TollCalculator().calculateDistance('Highway 400', 'QEW'))

    def test_qew_highway400_toll(self):
        self.assertEqual(TollCalculator().costOfTrip('QEW', 'Highway 400'), 16.94)

    def test_highway400_qew_toll(self):
        self.assertEqual(TollCalculator().costOfTrip('Highway 400', 'QEW'), 16.94)

    def test_qew_highway400_toll_equal(self):
        self.assertEqual(TollCalculator().costOfTrip('QEW', 'Highway 400'), TollCalculator().costOfTrip('Highway 400', 'QEW'))

    def test_qew_salem_road_direction(self):
        self.assertEqual(TollCalculator().calculateDirection('QEW', 'Salem Road'), 'east')

    def test_salem_road_qew_direction(self):
        self.assertEqual(TollCalculator().calculateDirection('Salem Road', 'QEW'), 'west')
    
    def test_qew_salem_road_distance(self):
        self.assertEqual(TollCalculator().calculateDistance('QEW', 'Salem Road'), 115.28)

    def test_salem_road_qew_distance(self):
        self.assertEqual(TollCalculator().calculateDistance('Salem Road', 'QEW'), 115.28)

    def test_qew_salem_road_distance_equal(self):
        self.assertEqual(TollCalculator().calculateDistance('QEW', 'Salem Road'), TollCalculator().calculateDistance('Salem Road', 'QEW'))

    def test_qew_salem_road_toll(self):
        self.assertEqual(TollCalculator().costOfTrip('QEW', 'Salem Road'), 28.82)

    def test_salem_road_qew_toll(self):
        self.assertEqual(TollCalculator().costOfTrip('Salem Road', 'QEW'), 28.82)

    def test_qew_salem_road_toll_equal(self):
        self.assertEqual(TollCalculator().costOfTrip('QEW', 'Salem Road'), TollCalculator().costOfTrip('Salem Road', 'QEW'))

    def test_keele_street_highway404_direction(self):
        self.assertEqual(TollCalculator().calculateDirection('Keele Street', 'Highway 404'), 'east')

    def test_highway404_keele_street_direction(self):
        self.assertEqual(TollCalculator().calculateDirection('Highway 404', 'Keele Street'), 'west')
    
    def test_keele_street_highway404_distance(self):
        self.assertEqual(TollCalculator().calculateDistance('Keele Street', 'Highway 404'), 12.89)

    def test_highway404_keele_street_distance(self):
        self.assertEqual(TollCalculator().calculateDistance('Highway 404', 'Keele Street'), 12.89)

    def test_keele_street_highway404_distance_equal(self):
        self.assertEqual(TollCalculator().calculateDistance('Keele Street', 'Highway 404'), TollCalculator().calculateDistance('Highway 404', 'Keele Street'))

    def test_keele_street_highway404_toll(self):
        self.assertEqual(TollCalculator().costOfTrip('Keele Street', 'Highway 404'), 3.22)

    def test_highway404_keele_street_toll(self):
        self.assertEqual(TollCalculator().costOfTrip('Highway 404', 'Keele Street'), 3.22)

    def test_keele_street_highway404_toll_equal(self):
        self.assertEqual(TollCalculator().costOfTrip('Keele Street', 'Highway 404'), TollCalculator().costOfTrip('Highway 404', 'Keele Street'))

if __name__ == '__main__':
    unittest.main()