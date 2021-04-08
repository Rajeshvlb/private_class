import json
handle = open("json_input.json", "r")
content = handle.read()

d = json.loads(content) #json to dictionary

j = json.dumps(d) #dictionary to json

j = json.dumps(d, ident=4)
handle.close()
handle = open("json_output.json", "w")
handle.write(j)
handle.close()
