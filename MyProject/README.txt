=========================================================================================================
WATCHLIST ORGANIZER
=========================================================================================================
What is it?
    - A multi function organizer for the shows that I am watching
---------------------------------------------------------------------------------------------------------
Important Data Structures used:
    - Dictionaries
    - Lists
---------------------------------------------------------------------------------------------------------
Important Algorithms used:
    - Binary Search Tree
    - Queues (First In First Out)
---------------------------------------------------------------------------------------------------------
What happens to the lists and data during run? 
    - The Dictionaries of shows added will be written and saved to a JSON file
    - The watch queue lists will also be saved and written to a JSON file
---------------------------------------------------------------------------------------------------------
=========================================================================================================


=========================================================================================================
"FUNCTIONS"
=========================================================================================================
---------------------------------------------------------------------------------------------------------
My List

1. Add a new show to the list
    -   includes details such as 
        *genre
        *number of episodes
        *length of the show (short or long)
        *type of the show (series or movie)

2. Find a show in the list
    - helps user finds a show in the created list

3. Random picker
    - Asks user for preferred details and gives a random show recommendation from the list.

---------------------------------------------------------------------------------------------------------
My Watch Queue

4. Add a show to my watch Queue
    - checks if the show is the "My List" 
    - if not asks user to add show to "My List"
    - appends the show to watch queue

5. Show watch queue
    - shows current watch queue (shows that you need to watch)

6. Dequeue watch queue
    - asks user if the first in has been watched already
    - if yes it will be popped!
    - else nothing
---------------------------------------------------------------------------------------------------------
=========================================================================================================