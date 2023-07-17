# how to create a infinity Infinity List Comprehension

input_list = [1,2,3]
[input_list.append(value) for value in input_list] # taking item from input list and appending into into the same list  

Output -> Keep runnning....

''' The solution to add timeout '''


import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Code execution timed out")

try :
    # Set the timeout to 5 seconds
    signal.signal(signal.SIGALRM, timeout_handler) # timeout_handler function will be called when it gets a number say 5 seconds.
    signal.alarm(5)

    input_list = [1,2,3]
    [input_list.append(value) for value in input_list] 
    # Disable the timeout
    signal.alarm(0)
    
except TimeoutError:
    print("Code execution timed out due to over runnig for 5 mins")

output -> Code execution timed out due to over runnig for 5 mins
