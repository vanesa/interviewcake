""""
interviewing.io

input: string, paren hash from opening paren to closing paren. Ignore all non-paren characters.
output: boolean which determines if the string contains balanced parentheses

"dfaa(a2222das)adcxa" => True 
")(" => False

"[](){}" => True
"[(])"   => False 
"[({})]" => True
"[()[]{}]" => True
"[](){}[({})][](){}" => True
str1 = str1[:untilc] + str1[pairc:]

set( ( [ {)

it = [ [, (, ] ]

parens: {'(' : ')', '[' : ']', '{' : '}'}

"""
parens = {'(' : ')', '[' : ']', '{' : '}'}



def parens_balance(str1, parenDict):
    tracker = []
    
    if str1[0] in parenDict.values():
        return False
    
    for p in str1:
        if p not in parenDict.items():
            continue
        if p not in parenDict.values():
            tracker.append(p)
            continue
        if parenDict[tracker.pop()] == p:
            continue
        else:
            return False
        
    if tracker:
        return False
    return True

if __name__ == '__main__':
    print parens_balance('[](){}[({})][](){}', parens)