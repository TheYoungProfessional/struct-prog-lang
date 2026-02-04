#parser.py

from tokenizer import tokenize

#EBNF

# expression  = term { ("+" | "-") term }
# term        = factor {("*" | "/") factor }
# factor      = <number>