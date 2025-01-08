>>> my_dict = {'dog': 'barks', 'cat': 'meows', 'pig': 'oinks',}
>>> my_dict
{'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}

>>> my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    ],
    'first_season': 1969,
    'second_season': 1974,
    'reboot_season': None,

    }
#produced this
>>> my_dict
{'title': "Monty Python's Flying Circus", 'cast': ['Eric Idle', 'John Cleese', 'Terry Gilliam', 'Graham Chapman', 'Michael Palin', 'Terry Jones'], 'first_season': 1969, 'second_season': 1974, 'reboot_season': None}

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

>>> my_dict
{'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}

>>> my_dict['pig']
'oinks'
>>> my_dict['bird']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'bird'

>>> my_dict
{'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}
>>> my_dict['cat'] = 'purrs'
>>> my_dict 
{'dog': 'barks', 'cat': 'purrs', 'pig': 'oinks'}
>>>

>>> dic = {}
>>> dic['a'] = 1
>>> dic['b'] = 2
>>> print(dic)
{'a': 1, 'b': 2}
>>> del dic['a']
>>> dic['a'] = 1
>>> print(dic)
{'b': 2, 'a': 1}
>>>