import random 

def random_caps(input_string): 
    ret = ""
    for letter in input_string: 

        if len(ret) >= 2: 
            if ret[-2:].isupper(): 
                ret += letter.lower() 
                continue 
            elif ret[-2:].islower(): 
                ret += letter.upper() 
                continue 

        ret += letter.upper() if random.choice([0, 1]) == 1 else letter.lower()

    return ret 

print(random_caps("put your sentence here."))