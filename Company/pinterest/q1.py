
import os
import sys


"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""

# Error Messages
invalid_address = """\nInvalid address!
Must be of the format: x.y.z.w:port
    x, y, z, w are integers ranging from 0 and 255, inclusive
    port is an integer ranging from 1 to 65,535, inclusive"""

# Utility Functions

# prints error message to help user identify error in socket address format
def error(message):
    print message

# checks the IP Address integers passed (ie. 127.12.23.43) are in range
def check_ip_ints(ip_ints):
    r = range(0,256)
    for d in ip_ints:
        d = int(d)
        if d not in r:
            error('%d is not in range for IP Address integers' % d)
            return False

    return True

# checks the port number passed is in range
def check_port(port):
    port = int(port)
    r = range(1,65536)
    if port not in r:
        error('%d is not in range for port integers' % port)
        return False

    return True


# Main Function
def is_valid_socket_address(socket_address):
    """Determine if the provided string is a valid socket address.
    This function declaration must be kept unmodified.

    Args:
        socket_address: A string with a socket address, eg, 
            '127.12.23.43:5000', to be checked for validity.
    Returns:
        A boolean indicating whether the provided string is a valid 
        socket address.
    """

    # Parse socket_address 
    try:
        # replace : with . so split function only needs to be used once
        arguments = socket_address.replace(':','.').split('.')

        # check parsed result has the correct number of arguments (x,y,z,w,port) = 5
        if len(arguments) == 5:

            # check IP Address integers and Port integer are in range
            if check_ip_ints(arguments[:4]) and check_port(arguments[4]):
                return True
            else:
                return False

        else:
            error(invalid_address)
            return False
            
    except ValueError as e:
        error(e)
        return False



# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    for socket_address in ["127.12.23.43:5000",
                   "127.A:-12"]:
        print is_valid_socket_address(socket_address)