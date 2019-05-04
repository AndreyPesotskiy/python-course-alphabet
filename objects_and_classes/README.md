# OBJECT and CLASSES

# Talk about tests and homework 

- Python is an object oriented programming language.

- Almost everything in Python is an object, with its properties and methods.

- Every object has its own class

- Class and type - is the same

- Class it is a template to create an object 

- Object of class - unique object for one class/type

- You could have any amount of instances for specific class. P.S. If programmer did not limited it progra

### Object lifetime 
    __new__ 
    __init__
    __del__
    
### Context manager
    __enter__
    __exit__
    
### Representation of object
    str
    repr
    talk about eval

### Comparing custom types
    >
    <
    ==
    !=
    
### Iterators
    __next__
    __iter__
    __contain__
    
    
  
### Classmethod and static method (bonus)
### Useful inks
 - list of magic methods https://www.tutorialsteacher.com/python/magic-methods-in-python
    >>> import uuid
    >>> uuid.uuid4()
    UUID('8ca11db2-df96-41e0-b839-f6da1c905cfc')
    >>> a = uuid.uuid4()
    UUID('3be7227a-b034-4f60-906c-38131e4e2278')
    >>> a.hex
