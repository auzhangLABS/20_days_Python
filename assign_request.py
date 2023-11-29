# Scenario: You're simulating a simple load balancer that distributes incoming requests to a pool of servers based on their current load.
# Each server's load is represented as a percentage, and you have a list of these loads.

# Task: Write a Python function assign_request that takes a list of server loads and returns the index of the server to which the next request 
# should be assigned. The server with the lowest load should be chosen.

# Example:

# Input: [30, 60, 20, 80] (each number represents the load on a server)
# Expected Output: 2 (index of the server with the lowest load, which is 20%)
def assign_request(): 
    input = [30,60,20,80]
    load = {}
    key = -1
    for i in input:
        key = key + 1
        value = i
        load[key] = value

    print(min(load, key=load.get))
    print(load[2])
assign_request()
