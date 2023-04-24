# Author: Thabang Thubane
# Description: This program implements three page replacement algorithms (FIFO, LRU, and OPT) 
# Usage: To run the program, execute the following command>>> python paging.py [number of page frames] [num pages in ref str]
# For example: python paging.py 3 100  >>>>>  This will simulate the three page replacement algorithms with a virtual memory
# of 3 pages and a reference string of 100 pages.
# Date: April 24, 2023

import numpy as np
import sys

# FIFO page replacement algorithm
def FIFO(size, pages):
    pgsInMem = []   # list to keep track of pages currently in memory
    pageFaults = 0  # counter to keep track of page faults

    for i in pages:
        if i in pgsInMem:
            pass   # page already in memory, no page fault

        elif len(pgsInMem) != size: # there's still space
            pgsInMem.append(i)

            pageFaults += 1

        else:
            pgsInMem.remove(pgsInMem[0])  # remove oldest page in memory
            pgsInMem.append(i)   # add current page to memory

            pageFaults += 1

    return pageFaults


# LRU page replacement algorithm
def LRU(size, pages):
    pgsInMem = []  # list to keep track of pages currently in memory
    pageFaults = 0  # counter to keep track of page faults

    for i in pages:
        if i in pgsInMem:
            pgsInMem.remove(i)  # remove current page from memory
            pgsInMem.append(i)  # add current page to end of memory (most recently used)

        elif len(pgsInMem) != size: # there's still space
            pgsInMem.append(i)

            pageFaults += 1

        else:
            pgsInMem.remove(pgsInMem[0])   # remove oldest page in memory
            pgsInMem.append(i)   # add current page to memory

            pageFaults += 1

    return pageFaults

# OPT page replacement algorithm
def OPT(size, pages):
    pgsInMem = []  # List to keep track of pages currently in memory
    ftrIndex = []  # List to keep track of next indexes of pages

    pageFaults = 0

    # Loop through the pages
    for i in range(len(pages)):
        nxtIndex = -1   # Initialize next index of page to -1(indicates index of element not found in the list)
        page = pages[i]     # Get the current page

        # Find the index of the next occurrence of the page
        try:
            nxtIndex = pages[i+1:].index(page) + (i+1)

        except ValueError:
            pass
        
        # Update future index of page in ftrIndex list if it's already in memory
        if page in pgsInMem:
            ftrIndex[pgsInMem.index(page)] = nxtIndex

        # If there is still space in memory, add the current page
        elif len(pgsInMem) != size:
            pgsInMem.append(page)
            ftrIndex.append(nxtIndex)

            pageFaults += 1

        # If there is no space in memory, remove the page with the highest future index
        else:
            maxInd = -1

            # Check if any in mem page will not be referenced again in the future
            if -1 in ftrIndex:
                pass

            else:
                # Find the page in mem with the maximum future index
                maxInd = max(ftrIndex)

            # index of page in mem that will either not be referenced again in the future or 
            #that will not be used for the longest period of time in future
            temp = ftrIndex.index(maxInd)

            # remove the page with the highest future index from mem (and it's ftr index from ftrInd list) 
            # and add the current page to memory
            pgsInMem.remove(pgsInMem[temp])
            ftrIndex.remove(maxInd)
            
            pgsInMem.append(page)
            ftrIndex.append(nxtIndex)

            pageFaults += 1

    return pageFaults


def main():

    size = int(sys.argv[1]) #number of page frames
    numOfPages = int(sys.argv[2]) #num pages in ref str

    pages = list(np.random.randint(low = 0,high=10,size=numOfPages))

    print(pages)

    print('FIFO ', FIFO(size, pages), ' page faults.')
    print('LRU ', LRU(size, pages), ' page faults.')
    print('OPT ', OPT(size, pages), ' page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paging.py [number of page frames] [num pages in ref str]")
    else: 
        main()
