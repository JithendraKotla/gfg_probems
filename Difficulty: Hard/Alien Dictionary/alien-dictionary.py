class Solution:
    def findOrder(words):
        # code here
        n=len(words)
        seen=set()
        for i in words:
            for ch in i:
                if ch not in seen:
                    seen.add(ch)
        k=len(seen)
        
        adj=[[] for _ in range(k)]
        chars = list(seen)
        idx_map = {ch: i for i, ch in enumerate(chars)}
        
        for i in range(n-1):
            s1=words[i]
            s2=words[i+1]
            
            shlen=min(len(s1),len(s2))
            if len(s1) > len(s2) and s1[:shlen] == s2[:shlen]:
                return ""  
            
            for ptr in  range(shlen):
                if s1[ptr]!=s2[ptr]:
                    u=idx_map[s1[ptr]]
                    v=idx_map[s2[ptr]]
                    adj[u].append(v)
                    break
        def bfs():
            q=deque()
            inDegree=[0]*k
            
            for i in range(k):
                for nei in adj[i]:
                    inDegree[nei]+=1
            for i in range(k):
                if inDegree[i]==0:
                    q.append(i)
            topo=[]
            while q:
                poped=q.popleft()
                topo.append(poped)
                
                for nei in adj[poped]:
                    inDegree[nei]-=1
                    if inDegree[nei]==0:
                        q.append(nei)
            return topo
        topo=bfs()
        if len(topo)!=k:
            return ""
        res=""
        for i in topo:
            res+=chars[i]
        return res
        
        
            
            
            
            
        
                