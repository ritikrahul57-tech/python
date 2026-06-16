x="python"
y="is"
z="awesome"
print(x,y,z)


x='python'
y='is'
z='awesome'
print(x+y+z)


x=7
z=2
print(x+z)


x=6
z='rahul'
print(x+z)  #this one will be a error


x=6
z='rahul'
print(x,z)


x='easy one'
def myfunc():
    print('python is'+x)
myfunc()


x='easy one'
def myfunc():
    x='awesome'
    print('python is'+x)
myfunc()
print('python is'+x)


def func():
    global x
    x='esay one'
myfunc()
print('python is'+x)    



x='awesome'
def myfunc():
    global x
    x='easy one'
myfunc()
print('python is'+x)



