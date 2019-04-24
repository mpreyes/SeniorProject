




def main():
    i, j = 0, 0
    h, w = 9, 9
    M = [[0 for x in range(w)] for y in range(h)] 
    
    # M[i-1][j-1] = i-1 * j-1
    while( i < 10): #rows
       #M[0..i-1][j] #M contains row of multiples of i, 0 -> n
        while( j < 10): #cols
            M[i][j] = i * j #  M[i-1][j-1]  contains multiples of i-1 * j-1 
            j += 1
        i += 1
    #M[i= 0->n][j= 0 -> n] contains multiples of i *j 

main()