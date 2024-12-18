  
def isSubsequence(V,B):
    vindex = 0
    bindex = 0
    
    while vindex < len(V) and bindex < len(B):
        if V[vindex] == B[bindex]:
            bindex += 1
        vindex += 1

    if bindex == len(B):
        return True
    return False

counter = 0

with open("inputs.txt", "r") as input_file:

    T = int(input_file.readline().strip())

    for i in range (T):

        V = input_file.readline().strip()
        
        N = int(input_file.readline().strip())
        
        for _ in range(N):
            B = input_file.readline().strip() 
            result = isSubsequence(V, B)
            
            if result:
                print("POSITIVE")
                counter +=1
            else:
                print("NEGATIVE")
        
    print("Infected Individuals :",counter)