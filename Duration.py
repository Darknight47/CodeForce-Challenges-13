"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1690/C ------------------------------------------------

Recently, Polycarp completed n successive tasks.

For each completed task, the time s(i) is known when it was given, no two tasks were given at the same time. Also given is the time f(i) when the task was completed. 
For each task, there is an unknown value d(i) (d(i) > 0) — duration of task execution.

It is known that the tasks were completed in the order in which they came. Polycarp performed the tasks as follows:

As soon as the very first task came, Polycarp immediately began to carry it out.
If a new task arrived before Polycarp finished the previous one, he put the new task at the end of the queue.
When Polycarp finished executing the next task and the queue was not empty, he immediately took a new task from the head of the queue (if the queue is empty — he just waited for the next task).
Find d(i) (duration) of each task.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The descriptions of the input data sets follow.

The first line of each test case contains one integer n (1 ≤ n ≤ 2⋅10^5).

The second line of each test case contains exactly n integers s1<s2<⋯<sn (0 ≤ s(i) ≤ 10^9).

The third line of each test case contains exactly n integers f1<f2<⋯<fn (s(i) < f(i) ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each of t test cases print n positive integers d1,d2,…,dn — the duration of each task.

Input:
4
3
0 3 7
2 10 11
2
10 15
11 16
9
12 16 90 195 1456 1569 3001 5237 19275
13 199 200 260 9100 10000 10914 91066 5735533
1
0
1000000000

Output:
2 7 1 
1 1 
1 183 1 60 7644 900 914 80152 5644467 
1000000000 
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    ans = []
    ans.append(arr2[0] - arr1[0])
    for i in range(sze - 1):
        first = arr1[i]
        firstTime = arr2[i]
        second = arr1[i + 1]
        secondTime = arr2[i + 1]
        if(second < firstTime):
            ans.append(secondTime - firstTime)
        else:
            ans.append(secondTime - second)
    print(*ans)