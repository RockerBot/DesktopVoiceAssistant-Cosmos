def talk(txt: str) -> str:
    return txt


operators = {
    'plus': '+', '+': '+', 'and': '+',
    'minus': '-', '-': '-',
    'into': '*', 'x': '*', '*': '*', 'times': '*', 'of': '*',
    'by': '/', '/': '/', 'mod': '%', 'percent': '*0.01',
    'dot': '.', 'point': '.', '.': '.',
    'power': '**', 'square': '**2', 'cube': '**3', 'root': '**(-1)',
    'hole': ')'
}

operands = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16',
    'seventeen': '17', 'eighteen': '18', 'nineteen': '19', 'twenty': '20', 'thirty': '30', 'fourty': '40', 'fifty': '50',
    'sixty': '60', 'seventy': '70', 'eighty': '80', 'ninety': '90',
    'hundred': '0' * 2, 'thousand': '0' * 3, 'lakhs': '0' * 5, 'lakh': '0' * 5, 'lacs': '0' * 5, 'lac': '0' * 5,
    'crores': '0' * 7, 'crore': '0' * 7, 'million': '0' * 6, 'billion': '0' * 9, 'trillion': '0' * 12,
    'quadrillion': '0' * 15, 'quintillion': '0' * 18, 'sextillion': '0' * 21, 'septillion': '0' * 24,
    'octillion': '0' * 27, 'nonillion': '0' * 30, 'decillion': '0' * 33, 'undecillion': '0' * 36,
    'duodecillion': '0' * 39, 'tredecillion': '0' * 42, 'quattuordecillion': '0' * 45, 'quindecillion': '0' * 48,
    'sexdecillion': '0' * 51, 'septendecillion': '0' * 54, 'octodecillion': '0' * 57, 'novemdecillion': '0' * 60,
    'vigintillion': '0' * 63, 'googol': '0' * 100, 'centillion': '0' * 303
}


def debug(*val):
    print(*val)


def replace_all(text, *values, new_value="", isword=True):
    """removes all instances of values in the text with the new_value
        if isword=True, replaces only if the word is present and not the set of characters"""
    if isword:
        return ' '.join(map(lambda x: (x, new_value)[x in [i.strip() for i in values]], text.split()))
    for value in values:
        text = text.replace(value, new_value)
    return text


def has(list1, *list2, check=any, isword=True):
    """creates a tuple of boolean values: True, if element in list2 is present in list1 else False
        and operates a given function on the iterable
        if isword=True, checks if the words in the string are present
        check=any, returns True if any item in the iterable is True else False
        check=all, returns True if all items in the iterable are True else False"""
    if is_str := type(list1) == str:
        list1 = f' {list1.strip()} '
    if isword and is_str and not any(type(i) != str for i in list2):
        list1 = list1.split()
    return check(i in list1 for i in list2)


command = "three hundred and sixty five thousand four hundred and seven"
# command = input()

command = replace_all(command, 'calculate', 'evaluate', 'expression', 'the')
command = replace_all(command, 'whole', new_value='hole')
command = replace_all(command, 'squared', new_value='square')
command = replace_all(command, 'cubed', new_value='cube')
command = replace_all(command, 'a', new_value='one').strip()
elems = command.split()

val = None
i = 0
while i < len(elems):
    debug(elems)
    if not (val:=operators.get(elems[i])) and elems[i].isalpha():

    elif not (val:=operands.get(elems[i])) and elems[i].isalpha():
        elems.pop(i)

    elems[i] = val if val else elems[i].replace('%', '*0.01')
    i += 1
command = ''.join(elems)
command = '(' * (command.count(')') - command.count('(')) + command.replace('***', '**')
try:
    debug(command, '=', talk(str(eval(command))))
except Exception as e:
    debug(talk(str(e)))
