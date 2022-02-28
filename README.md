# movie-theater-seating
**Language used:** Python

## Program Overview
This program takes in an input file of reservation requests through the command line  
and fulfills those reservations by assigning seats in the theatre to each request.  

The algorithm prioritizes customer satisfaction and customer safety.  

Assuming the seats in the back have a better viewing experience, the program searches  
for available seats starting for the back of the theatre for the specified party size.  

The program then assigns the first line of seats it finds to that reservation, and  
blocks off nearby seats to ensure customer safety.

## Assumptions
- Movie theater is arranged in 10 rows x 20 seats
- For safety reasons, 3 seats to the left and the right of each group
and directly in front and behind are blocked off
- Parties always want to be seated together and won't separate
- Reservations are in sequential order in the input file
- If request for reservation is unable to be fulfilled, it is not added to output file
- Seats in the back are better for customer experience
- Viewing experience is the same for all seats in a row

## Instructions
1. Navigate to the directory of the project containing all the files
2. In the terminal run 

        python main.py [path to input file]

3. Output file is available in the tests folder