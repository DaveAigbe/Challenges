"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given

scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains
. The second line contains n an array A[] of n integers each separated by a space"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    while arr:
        arr = list(dict.fromkeys(arr))

        arr.remove(max(arr))

        break

    print(max(arr))