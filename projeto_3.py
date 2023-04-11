Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
python -V
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python -V
NameError: name 'python' is not defined
help
Type help() for interactive help, or help(object) for help about object.
python3 -V
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    python3 -V
NameError: name 'python3' is not defined
Python
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Python
NameError: name 'Python' is not defined
print("ola aluno! bem vindo!!")
ola aluno! bem vindo!!
help()

Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> print
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> print("Brasil ganhou 5 titulos mundiais")
Brasil ganhou 5 titulos mundiais
>>> print("Brasil", "ganhou", "5 titulos mundiais", sep="-")
Brasil-ganhou-5 titulos mundiais
>>> print("Brasil", "ganhou", "5 titulos mundiais", end="/n")
Brasil ganhou 5 titulos mundiais/n
>>> print("Brasil", "ganhou", "5 titulos mundiais", end-"/n")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("Brasil", "ganhou", "5 titulos mundiais", end-"/n")
NameError: name 'end' is not defined
>>> print("Brasil", "ganhou", "5 titulos mundiais", end-"END")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("Brasil", "ganhou", "5 titulos mundiais", end-"END")
NameError: name 'end' is not defined
>>> print("Brasil", "ganhou", "5 titulos mundiais", end="END")
Brasil ganhou 5 titulos mundiaisEND
>>> 
... 

... 
>>> 

>>> 

... 
... 
>>> 

====================================================================== RESTART: Shell ======================================================================
>>> pais = "Italia"
>>> type(pais)
<class 'str'>
>>> quantidade = 4
>>> type(quantidade)
<class 'int'>
>>> print(pais, "ganhou", quantidade, "titulos mundiais")
Italia ganhou 4 titulos mundiais
