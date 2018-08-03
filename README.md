# Pyfunctions
A collection of useful  python functions tat I've built to fufill a variety of purposes

To import them all, use:
```python
import pyfunctions
pyfunctions.peek(file)
```

or, to import just one:
```python
from pyfunctions import peek
```

## `ExceptionMessage.py`
This contains a simple Exception class to differentiate your exceptions from those of another library or from default exceptions.
To use it:
```python
from pyfunctions import ExceptionMessage

raise ExceptionMessage("Something went wrong")
```

## `Nas.py`
This is a class whhch takes a .wsdl file, builds a client using the `zeep` module, and then logins to the server specified, and then attaches the sessionid to all of the requests sent.
It was designed to make the login portion and handling much easier and more standardized across projects, as well as to make it so the user doesn't have to provide and manage the session id
To use:
```python
from pyfunctions import Nas

nas = Nas()
nas.list_devices({'group': 'global', 'family': 'Cisco IOS'})
# You could make whatever command you want to here.
nas.example_command({'example': 'args'})
```

All of the commands are defined in the  WSDL file, as well as in the documentation for that WSDL file

## `colors.py`
This file provides access to a class that allows the user to access a number of colors for printing.
So the user can print a text in green in the following manner:
```python
from pyfunctions import colors
print colors.GREEN + "I'm GREEN" + colors.END
```

It provides the following colors:
* green
* magenta
* cyan
* blue
* yellow
* red
* bold
* underline
* end

end is used to tell the console to stop printing colors.

## `ensurelocaldir.py`
This provides a function to ensure that a directory exists in the calling file's directory.
So if in folder `/home/bob/scripts/`, I call `ensurelocaldir('logs')` in `mkdir.py`, it would make sure that `/home/bob/scripts/logs` exists, regardless of where you call `mkdir.py`

It is used in the following manner:
```python
from pyfunctions import ensurelocaldir

ensurelocaldir("logs")
```

## `getblocksize.py`
This function takes in a sustring bnet mask, and it computes the corresponding numeric block size.

So if you call `getblocksize("255.255.255.128")`, you would receive back 25.

It is used as follows:
```python
from pyfunctions import getblocksize

print getblocksize("255.255.255.196")
# Outputs 26
```

## `inlist.py`
Similar to the `in` function in python, this merely checks if the passed argument is in any element of the list

I.e.
`inlist('a', ['cat', 'dog']) == True`
`inlist('a', ['dog', 'fox']) == False`

Used as follows:
```python
from pyfunctions import inlist

list = [["cat", "dog"], ["snake", "lizard"]]
if inlist("dog",list):
   print "We have a dog"
```

## `ipand.py`
Performs the AND operation between a string IP address and a string subnet mask, returning a string
I.e.:
`ipand('216.003.128.012','255.255.255.000') -> '216.003.128.000'`

Use it as follows:
```python
from pyfunctions import ipand

ip_address = '123.234.234.124'
subnet_mask = '255.255.128.0'
return ipand(ip_address, subnet_mask)
```

## `openlocal.py`
Identical to the `open` command in python, but it makes sure that the file is opened in the same directory as the calling file

```python
from pyfunctions import openlocal

openlocal("logs.txt", 'w')
```

## `parray.py`
Returns a pretty string version of an array
I.e.
`parray(["cat", "dog"]) -> "cat and dog"` 
`parray(["cat", "dog", "mouse"]) -> "cat, dog, and mouse"`

```python
from pyfunctions import parray

print parray(['some', 'array'])
```

## `parsetestlist.py`
This is used to compile a 'test list' for making it efficient to compute the values of the tests

It takes in something like the following:
```python
tests = [{'test': 'some regex string',
          'function': somefunction,
	  'let': 'The first letter of the regex'}}]
```

and it will return the e following:
```python
[[],[],...,[],[{'test': compiledregex.match, 'function': somefunction}],[],...,[]]
```
Where the test is now indexed based on the ascii value of the 'let' field

## `pbad.py`, `pcolor.py`, `pfail.py`, `psucceed.py`, `pwarn.py`
These functions all print out colored text
`pbad` prints out red text. -> Expects to receive a string
`psucceed` prints out green text -> Expects to receive a string
`pwarn` prints out yellow text -> Expects to receive a string
`pfail` prints out red text and then exits -> Expects a receive a string, and optionally an error code
`pcolor` prints out whatever color it receives, followed by the text, and then the `colors.END` described in `colors.py` -> expects to receive a string and a color, which is a string

## `peek.py`
This is used to peek ahead in the file without advancing the file cursor. It expects the file object as a parameter.
It is used to read the next line if you don't want to 'record' that line as read

Use it as follows:
```python
from pyfunctions import peek

file = open ( 'cat.txt', 'r' )

print peek(file)
print file.readline()
# These both produce the same output, regardless of the file
```