"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1388/A ---------------------------------------

Despite his bad reputation, Captain Flint is a friendly person (at least, friendly to animals). Now Captain Flint is searching worthy sailors to join his new crew 
(solely for peaceful purposes). A sailor is considered as worthy if he can solve Flint's task.

Recently, out of blue Captain Flint has been interested in math and even defined a new class of integers. Let's define a positive integer x as nearly prime if it can be represented as p⋅q
, where 1 < p < q and p and q are prime numbers. For example, integers 6 and 10 are nearly primes (since 2⋅3=6 and 2⋅5=10), but integers 1, 3, 4, 16, 17 or 44 are not.

Captain Flint guessed an integer n and asked you: can you represent it as the sum of 4 different positive integers where at least 3 of them should be nearly prime.

Uncle Bogdan easily solved the task and joined the crew. Can you do the same?

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

Next t lines contain test cases — one per line. The first and only line of each test case contains the single integer n (1 ≤ n ≤ 2⋅10^5) — the number Flint guessed.

Output
For each test case print:

YES and 4 different positive integers such that at least 3 of them are nearly prime and their sum is equal to n (if there are multiple answers print any of them);
NO if there is no way to represent n as the sum of 4 different positive integers where at least 3 of them are nearly prime.
You can print each character of YES or NO in any case.

Input:
7
7
23
31
36
44
100
258

Output:
NO
NO
YES
14 10 6 1
YES
5 6 10 15
YES
6 7 10 21
YES
2 10 33 55
YES
10 21 221 6
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    if(num <= 30):
        print("NO")
    else:
        print("YES")
        diff = num - 30
        if(diff == 6 or diff == 10 or diff == 14):
            diff -= 1
            print(6, 10, 15, diff)
        else:
            print(6, 10, 14, diff)