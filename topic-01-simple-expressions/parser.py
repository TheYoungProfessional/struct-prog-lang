#parser.py

from tokenizer import tokenize
from pprint import pprint

#EBNF

# expression = term { ("+" | "-") term }
# term = factor { ("*" | "/") factor }
# factor = <number>

def parse_factor(tokens):
  """factor = <number>"""
  token = tokens[0]
  if token["tag"] == "number":
    node = {"tag":"number", "value":token["value"]}
    return node, tokens[1:]
  assert False, f"Expected number, got {token}"

def test_parse_factor():
  """factor = <number>"""
  print("test parse_factor()")
  tokens = tokenize("3")
  ast, token = parse_factor(tokens)
  assert ast == {'tag': 'number', 'value': 3}
  print(tokens)
  exit()

# term = factor { ("*" | "/") factor }
def parse_term(tokens):
  left, tokens = parse_factor(tokens)
  while tokens[0]["tag"] in ["*", "/"]:
    op = tokens[0]["tag"]
    right, tokens = parse_factor(tokens[1:])
    tree = {"tag": op, "left": left, "right": right}
  return left, tokens

def test_parse_term():
  """term = factor { ("*" | "/") factor }"""
  print("test parse_term()")
  tokens = tokenize("3")
  ast, token = parse_term(tokens)
  assert ast == {'tag': 'number', 'value': 3}


if __name__ == "__main__":
  test_parse_factor()
  test_parse_term
  print("done")