def merge(left, right, reverse=False):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j] and not reverse) or (left[i] > right[j] and reverse):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements from both lists
    result.extend(left[i:])
    result.extend(right[j:])
    return result





def merge_sort(data):
    if len(data) <= 1:
        return data

    # Find the middle point to divide the list
    mid = len(data) // 2

    # Recursively call merge_sort to sort the left half
    left = merge_sort(data[:mid])

    # Recursively call merge_sort to sort the right half
    right = merge_sort(data[mid:])

    # Merge the two sorted halves
    return merge(left, right)

def bubble_sort(data: list, reverse=False):
    n = len(data)
    for i in range(n):
        swapped = False
        for k in range(n-1-i):
            if data[k+1] < data[k]:
                data[k], data[k + 1] = data[k + 1], data[k]
                swapped = True
        if not swapped:
            break
    return data


def bisect_search(sorted_data: list, value) -> int:
    low, high = 0, len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        mid_value = sorted_data[mid]

        if mid_value == value:  # Value found
            return mid
        elif mid_value < value:  # Value is in the right half
            low = mid + 1
        else:  # Value is in the left half
            high = mid - 1

    return -1  # Value not found


def ngrams(word: str) -> list[str]:
    """Returns a list of n-grams of word for all relevant n, in descending order of n."""
    return [word[i:i+n] for n in range(len(word), 0, -1) for i in range(0, len(word) - n + 1)]


#     # [TODO] Add code here to add a word to the index


def add_to_index(option: str, index: dict[str, list[str]]) -> None:
    """Adds a valid option to the n-gram index."""
    # [TODO] Add code here to add a word to the index
    for individual_ngram in ngrams(option):
        index[individual_ngram].append(option)





def build_index(options: list[str]) -> dict[str, list[str]]:
    """Creates an n-gram index from options.
    The n-gram index will be a dictionary with n-grams as keys, and lists of corrosponding options as values."""
    index = defaultdict(list)
    # [TODO] Add code here to build up the index, using add_to_index
    for words in options:
        add_to_index(words, index)

    return index


def fuzzy_pick(query: str, index: dict) -> dict[str,str]:
    """Returns suggestions for valid options based on the query string.
    Suggestions will take the form of a dictionary with suggestions as keys and longest matching ngram as the value"""
    suggestions = {}

    for ngrams_made in ngrams(query):
        if ngrams_made in index:
            for options in index[ngrams_made]:
                if options not in suggestions or len(ngrams_made)>len(suggestions[options]):
                    suggestions[options]=ngrams_made
    return suggestions





def comp(query: str, dunders=False) -> None:
    """Provides completions for all objections in the current Python REPL session.
    By default, objects starting with underscores are excluded, but this behavior can be adjusted by passing dunders=True"""
    options = dict(inspect.getmembers(inspect.stack()[len(inspect.stack()) - 1][0]))["f_globals"]
    targets = [obj + '.' + attr
               for obj in options.keys()
               for attr in dir(options[obj])
               if dunders or not (obj.startswith('_')
                                  or attr.startswith('_'))]
    index = build_index(targets)
    suggestions = fuzzy_pick(query, index)
    sorted_suggestions = sorted(suggestions.keys(), key=lambda x: len(suggestions[x]), reverse=True)
    longest_match = len(suggestions[sorted_suggestions[0]])
    for suggestion in sorted_suggestions:
        if len(suggestions[suggestion]) >= longest_match - _FUDGE:
            print(suggestion, '(' + suggestions[suggestion] + ')')



def ceasar(string_sample, shift):
"""shifts letters by desired amount"""
    new_string=''
    for i in range(len(string_sample)):
        character=string_sample[i]
        if character in string.ascii_uppercase:
            number=ord(character)
            new_character=chr(((number-65)+shift)%26+65)
            new_string+=new_character
        elif character in string.ascii_lowercase:
            number=ord(character)
            new_character=chr(((number-97)+shift)%26+65)
            new_string+=new_character
        else:
            new_character=character
            new_string+=new_character
    return new_string
