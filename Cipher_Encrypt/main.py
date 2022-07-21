alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

text = input("Enter the code")
shift = int(input("Enter the shift number"))
choice = input("Enter the choice decode or encode")
new_text = ''
ask = 'yes'


def numb(n, shift_by):
    if choice == 'decode':
        num = n + shift_by
        if shift_by > 25:
            num -= 26
    elif choice == 'encode':
        num = n - shift_by
        if shift_by < 0:
            num += 26
    return num


while ask == 'yes':
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                new_text += alphabet[numb(i, shift)]
    print(new_text)
    ask = input("Do you want to continue Yes or No").lower()

    if ask == 'yes':
        text = input("Enter the code")
        shift = int(input("Enter the shift number"))
        choice = input("Enter the choice decode or encode")
        new_text = ''



