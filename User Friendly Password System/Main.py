def encode(password):
    length = len(password) - 1
    P = 131
    M = 10**9 + 7
    hashedValue = 0
    for character in password:
        hashedValue += ord(character) * (P ** length)
        length -= 1
    
    
    unhashedPassword = password
    hashedPassword = (hashedValue % M)
    
    return unhashedPassword, hashedPassword

def decode(value, unhashedPassword, hashedPassword):

    asciilist = []
    for i in range(48,58):
        asciilist.append(chr(i))
        
    for i in range (65,91):
        asciilist.append(chr(i))

    for i in range (97, 123):
        asciilist.append(chr(i))


    if value == str(hashedPassword):
        return 1
    else:
        for i in range(len(asciilist)):
            temp = unhashedPassword
            temp += asciilist[i]
            garbage, authCompareValue = encode(temp)
            if str(authCompareValue) == value:
                return 1
        return 0
                
def authEvents(events):
    # Write your code here
    output = []
    for event in events:
        if event[0] == 'setPassword':
            passwordStr = event[1]
            a,b = encode(passwordStr)  
        else:
            authvalue = event[1]
            result = decode(authvalue, a, b)
            output.append(result)
    return output
    
    
if __name__ == '__main__':
    
    events = [['setPassword', '000A'], ['authorize', '108738450'], ['authorize', '108738449'], ['authorize', '244736787']]
    a = authEvents(events)
    print(a)

    