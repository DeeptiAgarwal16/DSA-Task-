class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        l=[]
        for i in range(0,len(s)):
            if s[i] not in l:
                c=s.count(s[i]) 
                d[s[i]]=c
                l.append(s[i])
        d=dict(sorted(d.items(), key=lambda key_val: key_val[1], reverse=True))
        s1=""
        for i in d.keys():
            ss=i*d[i]
            s1+=ss
        return s1
