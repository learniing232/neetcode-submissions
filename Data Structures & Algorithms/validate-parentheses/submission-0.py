class Solution:
    def isValid(self, s: str) -> bool:
        bracket_guide = {'{':'}', '(':')', '[':']'}
        st = []
        for br in s:
            if br in bracket_guide or len(st)==0:
                st.append(br)
            else:
                if br!=bracket_guide.get(st[-1]):
                    return False
                else:
                    st.pop()
        if len(st)!=0:
            return False
        return True