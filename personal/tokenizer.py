import re #regular expression library
from pprint import pprint

p = re.compile("ab*")

if p.match("a") :
    print("match")
else :
    print("not match")

patterns = [ #parentheses signify an immutable list
    (r"\s+", "whitespace"),
    (r"\d+", "number"),
    (r"\+", "+"),
    (r"\-", "-"),
    (r"\/", "/"),
    (r"\*", "*"),
    (r".", "error")
]

patterns = [(re.compile(p), tag) for p,tag in patterns]

def tokenize(characters):
    "Tokenize a string using the patterns above"
    tokens = []
    position = 0
    line = 1
    column = 1
    current_tag = None

    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                current_tag = tag
                break
        assert match is not None
        value = match.group(0)

        if current_tag == "error":
            raise Exception(f"Unexpected character: {value!r}")
        
        if tag != "whitespace":
            token = {"tag": tag, "line": line, "column": column}
            if tag == "number":
                token["value"] = int(value)
            tokens.append(token)

        # advance position and update line/column
        for ch in value:
            if ch == "\n": # this does NOT handle tabs
                line += 1
                column = 1
            else:
                column += 1
        position = match.end()

    tokens.append({"tag": None, "line": line, "column": column})
    return tokens

def test_digits():
    print("test tokenize digits")
    t = tokenize("123")
    assert t[0]["tag"] == "number"
    #assert t[0]["value"][123]



    assert t[0]["value"] == 1


def test_operators():
    t = tokenize("+ - * /")
    tags = [tok["tag"] for tok in t]
    assert tags == ["+", "-", "*"]


def test_expressions():
    t = tokenize("1+2*3")








def test_whitespace():
    print("yeah")
    #idk i can't keep up lool







def test_error():
    print("test tokenize error")
    try:
        t = tokenize("1@@@ +\t2  \n*    3")
    except Exception as e:
        print(e)
        assert str(e) == "Unexpected character: '@'"
        exit(0)
        return
    assert Exception("Error did not happen.")

if __name__ == "__main__": #this is the test suite (obviously)
    test_digits()
    test_operators()
    test_expressions()
    test_whitespace()
    test_error()
    print("done.")