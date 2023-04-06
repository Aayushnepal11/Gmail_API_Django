import json
import os

def json_operations(filename, *args):
    json_file = None
    with open(os.path.join(os.getcwd(), filename), 'w', encoding='utf-8') as json_out:
        for data in args:
            json_file = json.dumps(json_out.write(str(data)))
    
    # with open(filename, 'r') as json_read:
    #     json.loads(json_read.read(json_file))