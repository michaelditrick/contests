"""sumary_line
Input
The input consists of several test cases. Each test case consists of two lines, first a non-empty pattern, then a non-empty text. Input is terminated by end-of-file. The input file will not be larger than 5 Mb.

Output
For each test case, output one line containing the positions of all the occurences of pattern in text, from first to last, separated by a single space.
"""





import sys

def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(pattern, text):
    M, N = len(pattern), len(text)
    lps = compute_lps_array(pattern)
    result = []
    i, j = 0, 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            result.append(str(i - j))
            j = lps[j - 1]
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

if __name__ == "__main__":
    for line in sys.stdin:
        pattern = line.strip()
        text = sys.stdin.readline().strip()
        positions = kmp_search(pattern, text)
        print(" ".join(positions))
