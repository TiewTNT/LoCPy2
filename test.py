import time
import re

def gcd(x, y):

    for i in range(abs(min(x, y)), -1, -1):
        if x % i == 0 and y % i == 0:
            return i
       
def lcm(x, y):
    lx = set()
    ly = set()   
    i = 1
    while True:
        lx.add(x * i)
        ly.add(y * i)
        if len(lx.intersection(ly)) == 1:
            return lx.intersection(ly).pop()
        i += 1

    

def enum(l):
    return list(enumerate(l))

def phone_num_probs1(num):  
    if type(num) != str:
        raise TypeError('It should be a string.')
    try:
        if re.search('\+\d\d', num).pos:
            raise LookupError('You should have the country code as well.')
    except AttributeError:
        raise LookupError('Country code pattern not found.')
    if not re.match('\+\d\d\d\d\d\d\d\d\d\d\d\d', num):
        raise ValueError('Incorrect pattern.')
    if len(num) != 13:
        raise IndexError('Check the phone number\'s length.')

    if num.startswith('+66'):
        return 'Thailand'
    elif num.startswith('+34'):
        return 'Spain'
    else:
        return 'Other'

def phone_num_probs2(num):  
    assert type(num) == str
    assert num.startswith('+')
    assert len(num) == 13
    assert re.match('\+\d\d\d\d\d\d\d\d\d\d\d\d', num)

    if num.startswith('+66'):
        return 'Thailand'
    elif num.startswith('+34'):
        return 'Spain'
    else:
        return 'Other'
    
def do_something(x):
    answer = 0
    try:
        array = [x, x ** 0, x // x , x % (x - 4), [x]]
        for i in range(x):
            answer += array[i]
    except ZeroDivisionError:
        print('I think you tried to divide by zero.')
    except TypeError:
        print('The last item in array is a list.')
    else:
        print('No Errors')

    return answer

def euclidean(x, y):
    while y != 0:
        x, y = y, x % y
    return x

time_start = time.time()
print(lcm(6, 27))
print(time.time() - time_start)

def foo(*args, **kwargs):
    print(type(args), type(kwargs))
foo()


