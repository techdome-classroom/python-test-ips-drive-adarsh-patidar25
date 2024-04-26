def longest_substring(s: str) -> int:
    
    def longest_substring_without_repeating(s):
        if not s:
            return 0
    
    max_length = 0
    start = 0
    char_index_map = {}
    
    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length





