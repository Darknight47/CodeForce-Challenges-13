"""
--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2086/A ---------------------------

The most valuable berry of the Karelian forests is cloudberry. To make jam from cloudberries, you take equal amounts of berries and sugar and cook them. 
Thus, if you have 2 kg of berries, you need 2 kg of sugar. However, from 2 kg of berries and 2 kg of sugar, you will not get 4 kg of jam, as one might expect, 
but only 3 kg, since some of the jam evaporates during cooking. Specifically, during standard cooking, exactly a quarter (or 25%) of the jam evaporates.

How many kilograms of cloudberries are needed to prepare n 3-kilogram jars of jam?

Input
Each test consists of several test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The following lines describe the test cases.

Each test case contains a single integer n (1 ≤ n ≤10^8) — the number of jars of jam that need to be prepared.

Output
For each test case, output a single integer — the amount of berries needed for the jam in kilograms.

Input:
2
1
3

Output:
2
6
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    print(num * 2)