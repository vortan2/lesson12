import random
#1
# symbols = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ()!,.&^%$#@*-_=="
# password = ''.join(random.sample(symbols, 12))
# has_small_symbol = False
# has_big_symbol = False
# has_digit = False
# has_special_symbol = False
# for symbol in password:
#     if symbol.islower():
#         has_small_symbol = True
#     elif symbol.isupper():
#         has_big_symbol = True
#     elif symbol.isdigit():
#         has_digit = True
#     else:
#         has_special_symbol = True
# if has_special_symbol and has_small_symbol and has_big_symbol and has_digit:
#     print(f"Пароль успешно сгенерирован: {password}")
# else:
#     print(password)
#2
s = "(((())"
def brackets(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                    print(stack)
                else:
                    return False
            else:
                return False
        else:
            return False
    return not stack
print(brackets(s))