def kmp_algorithm(text, pattern):
    def compute_lps(pat):
        lps = [0] * len(pat)
        length = 0
        for i in range(1, len(pat)):
            while length > 0 and pat[i] != pat[length]:
                length = lps[length - 1]
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            j = lps[j - 1] if j > 0 else 0
            if j == 0:
                i += 1
    return -1

# Test
text = "hello world"
pattern = "hello"
result = kmp_algorithm(text, pattern)
print(f"Pattern found at index {result}" if result != -1 else "Pattern not found")

