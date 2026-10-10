class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        op='+'
        num=0
        for i in range(len(s)+1):
            ch= '+' if i==len(s) else s[i]

            if ch.isdigit():
                num=num*10+int(ch)
            elif ch!=' ':
                if op=='+':
                    st.append(num)
                elif op=='-':
                    st.append(-num)
                elif op=='/':
                    st.append(int(st.pop()/num))
                elif op=='*':
                    st.append(st.pop()*num)
                num=0
                op=ch
        return sum(st)