""" Module for loading and outputting data """


def load_data(filename):


    """
        Data returned: data_config, video_config, endpoints, requests

        each endpoint is dictionary with the cache_id being the key and the latency being the value, 
        the latency datacentre is stored in a key "datacentre"

        each request is a list of tuples: (video_id, endpoint_id, number of requests for the video)
    """


    # config line loaded
    raw_data = open(filename).readlines()
    # split all the lines
    for i in range(len(raw_data) ):
        line = raw_data[i]
        raw_data[i] = line.split()
        for j in range(len(raw_data[i])):
            v = raw_data[i][j]
            raw_data[i][j] = int(v)
    
    line0 = raw_data[0]
    data_config = {
        "videos": line0[0],
        "endpoints": line0[1],
        "requests": line0[2],
        "caches":  line0[3],
        "cache_size": line0[4]
    }

    #video info loaded
    video_config = raw_data[1]

    # delete first two lines
    raw_data[0:1] = []

    endpoints = list()
    endpoint = dict()
    cache_connections = 0
    datacentre_latency = 0
    index = 0
    endpoint_count = 0
    #load endpoint data
    while endpoint_count < data_config["endpoints"]:
        #end point config line 
        line0 = raw_data[index]
        endpoint["datacentre"] = line0[0]
        cache_connections = line0[1]

        #for each cache config
        for j in range(index, index + cache_connections + 1):
            line = raw_data[j] # line = {cache_id} {latency}
            endpoint[line[0]] = line[1]
        
        endpoints.append(endpoint)
        index += cache_connections
        endpoint_count +=1
    

    # load requests data
    requests = list()
    for i in range(index, len(raw_data)):
        line = raw_data[i]
        requests.append( (line[0], line[1], line[2]) )

    return data_config, video_config, endpoints, requests


def output_data(caches):
    