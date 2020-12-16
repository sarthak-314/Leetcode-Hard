//SARTHAK BHATT - 20198059

#include <stdio.h>
//Assumption : The string length does not exceed MAX_STR_LEN
//Alternative Approach : Ask the user for the length of the string. 
#define MAX_STR_LEN 500 

char mainString[MAX_STR_LEN]; 
char patternString[MAX_STR_LEN]; 
char replacementString[MAX_STR_LEN]; 
char outputString[MAX_STR_LEN]; 

int patternFound = 0; 
    
int c = 0, m = 0, i = 0, j = 0, k; 

//patternMatchingOperation : Replaces all the occurances of pattern in main string with the replacement string
void patternMatchingOperation() {

    while(mainString[c] != '\0'){
        //Chars match
        if(mainString[m] == patternString[i]){
            i++; 
            m++; 

            if(patternString[k] == '\0'){
                patternFound = 1;
                for(int k = 0; replacementString[k] != '\0'; k++, j++){
                    outputString[j] = replacementString[k]; 
                }
                i = 0; 
                c = m; 
            }
            
        }
        else {

            outputString[j] = mainString[c]; 
            j++; 
            c++; 
            m = c; 
            i = 0; 
        }
    }
    outputString[j] = '\0'; 

}

int main() {

    //Read the main string
    printf("Enter the main string : ");
    //Reads the main string from the standard input upto MAX_STR_LEN 
    fgets(mainString, MAX_STR_LEN, stdin);   
     
    //Read the pattern string
    printf("\nEnter the pattern string : "); 
    fgets(patternString, MAX_STR_LEN, stdin); 

    //Read the replacement string
    printf("\nEnter the replacement string : "); 
    fgets(replacementString, MAX_STR_LEN, stdin); 

    patternMatchingOperation();
    if(patternFound == 1)
        printf("\nResult String :  %s", outputString);
    else
        printf("\nPattern not found in main string"); 

    return 0; 
}


//Complexity Analysis
//length of main string = N | length of pattern string = K
//Time Complexity - O(N * K)















//Scanf stops taking input after encountering a space 
//fgets function takes input only upto the maxlimit
//