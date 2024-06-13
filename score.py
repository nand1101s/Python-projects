# function to process positive scores only
def scoreresult(score):
    if score < 50:
        print( "fail") 
# score is greater than 50
    else:
        print( "pass")

# main program
score = (int) (input("Enter the score of your food item: "))
while(score != 0):
    scoreresult(score)
    if score <0:
        print("invalid score")
        break




