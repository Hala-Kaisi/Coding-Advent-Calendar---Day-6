line = open("D6_Input.txt").readlines()

buffer = str(line[0])

counter = 14

fourteenLetters = []

letters = [*buffer]

fourteenLetters.append(buffer[0]) 
fourteenLetters.append(buffer[1])
fourteenLetters.append(buffer[2])
fourteenLetters.append(buffer[3]) 
fourteenLetters.append(buffer[4]) 
fourteenLetters.append(buffer[5]) 
fourteenLetters.append(buffer[6]) 
fourteenLetters.append(buffer[7]) 
fourteenLetters.append(buffer[8]) 
fourteenLetters.append(buffer[9]) 
fourteenLetters.append(buffer[10]) 
fourteenLetters.append(buffer[11]) 
fourteenLetters.append(buffer[12]) 
fourteenLetters.append(buffer[13]) 

firstDuplicates = [letter for letter in fourteenLetters if fourteenLetters.count(letter) > 1]
if len(firstDuplicates) > 0:
    for i in range(14, len(buffer)):
        fourteenLetters.pop(0)
        fourteenLetters.append(buffer[i])
        duplicates = [letter for letter in fourteenLetters if fourteenLetters.count(letter) > 1]
        if len(duplicates) > 0:
            counter += 1
        else:
            break
    
for i in range(0, len(letters)):
    if letters[i] == fourteenLetters[0] and letters[i+1] == fourteenLetters[1] and letters[i+2] == fourteenLetters[2] and letters[i+3] == fourteenLetters[3] and letters[i+4] == fourteenLetters[4] and letters[i+5] == fourteenLetters[5] and letters[i+6] == fourteenLetters[6] and letters[i+7] == fourteenLetters[7] and letters[i+8] == fourteenLetters[8] and letters[i+9] == fourteenLetters[9] and letters[i+10] == fourteenLetters[10] and letters[i+11] == fourteenLetters[11] and letters[i+12] == fourteenLetters[12] and letters[i+13] == fourteenLetters[13]:
        print(i)
        break

print(fourteenLetters)
print(counter)
    
    
