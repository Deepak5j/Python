# txt = "We are the so-called "Vikings" from the north."
# above will result in erro. use escape character \
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# raw string created as escape chars are used
# 'r' begenning of '''
escape_cahrs = r''' 
\' single quote
\\ backslash
\n New Line
\r Carriage Return
\t Tab
\f Form Feed
\ooo Ocatal Value
\xhh Hex value
'''
print(escape_cahrs)
