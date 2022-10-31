'''
First, def a function, shut_down, that takes one argument s. Then, if the shut_down function
receives an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no",
then the function should return "Shutdown aborted". Finally, if shut_down gets anything other
than those inputs, the function should return "Sorry".
'''
def shut_down(s):
    if s == 'yes':
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"



