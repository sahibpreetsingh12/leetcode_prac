class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        new_code = code*3
        length = len(code)
        if k == 0 :
            return [0]*len(code)
        elif k>0 : 
            ls = []
            for i in range(length,length*2):

                l = sum(new_code[i+1:i+1+k])
                ls.append(l)
            return ls
        else:
            res = []
            for i in range(length, 2*length):
                # since k is negative, i+k < i
                l = sum(new_code[i+k : i])
                res.append(l)
            return res


    