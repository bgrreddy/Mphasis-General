import json

def pop_element(element):
    # data = open('/Users/test/Downloads/Updated_Python_exercises_QA_Engr/test_payload.json')
    # json_data = json.load(data)
    # print(json_data)
    # data.close()
    
    
    with open('/Users/test/Downloads/Updated_Python_exercises_QA_Engr/test_payload.json') as json_file:
        data = json.load(json_file)
        print(data[element])
        print(len(data))



        for i in range(len(data)):
            print(data[i])
            if data[i] == element:
                data.pop(i)
            
    with open('/Users/test/Downloads/Updated_Python_exercises_QA_Engr/test_payload.json', mode='w') as write_file:
        json.dumps(data,write_file)


pop_element('outParams')
