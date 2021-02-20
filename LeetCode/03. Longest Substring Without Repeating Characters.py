class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrs = []
        result = 0
        for i in s:
            if i in chrs:
                if len(chrs) > result :
                    result = len(chrs)
                chrs = chrs[chrs.index(i)+1:] # 겹치는 str나오면 그 str 기준으로 앞의 것 전부 날림
                chrs.append(i)
            else:
                chrs.append(i)
        if len(chrs) > result :
            result = len(chrs)
        return result

    # chrs 변화 예시
    # 입력이 abcabcbb 일때
    #   a
    #   a b
    #   a b c
    #   b c a
    #   c a b
    #   a b c
    #   c b
    #   b