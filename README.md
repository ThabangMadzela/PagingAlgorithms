# Page Replacement Algorithm

This is a Python program that simulates page replacement algorithms for virtual memory management. The implemented algorithms are:

* First In First Out (FIFO)
* Least Recently Used (LRU)
* Optimal Page Replacement (OPT)

## Requirements

This program requires Python 3 and the following libraries:

> * numpy

## Usage

To run the program, execute the following command:

```css
python paging.py [number of page frames] [num pages in ref str]
```

For example:

'''css
python paging.py 3 100
'''

This will simulate the three page replacement algorithms with a virtual memory of 3 pages and a reference string of 100 pages.

## Output

The program outputs the number of page faults for each algorithm.

'''css
[5, 8, 1, 7, 0, 4, 0, 8, 2, 0, 0, 3, 3, 3, 7, 5, 4, 9, 5, 7, 2, 6, 1, 4, 6, 5, 4, 9, 6, 1, 6, 7, 5, 6, 3, 9, 6, 7, 8, 4, 5, 6, 1, 6, 2, 5, 2, 8, 3, 6, 1, 2, 4, 5, 3, 0, 6, 9, 7, 0, 3, 2, 3, 9, 5, 1, 6, 4, 5, 0, 8, 1, 1, 1, 2, 4, 6, 1, 0, 2, 9, 9, 9, 0, 4, 5, 7, 3, 8, 9, 6, 2, 8, 1, 8, 1, 4, 2, 9, 7]
FIFO  81  page faults.
LRU  79  page faults.
OPT  56  page faults.
'''
                      
