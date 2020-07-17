def word_reversal(value: str) -> str:
    words_list = value.split(' ')
    result: str = ""

    for word in words_list:
        result += f'{word[::-1]} '

    return result


print(word_reversal('This is an   example!'))
print(word_reversal('double  spaces'))
