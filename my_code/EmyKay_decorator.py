def my_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        print(f'{args}, {kwargs}')
        return original_function(*args, **kwargs)
    return wrapper_function
    
@my_decorator
def display(hello):
    print(f'display function ran, {hello}')
    
    #print(f"inside {__name__}, {args} $$ my_func()\n")
display('welt')

from EmyKaydigi_pringles import IntermediatePhone as Phone

ph = Phone('v', 'v', 'v')

#########################################

#print(dir(ph))

#@my_decorator
class Ph0n3(Phone):
    def __init__(a,b,c):
        super().__init__(a,b,c)
    @my_decorator
    def call(self, recipient):
        super().call(recipient)

myp = Ph0n3('1','2')
myp.call('nlb')