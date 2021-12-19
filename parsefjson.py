import ast
import json
        
with open('C:/Users/Papa Ba GAYE/Desktop/flights.json', mode="r") as f:
    lines = f.readlines()

# lines = lines[:4]

# for line in lines:
#     line = json.dumps(ast.literal_eval(line))
#     print(line)

bulks = []
jsons = []
for idx in range(len(lines)):
    bulk = '{"index":{"_index": "flights","_type":"flight",\"_id\":'+str(idx+1)+'}}'
    bulks.append(bulk)

for line in lines:
    # line = json.dumps(ast.literal_eval(line))
    print(line)
    jsons.append(line)
    

for i, j in zip(bulks, jsons):
    f = open('C:/Users/Papa Ba GAYE/Desktop/flights_finish.json', "a")
    f.write(f'{i}\n{j}')
f.close()



