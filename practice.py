import requests
response = requests.get("https://www.gutenberg.org/files/3201/files/COMMON.TXT")
response.text
words = response.text.split('\r\n')
print(words)
len(words)

def less_than_20(words:list[str]):
    new_list = []
    for i in words:
        if len(i)>20:
            new_list.append(i)
    return new_list

print(less_than_20(words))

def has_no_e(list_from_above:list):
    length_before = len(list_from_above)
    new_list = []
    for word in list_from_above:
        for letter in word:
            if letter in 'eE':
                break
        else:
            new_list.append(word)
    return new_list
print(has_no_e(less_than_20(words)))


