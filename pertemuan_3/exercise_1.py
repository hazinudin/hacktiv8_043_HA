def reverse(input_str):
    input_str = str(input_str)

    result = ''
    for str_i in range(len(input_str)-1, -1, -1):
        char = input_str[str_i]
        result += char

    print(result)

reverse('siapa saya')
reverse('indonesia raya')
reverse('wadidaw')