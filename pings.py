#Task: Write a Python function calculate_average_response_time that calculates the average response time for each service over the last hour. 
#You receive a list of these ping dictionaries and the current timestamp.

# Example:

# Input: List of ping dictionaries and current timestamp.
# Expected Output: Dictionary mapping each service to its average response time over the last hour.

pings = [
    {"service_name": "web_service", "timestamp": "2023-11-27T10:00:00", "response_time": 120},
    {"service_name": "database",    "timestamp": "2023-11-27T10:05:00", "response_time": 300},
    {"service_name": "auth_service", "timestamp": "2023-11-27T10:10:00", "response_time": 200},
    {"service_name": "web_service", "timestamp": "2023-11-27T10:15:00", "response_time": 110},
    {"service_name": "database",    "timestamp": "2023-11-27T10:20:00", "response_time": 290},
    {"service_name": "auth_service", "timestamp": "2023-11-27T10:25:00", "response_time": 210},
    {"service_name": "web_service", "timestamp": "2023-11-27T10:30:00", "response_time": 115},
    {"service_name": "database",    "timestamp": "2023-11-27T10:35:00", "response_time": 310},
    {"service_name": "auth_service", "timestamp": "2023-11-27T10:40:00", "response_time": 190},
    {"service_name": "web_service", "timestamp": "2023-11-27T10:45:00", "response_time": 105},
    {"service_name": "database",    "timestamp": "2023-11-27T10:50:00", "response_time": 305},
    {"service_name": "auth_service", "timestamp": "2023-11-27T10:55:00", "response_time": 205}
]

def calculate_average_response_time(info):
    temp_dict = {}
    count_dict = {}
    for i in pings:
        key = i["service_name"]
        value = i["response_time"]
        if key not in temp_dict:
            temp_dict[key] = value
            count_dict[key] = 1
        elif key in temp_dict:
            c1 = temp_dict.get(key) 
            total = c1 + value
            temp_dict[key] = total 
            count_dict[key] += 1
    for items in temp_dict:
        average = temp_dict[items]/ count_dict[items]
        temp_dict[items] = average
    print(temp_dict)

calculate_average_response_time(pings)
