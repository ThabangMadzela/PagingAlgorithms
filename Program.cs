using System;
using System.Collections.Generic;
using System.Linq;

namespace PageReplacementAlgorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 2)
            {
                Console.WriteLine("Usage: dotnet run [number of page frames] [num pages in ref str]");
                return;
            }

            int size = int.Parse(args[0]); // number of page frames
            int numOfPages = int.Parse(args[1]); // number of pages in the reference string

            List<int> pages = GenerateRandomPages(numOfPages);

            Console.WriteLine(string.Join(", ", pages));
            Console.WriteLine($"FIFO: {FIFO(size, pages)} page faults.");
            Console.WriteLine($"LRU: {LRU(size, pages)} page faults.");
            Console.WriteLine($"OPT: {OPT(size, pages)} page faults.");
        }

        static List<int> GenerateRandomPages(int numOfPages)
        {
            Random random = new Random();
            return Enumerable.Range(0, numOfPages).Select(_ => random.Next(0, 10)).ToList();
        }

        static int FIFO(int size, List<int> pages)
        {
            Queue<int> pgsInMem = new Queue<int>();
            int pageFaults = 0;

            foreach (int page in pages)
            {
                if (pgsInMem.Contains(page))
                {
                    continue; // page already in memory, no page fault
                }

                if (pgsInMem.Count != size)
                {
                    pgsInMem.Enqueue(page);
                    pageFaults++;
                }
                else
                {
                    pgsInMem.Dequeue();
                    pgsInMem.Enqueue(page);
                    pageFaults++;
                }
            }

            return pageFaults;
        }

        static int LRU(int size, List<int> pages)
        {
            List<int> pgsInMem = new List<int>();
            int pageFaults = 0;

            foreach (int page in pages)
            {
                if (pgsInMem.Contains(page))
                {
                    pgsInMem.Remove(page);
                    pgsInMem.Add(page);
                }
                else if (pgsInMem.Count != size)
                {
                    pgsInMem.Add(page);
                    pageFaults++;
                }
                else
                {
                    pgsInMem.RemoveAt(0);
                    pgsInMem.Add(page);
                    pageFaults++;
                }
            }

            return pageFaults;
        }

        static int OPT(int size, List<int> pages)
        {
            List<int> pgsInMem = new List<int>();
            List<int> ftrIndex = new List<int>();
            int pageFaults = 0;

            for (int i = 0; i < pages.Count; i++)
            {
                int nxtIndex = -1;
                int page = pages[i];

                try
                {
                    nxtIndex = pages.IndexOf(page, i + 1) + (i + 1);
                }
                catch (Exception)
                {
                }

                if (pgsInMem.Contains(page))
                {
                    ftrIndex[pgsInMem.IndexOf(page)] = nxtIndex;
                }
                else if (pgsInMem.Count != size)
                {
                    pgsInMem.Add(page);
                    ftrIndex.Add(nxtIndex);
                    pageFaults++;
                }
                else
                {
                    int maxInd = -1;

                    if (ftrIndex.Contains(-1))
                    {
                        // Check if any page in memory will not be referenced again in the future
                    }
                    else
                    {
                        maxInd = ftrIndex.Max();
                    }

                    int temp = ftrIndex.IndexOf(maxInd);
                    pgsInMem.RemoveAt(temp);
                    ftrIndex.RemoveAt(temp);

                    pgsInMem.Add(page);
                    ftrIndex.Add(nxtIndex);
                    pageFaults++;
                }
            }

            return pageFaults;
        }
    }
}
