class Solution:
    def simplifyPath(self, path: str) -> str:
        temp =path.split('/')
        result = ''
        for line in temp:
            if line =='..':
                if result =='':
                    continue
                while result[-1] !='/':
                    result= result[:-1]
                result= result[:-1]
            elif line !='' and line != '.':
                result +=('/'+line)

        if len(result)<1:
            return '/'
        else:
            return result