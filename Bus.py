"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2000/B ------------------------------

In Berland, a bus consists of a row of n seats numbered from 1 to n. Passengers are advised to always board the bus following these rules:

If there are no occupied seats in the bus, a passenger can sit in any free seat;
Otherwise, a passenger should sit in any free seat that has at least one occupied neighboring seat. In other words, 
a passenger can sit in a seat with index i (1 ≤ i ≤ n) only if at least one of the seats with indices i−1 or i+1 is occupied.
Today, n passengers boarded the bus. The array a chronologically records the seat numbers they occupied. That is, a1 contains the seat number where the first passenger sat, 
a2 — the seat number where the second passenger sat, and so on.

You know the contents of the array a. Determine whether all passengers followed the recommendations.

For example, if n = 5, and a = [5,4,2,1,3], then the recommendations were not followed, as the 3-rd passenger sat in seat number 2, while the neighboring seats with numbers 1 and 3 were free.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The following describes the input test cases.

The first line of each test case contains exactly one integer n (1 ≤ n ≤ 2⋅10^5) — the number of seats in the bus and the number of passengers who boarded the bus.

The second line of each test case contains n distinct integers a(i) (1 ≤ a(i) ≤ n) — the seats that the passengers occupied in chronological order.

It is guaranteed that the sum of n values across all test cases does not exceed 2⋅10^5, and that no passenger sits in an already occupied seat.

Output
For each test case, output on a separate line:

"YES", if all passengers followed the recommendations;
"NO" otherwise.
You may output the answer in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer)

Input:
4
5
5 4 2 1 3
3
2 3 1
4
2 3 1 4
5
1 2 3 5 4

Output:
NO
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set()
    tempSet.add(arr[0])
    ok = True
    for i in range(1, sze):
        t = arr[i]
        before = t - 1
        after = t + 1
        if(before in tempSet or after in tempSet):
            tempSet.add(t)
        else:
            ok = False
            break
    print("YES" if ok else "NO")