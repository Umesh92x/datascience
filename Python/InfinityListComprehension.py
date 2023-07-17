# how to create a Infinity List Comprehension

input_list = [1,2,3]
[input_list.append(value) for value in input_list] # Taking item from the input list and appending into the same list  

Output -> Keep running...until outside keyboard or kernel interruption 


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
    print("Code execution timed out due to over running for 5 mins")

output -> Code execution timed out due to over running for 5 mins
