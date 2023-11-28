#Task: Write a Python function analyze_logs that takes this list as input and returns a dictionary. 
#The dictionary should map each service to another dictionary that counts how many times each status code has occurred for that service.

#Example:
#Input: [("2023-03-01T12:00", "auth_service", "200 OK"), ("2023-03-01T12:01", "data_service", "500 Internal Server Error"), ("2023-03-01T12:02", "auth_service", "200 OK")]
#Expected Output: {"auth_service": {"200 OK": 2}, "data_service": {"500 Internal Server Error": 1}}

# input is a tuple
# list
input = [("2023-03-01T12:00", "auth_service", "200 OK"), ("2023-03-01T12:01", "data_service", "500 Internal Server Error"), ("2023-03-01T12:02", "auth_service", "200 OK")]

# print(input[1])

def analyze_logs (temp_data):
    temp_dict = {}
    for i in input:
        key = i[1]
        value = i[2]
        if key not in temp_dict:
            temp_dict[key] = {}
        
        if value not in temp_dict[key]:
            temp_dict[key][value] = 1
        else:
            temp_dict[key][value] += 1

    print(temp_dict)

analyze_logs(input)
