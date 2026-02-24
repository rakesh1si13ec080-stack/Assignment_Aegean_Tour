# Assignment_Aegean_Tour
Assignment
Overview

1.this program generates an island tour itinerary based on the preference given by each customer
2.assigns each hop as airborne or by-sea
3.satisfies all customer transport preferences
4.minimizes the number of airborne hops
5.prints "NO ITINERARY" if no valid solution exists
6.assumptios TRUE for airborne and FALSE for by-sea


How to Run:

1. Save your input file data.txt and python file aaegan_tour.py in the same folder
2. Run the script: "python aaegan_tour.py" in console
3. The program will: Read from data.txt and print the final itinerary to the console



example:input from data.txt

6----> hops count

4----> customer count

0 by-sea, 2 by-sea, 3 by-sea ------> customer 1 preference

0 by-sea, 5 airborne         ------> customer 2 preference

0 airborne, 5 by-sea         ------> customer 3 preference

2 airborne                   ------> customer 4 preference


output:

0 by-sea, 1 by-sea, 2 airborne, 3 by-sea, 4 by-sea, 5 by-sea
