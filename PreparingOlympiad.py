"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2051/A -----------------------------

Monocarp and Stereocarp are preparing for the Olympiad. There are n days left until the Olympiad. On the i-th day, if Monocarp plans to practice, 
he will solve ai problems. Similarly, if Stereocarp plans to practice on the same day, he will solve bi problems.

Monocarp can train on any day he wants. However, Stereocarp watches Monocarp and follows a different schedule: if Monocarp trained on day i and i < n, then Stereocarp will train on day (i+1).

Monocarp wants to organize his training process in a way that the difference between the number of problems he solves and the number of problems Stereocarp solves is as large as possible. Formally, Monocarp wants to maximize the value of (m−s), 
where m is the number of problems he solves, and s is the number of problems Stereocarp solves. Help Monocarp determine the maximum possible difference in the number of solved problems between them.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100).

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100).

The third line contains n integers b1,b2,…,bn (1 ≤ b(i) ≤ 100).

Output
For each test case, print a single integer — the maximum possible difference between the number of problems Monocarp solves and the number of problems Stereocarp solves.
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    firstSum = 0
    secondSum = 0
    for i in range(n - 1):
        first = arr1[i]
        second = arr2[i + 1]
        if(second < first):
            firstSum += first
            secondSum += second
    firstSum += arr1[n - 1]
    print(firstSum - secondSum)