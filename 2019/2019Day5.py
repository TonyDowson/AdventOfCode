import math

def getValue(all_data,value,mode):
    if mode == '0':
        return all_data[value]
    elif mode == '1':
        return value

def execute(all_data,pointer,input):

    instruction = str(all_data[pointer])
    instruction = '0'*(5 - len(instruction)) + instruction
    #print("Instructions " + instruction)

    opcode = instruction[-2:]        
    #print("Opcode="+opcode)

    if opcode == '01' or opcode == '02':
        v1 = getValue(all_data, all_data[pointer+1],instruction[2])
        v2 = getValue(all_data, all_data[pointer+2],instruction[1])  
        if opcode == '01':
            calc = v1 + v2            
        else:
            calc = v1 * v2
        #print("v1="+str(v1)+" v2="+str(v2)+" Calc "+str(calc)+ " store in "+str(all_data[pointer+3]))
        all_data[all_data[pointer+3]] = calc
        newpointer = pointer + 4
    elif opcode == '03':
        print("INPUT="+str(input) + " written to loc "+ str(all_data[pointer+1]))
        all_data[all_data[pointer+1]] = input
        newpointer = pointer + 2
    elif opcode == '04':
        if instruction[2] == '1':
            print("OUTPUT - "+str(all_data[pointer+1]))
        else:
            print("OUTPUT - "+str(all_data[all_data[pointer+1]]))        
        newpointer = pointer + 2
    elif opcode == '05' or opcode == '06':
        if instruction[2] == '1': 
            v = all_data[pointer+1]
        else:
            v = all_data[all_data[pointer+1]]

        if ((v != 0 and opcode == '05') or (v == 0 and opcode == '06')):
            if instruction[1] == '1':        
                newpointer = all_data[pointer+2]
            else:
                newpointer = all_data[all_data[pointer+2]] 
        else:
            newpointer = pointer + 3             
    elif opcode == '07':
        v1 = getValue(all_data, all_data[pointer+1],instruction[2])
        v2 = getValue(all_data, all_data[pointer+2],instruction[1])  
        if v1 < v2:
            r = 1
        else:
            r = 0        
        all_data[all_data[pointer+3]] = r
        newpointer = pointer + 4
    elif opcode == '08':
        v1 = getValue(all_data, all_data[pointer+1],instruction[2])
        v2 = getValue(all_data, all_data[pointer+2],instruction[1])  
        #print("v1="+str(v1) + " v2="+str(v2))
        if v1 == v2:
            r = 1
        else:
            r = 0        
        all_data[all_data[pointer+3]] = r
        newpointer = pointer + 4        
    elif opcode == '99':
        newpointer = -1

    #print("Instructions executed "+str(instructions[pointer:newpointer]))

    return all_data, newpointer

gd = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,210,88,224,101,-143,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,101,42,92,224,101,-78,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1101,73,10,225,1102,38,21,225,1102,62,32,225,1,218,61,224,1001,224,-132,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,19,36,225,102,79,65,224,101,-4898,224,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1101,66,56,224,1001,224,-122,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1002,58,82,224,101,-820,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,2,206,214,224,1001,224,-648,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,76,56,224,1001,224,-4256,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,37,8,225,1101,82,55,225,1102,76,81,225,1101,10,94,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1107,677,677,224,1002,223,2,223,1006,224,389,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,419,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,524,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,659,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

#part 1 test data
test0 = [1002,4,3,4,33]

#part 2 test data
test1 = [3,9,8,9,10,9,4,9,99,-1,8] # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
test2 = [3,9,7,9,10,9,4,9,99,-1,8] # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
test3 = [3,3,1108,-1,8,3,4,3,99] # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).]
test4 = [3,3,1107,-1,8,3,4,3,99] # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).]
#jump tests
test5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
test6 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

test7 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day5.txt", "r")
#gd = f.readlines()
#game_data = [i.strip('\n') for i in gd]
instructions = gd
pointer = 0
#input = 1 # part 1 input
input = 5 # part 2 input
print("Starting with..." + str(instructions))

while pointer != -1:
    instructions,pointer = execute(instructions,pointer,input)

#print("Instructions - " + str(instructions))
