# Scenario: You are monitoring the response times of various API endpoints. 
# The data is provided as a list of JSON-like dictionaries, each representing an API call with endpoint, 
# timestamp, and response_time_ms (response time in milliseconds).

# Task: Write a Python function analyze_api_response_times that takes this list and calculates the average response time for each API endpoint.

input = [
    {"endpoint": "/login", "timestamp": "2023-03-01T12:00", "response_time_ms": 150},
    {"endpoint": "/data", "timestamp": "2023-03-01T12:01", "response_time_ms": 200},
    {"endpoint": "/login", "timestamp": "2023-03-01T12:02", "response_time_ms": 130},
    {"endpoint": "/update", "timestamp": "2023-03-01T12:03", "response_time_ms": 180},
    {"endpoint": "/data", "timestamp": "2023-03-01T12:04", "response_time_ms": 220},
    {"endpoint": "/login", "timestamp": "2023-03-01T12:05", "response_time_ms": 160},
    {"endpoint": "/update", "timestamp": "2023-03-01T12:06", "response_time_ms": 170}
]

#desired output: 
# {
#     "/login": 146.67,  # Average of 150, 130, and 160
#     "/data": 210.0,    # Average of 200 and 220
#     "/update": 175.0   # Average of 180 and 170
# }

def analyze_api_response_times():
    desired_output = {}
    count = {} 
    for time in input:
        key = time['endpoint']
        value = time['response_time_ms']  
        if key not in desired_output:        
            desired_output[key] = value
            count[key] = 1  
        elif key in desired_output:
            prev = desired_output[key]
            desired_output[key] = value + prev
            prevcount = count[key]
            count[key] = 1 + prevcount

    average = 0    
    for item in desired_output:
        average = desired_output[item]/count[item]        
        desired_output[item] = round(average,2)

    print(desired_output)

analyze_api_response_times()
