def division_decarator(func):
    def wrapper(x,y):
        if y>x:
            x,y=y,x
        return func(x,y)
    return wrapper 

@division_decarator
def division(x,y):
    result =x/y
    return result
div=division(2,12)
print(div)