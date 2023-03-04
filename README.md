# Trip Calculator

*Goal:* Given an entry and exit point, calculate the toll based on the rate of $0.25/km.

*Code Overview:* The trip calculator has been implemented as a class in Python 3. The TollCalculator class is stored in toll_calculator.py whereas its unit tests, written using the built-in unittest library are stored in toll_calculator_tests. Below is an overview of its functions:

```

calculateDirection() -> Takes entry and exit interchanges as a string and determines whether the route is east-bound or west-bound. Returns either 'east' or 'west' as a string.

calculateDistance() -> Given an entry and exit interchange as a string, it will determine the distance between the two in kilometres and return it as a floating point

costOfTrip() -> Given an entry and exit interchange as a string, it will calculate the total cost to travel this segment

generateList() -> Given an entry and exit interchange, a list will be returned containing only the keys of the traversed interchanges ordered in the direction of travel

```

*Prerequisites:* Python 3.5+

*Instructions:* To execute some functions in the main class, execute the following in your terminal. By default it will display the price for the QEW to Highway 400 east-bound and west-bound as well as the cost for Salem Road to the QEW both east-bound and west-bound.

```

python toll_calculator.py

```

To run the unit tests, please execute the following:

```

python toll_calculator_tests.py

```
There are 24 unit tests written, testing the cost, distance and direction of 6 different possible routes: QEW to Salem Road, Salem Road to QEW, Keele Street to Highway 404, Highway 404 to Keele Street, QEW to Highway 400, and Highway 400 to QEW.