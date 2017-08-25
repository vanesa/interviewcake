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

parens: {'(' : ')', '[' : ']', '{' : '}'}

"""
import unittest


def parens_balance(str1, parenDict):
    tracker = []
    
    if str1[0] in parenDict.values():
        return False

    valid_parens = set()

    for k, v in parenDict.items():
        valid_parens.add(k)
        valid_parens.add(v)
    
    for p in str1:
        if p not in valid_parens:
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

parens = {'(' : ')', '[' : ']', '{' : '}'}

class Test(unittest.TestCase):
    data = [
            (["[](){}", parens], True),
            (["[(])", parens], False),
            (["[({})]", parens], True),
            (["[()[]{}]", parens], True),
            (["[](){}[({})][](){}", parens], True),
            (["dfaa(a2222das)adcxa", parens], True),
            ([")(", parens], False)
        ]

    def test_parens_balance(self):
        for [[str1, parenDict], expected] in self.data:
            actual = parens_balance(str1, parenDict)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()