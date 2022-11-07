import pandas as pd
import sys
import csv

#Test case were created with http://www.faculty.ucr.edu/~mmaduro/random.htm
#Reference video https://www.youtube.com/watch?v=LkwgI2mHbik&feature=youtu.be
class needlemanWunschAlgorithm:
    def __init__(self, sequence1, sequence2):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.matrix = self.needlemanWunsch(self.sequence1, self.sequence2) #Generate scoring matrix
    def needlemanWunsch(self, sequence1, sequence2): #Generate Lookup Table 
        #Returns the matrix
        #Parameters:
        #   sequence1 (str):The string represent the sequence 1
        #   sequence2 (str):The string represent the sequence 2

        g_factor = -2
        matrix = [["", ""],["", 0]]
        index = 0
        g = g_factor

        ### Matrix setup
        while (index < len (sequence1)):
            matrix[0].append(sequence1[index])
            matrix[1].append(g) # gap penalty
            g-=2
            index+=1

        index = 0
        g= g_factor
        while (index < len (sequence2)):
            matrix.append([sequence2[index], g])
            g-=2 # gap penalty 
            index+=1
    
        ## Generate full matrix
      
        for ai in range(2,len(matrix)):
            for bj in range(2,len(matrix[0])):
                f = [matrix[ai-1][bj-1] + self.scoring(matrix[ai][0], matrix[0][bj]),  matrix[ai][bj-1] + g_factor, matrix[ai-1][bj] + g_factor] 
                matrix[ai].append(max(f))
                
        #print()
        #self.printMatrix(matrix)
        return matrix

    def printMatrix(self, matrix): #Pretty print the Matrix in the terminal
        for i in range(len(matrix)):
            for j in matrix[i]:
                print(f"{j:>4}", " ", end="")
            print("\n")

    def scoring(self, n1, n2):
        #Returns the scoring Matrix
        #Parameters:
        #   n1 (str):The string represent neucloutide 1
        #   n2 (str):The string represent neucloutide 2
        if n1 != n2:
            return -1
        else:
            return 1

    def backtracking(self):     #return score, and sequence alaigment in a string with format dna_string1 dna_string2 scoring 
        #print(self.sequence1, self.sequence2)
        dna_h = "" #seq 1
        dna_v = "" #seq 2
        matrix_c = self.matrix
        ai = len(matrix_c)-1
        bi = len(matrix_c[ai])-1
       
        score = matrix_c[ai][bi]

        while(ai != 1 or bi != 1):

            if ai ==  1:
                dna_h = matrix_c[0][bi] + dna_h
                dna_v = "-" + dna_v
                bi-=1
            elif bi == 1:
                dna_h = "-" + dna_h
                dna_v = matrix_c[ai][0] + dna_v
                ai-=1
            
            #calculate larger
            else:

                dif = 1 if matrix_c[ai][0] == matrix_c[0][bi] else -1
                upper =  matrix_c[ai-1][bi] -2
                left =  matrix_c[ai][bi-1] - 2 #gap - 2
                diag =  matrix_c[ai-1][bi-1] + dif

                #print(upper, left, diag)
                if upper >= diag and upper >= left:
                    dna_v = matrix_c[ai][0] + dna_v
                    dna_h = "-" + dna_h
                    ai-=1
                elif left >= upper and left >= diag:
                    dna_v = "-" + dna_v
                    dna_h = matrix_c[0][bi] + dna_h
                    bi -= 1
                else: 
                    dna_v = matrix_c[ai][0] + dna_v
                    dna_h = matrix_c[0][bi] + dna_h
                    ai-=1 
                    bi-=1
                   

        """
        From end to begin implementaiton backtraking (not working, it finds the aligment but it may not be the specific aligment require)
        I found out that there can be more than 1 correct aligment but for this specific assigment we need to use the max formula** in this video https://www.youtube.com/watch?v=LkwgI2mHbik&feature=youtu.be minute 14:15
        ai = len(matrix_c)-1
        bi = len(matrix_c[ai])-1
       
        score = matrix_c[ai][bi]
        while( (ai != 1 or bi != 1) ):
            
            print(matrix_c[ai][bi], matrix_c[ai][0], matrix_c[0][bi], ai ,bi)
            if ai == 1: 
            
                dna_horizontal = "-" + dna_horizontal
                dna_vertical = matrix_c[0][bi] + dna_vertical
                bi -= 1

            elif bi == 1:
                dna_horizontal = matrix_c[0][bi] + dna_horizontal
                dna_vertical = "-" + dna_vertical
                ai -= 1

            elif matrix_c[ai-1][bi-1] >= matrix_c[ai][bi-1] and matrix_c[ai-1][bi-1] >= matrix_c[ai-1][bi] or matrix_c[0][bi] == matrix_c[ai][0]:
              
            
                dna_horizontal = matrix_c[ai][0] + dna_horizontal
                dna_vertical = matrix_c[0][bi] + dna_vertical

                ai -= 1
                bi -= 1
                
            elif matrix_c[ai-1][bi] > matrix_c[ai-1][bi-1] and matrix_c[ai-1][bi] > matrix_c[ai][bi-1]:
              
                dna_horizontal = matrix_c[ai][0] + dna_horizontal
                dna_vertical = "-" + dna_vertical
                ai -= 1
            else:
         
                dna_horizontal = "-" + dna_horizontal
                dna_vertical = matrix_c[0][bi] + dna_vertical
                bi -= 1
            
        """
        return f"{dna_h} {dna_v} {score}"



if __name__ == "__main__":
   
    if len(sys.argv) > 1:
        cvsFile = pd.read_csv("input.csv")

    if len(sys.argv) > 1:
        csv_file = open("input.csv",newline="")
        reader = csv.reader(csv_file)  # the first line is the header

        header = next(reader)  # skip the header (first line)
        for row in reader:
            print(needlemanWunschAlgorithm(row[0],row[1]).backtracking())

