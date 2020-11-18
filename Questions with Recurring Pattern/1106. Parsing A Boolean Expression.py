#BEFORE HINT

#Question Pattern : Given an expression that includes brackets as a string, find the final value of the expression
#Use stacks to store the values inside brackets, 

#Solution : 
#Iterate in reversed order, have a current value, keep a stack
def evaluate(bool_expression): 
    stack = []
    for char in bool_expression: 
        if char == ')': 
            while stack[-1] != '(': 
                
                stack.pop()
            #Calculate stack value
        
        elif char != ',': 
            stack.append(True if c == 't' else False)

#The information to evaluate the stack is before that stack so you go from start to end.
#If this was the atom question, you would go from end to start. 
#While going linearly you can find out how is the stack evaluated. 
#Common pattern. 