Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
vowels = {"a", "e", "i", "o", "u"}
vowels[1]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    vowels[1]
TypeError: 'set' object is not subscriptable
vowels
{'u', 'i', 'o', 'e', 'a'}
vowels
{'u', 'i', 'o', 'e', 'a'}
vowels
{'u', 'i', 'o', 'e', 'a'}
print(vowels)
{'u', 'i', 'o', 'e', 'a'}
empty = set()
vowels1 = "aeiou"
vowels1
'aeiou'
vowels1 = {"aeiou"}
vowels1
{'aeiou'}
vowels = set("a", "e", "i", "o", "u")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    vowels = set("a", "e", "i", "o", "u")
TypeError: set expected at most 1 argument, got 5
letters = {ch(x) for x in range(ord("a"), ord("z")+1}
           
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
letters = {ch(x) for x in range(ord("a"), ord("z")+1)}
           
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    letters = {ch(x) for x in range(ord("a"), ord("z")+1)}
  File "<pyshell#13>", line 1, in <setcomp>
    letters = {ch(x) for x in range(ord("a"), ord("z")+1)}
NameError: name 'ch' is not defined. Did you mean: 'chr'?
letters = {chr(x) for x in range(ord("a"), ord("z")+1)}
           
letters
           
{'p', 'c', 't', 'a', 'h', 'o', 'b', 'm', 'e', 'n', 'd', 'y', 'k', 'q', 'u', 's', 'j', 'g', 'v', 'r', 'i', 'f', 'w', 'z', 'x', 'l'}
numbers = {x for x in range(1, 11)}
           
numbers
           
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
words = {"a", "u"}
           
words >=vowels
           
False
words <= vowels
           
True
num1 = {1, 2, 3}
           
num2 = {4, 5, 6}
           
u = num1.union(num2)
           
u
           
{1, 2, 3, 4, 5, 6}
letters <= {"a", "e", "i", "o", "u"}
           
False


letters >= {"a", "e", "i", "o", "u"}
           
True
num1.update(num2)
           
num1
           
{1, 2, 3, 4, 5, 6}
powers = {x: x ** x for x in range(2,8)}
           
powers
           
{2: 4, 3: 27, 4: 256, 5: 3125, 6: 46656, 7: 823543}
powers = {x: x ** 2 for x in range(2,8)}
           
powers
           
{2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
stock = {"apple":10, "banana":15, "orange":11 }
           
stock["apple"]
           
10
sotck[0]
           
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sotck[0]
NameError: name 'sotck' is not defined. Did you mean: 'stock'?
stock = dict({"apple":10, "banana":15, "orange":11})
           
stock
           
{'apple': 10, 'banana': 15, 'orange': 11}
stock = dict(apple=10, banana=15, orange=11)
           
stock
           
{'apple': 10, 'banana': 15, 'orange': 11}
stock = dict([("apple",10), ("banana",15), ("orange",11)])
           
stock
           
{'apple': 10, 'banana': 15, 'orange': 11}
stock = dict(apple=10, banana=15, 78=11)
           
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
stock = dict(apple=10, banana=15, p78=11)
           
stock
           
{'apple': 10, 'banana': 15, 'p78': 11}
stock = dict(apple=10, banana=15, "678"=11)
           
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
stock = dict([("apple",10), ("banana",15), ("orange",11)])
           
stock["pear"] = 50
           
stock
           
{'apple': 10, 'banana': 15, 'orange': 11, 'pear': 50}
stock["apple"] += 1
           
stock
           
{'apple': 11, 'banana': 15, 'orange': 11, 'pear': 50}
del stock["orange"]
           
stock
           
{'apple': 11, 'banana': 15, 'pear': 50}
if "apple" in stock:
    print("Apple stock level is", stock["apple"])

           
Apple stock level is 11
stock(keys)
           
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    stock(keys)
NameError: name 'keys' is not defined
stock[keys]
           
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    stock[keys]
NameError: name 'keys' is not defined
stock.keys
           
<built-in method keys of dict object at 0x00000257DA41A4C0>
stock.keys()
           
dict_keys(['apple', 'banana', 'pear'])
stock.value()
           
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    stock.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
stock.values()
           
dict_values([11, 15, 50])
if 11 in stock.values():
    print("Apple stock level is", stock["apple"])

           
Apple stock level is 11
stock.items()
           
dict_items([('apple', 11), ('banana', 15), ('pear', 50)])
for item in stock:
    print(item)

           
apple
banana
pear
for level in stock.values():
    print(level)

           
11
15
50
def multiple(a, **b):
    print(a*b)

    
multiple(4)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    multiple(4)
  File "<pyshell#74>", line 2, in multiple
    print(a*b)
TypeError: unsupported operand type(s) for *: 'int' and 'dict'
def show_details(title="Details", **info):
    print(title)
    for name in info:
        print(name, ":", info[name])

        
show_details(title="Info", msg="file created", err="no issues")
Info
msg : file created
err : no issues
show_details(msg="file created", err="no issues")
Details
msg : file created
err : no issues
def show_details(title="Details", **info):
    print(title)
    for name in info:
        print(name, ":", info[name])
    print(info)

    
show_details(title="Info", msg="file created", err="no issues")
Info
msg : file created
err : no issues
{'msg': 'file created', 'err': 'no issues'}
show_details(title="Info", msg="file created", err="no issues", success = "with no error")
Info
msg : file created
err : no issues
success : with no error
{'msg': 'file created', 'err': 'no issues', 'success': 'with no error'}
