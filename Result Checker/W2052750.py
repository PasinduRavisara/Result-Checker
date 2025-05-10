#Import graphics module
from graphics import *


#creating and initializing variables
student=0
passcredit=0
defercredit=0
failcredit=0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
outcomes=0

#Creating some lists
progress_values=[]
exclude_values=[]
trailer_values=[]
retriever_values=[]

#A tuple with all possible credit values
range_tuple=(0,20,40,60,80,100,120)

#user defined functions
def continue_or_quit():
    con_or_quit=input('''
                Would you like to enter another set of data?
                Enter 'y' for yes or 'q' to quit and view results:''')
    return con_or_quit


#Main program


#Ask if the user is a student or staff member
user=input('''
Are you a student or a staff member

Enter 'student' if you are a student                                      
Enter 'staff' if you are a staff member:''')
print("\n")

while True:
    if student==1:
        continue
    while True:
        try:
            passcredit=int(input("Please enter credits at pass:"))#Ask the user to input credits

            if not passcredit in range_tuple: #Check if the credit is in the range
                print("Out of range\n")
                continue
            else:
                break
        except ValueError: #Exception to avoid value error
            print("Integer required\n")
            continue

    while True:
        try:
            defercredit=int(input("Please enter credits at defer:"))#Ask the user to input credits

            if not defercredit in range_tuple: #Check if the credit is in the range
                print("Out of range\n")
                continue
            else:
                break
        except ValueError: #Exception to avoid value error
            print("Integer required\n")
            continue

    while True:
        try:
            failcredit=int(input("Please enter credits at fail:"))#Ask the user to input credits

            if not failcredit in range_tuple: #Check if the credit is in the range
                print("Out of range\n")
                continue
            else:
                break
        except ValueError: #Exception to avoid value error
            print("Integer required\n")
            continue


    if not passcredit+defercredit+failcredit == 120: #Check total credit
        print("Total incorrect\n")
        continue


    #Create a list with Pass, Defer and Fail credits
    all_credit=[passcredit,defercredit,failcredit]

        
    #Find out if the student is progressing, trailing, module retriever or excluded
    if all_credit==[120,0,0]:
        progress_count +=1
        outcomes+=1
        progress_values.append(all_credit)
        print("\nResult = Progress\n")#The student is prgrassing

    elif all_credit==[100,20,0] or all_credit==[100,0,20]:
        trailer_count+=1
        outcomes+=1
        trailer_values.append(all_credit)
        print("\nResult = Progress (module trailer)\n")#The student is trailing

    elif all_credit==[80,40,0] or all_credit==[80,20,20] or all_credit==[80,0,40] or all_credit==[60,60,0] or all_credit==[60,40,20] or all_credit==[60,20,40] or all_credit==[60,0,60] or all_credit==[40,80,0] or all_credit==[40,60,20] or all_credit==[40,40,40] or all_credit==[40,20,60] or all_credit==[20,100,0] or all_credit==[20,80,20] or all_credit==[20,60,40] or all_credit==[20,40,60] or all_credit==[0,120,0] or all_credit==[0,100,20] or all_credit==[0,80,40] or all_credit==[0,60,60]:
        retriever_count +=1
        outcomes+=1
        retriever_values.append(all_credit)
        print("\nResult = Do not progress – module retriever\n")#The student has to retrieve the module

    elif all_credit==[40,0,80] or all_credit==[20,20,80] or all_credit==[20,0,100] or all_credit==[0,40,80] or all_credit==[0,20,100] or all_credit==[0,0,120]:
        exclude_count +=1
        outcomes+=1
        exclude_values.append(all_credit)
        print("\nResult = Exclude\n")#The student is excluded
        
        
    #If the user is a student the programme should stop 
    if user=="student" or user=="Student" or user=="'student'":
        print("Thank you.\n")
        student=1
        continue 



    #Ask the user to continue or quit

    myfunction=continue_or_quit()#Using a function

    if myfunction=="y" or myfunction=="Y" or myfunction=="q" or myfunction=="Q": #Check is the user input is y or Y or q or Q
        if myfunction=="y" or myfunction=="Y": #Enter y or Y to continue
            print()
            continue

        elif myfunction=="q" or myfunction=="Q": #Enter q or Q to quit
            break




#Creating the histogram

# List to store the category names and corresponding frequencies
categories = ['Progress', 'Trailing', 'Retriever', 'Exclude']
frequencies = [progress_count, trailer_count, retriever_count, exclude_count]

        
while True:
    # Create the histogram
    histogram = GraphWin("Student Progression Histogram", 800, 600)
    histogram.setBackground("White")

    #Draw the title
    title= Text(Point(400,20),"Student  Progression  Histogram")
    title.draw(histogram)
    
    # Scale factor for the histogram bars
    

    # Draw the histogram bars
    for i, freq in enumerate(frequencies):
        x1 = i * 100 * 2
        y1 = 500 - freq * 20
        x2 = (i + 1) * 100 * 2
        y2 = 500

        rect = Rectangle(Point(x1, y1), Point(x2, y2))
        rect.setFill(['green', 'yellow', 'orange', 'red'][i])#different colors for each bar
        rect.draw(histogram)

        # Display category names below the bars
        text = categories[i] + f' ({freq})'
        text_point = Point((x1 + x2) / 2, y2 + 10)
        label = Text(text_point, text)
        label.draw(histogram)

        # Draw the total number of outcomes
        total_outcomes = Text(Point(400, 550), f"{outcomes} outcomes in total!")
        total_outcomes.draw(histogram)

    # Wait for a click and then close the window
    try:
        histogram.getMouse()
        histogram.close()
        break
    except:
        print("\nPlease click on the histogram.")
        continue
        

#Part 2

#After closing the histogram, show the user input values
print("\n\nPart 2:\n")
for i in progress_values:
    print("Progress -", i[0],",",i[1],",",i[2])
for i in trailer_values:
    print("Progress (module trailer) -", i[0],",",i[1],",",i[2])
for i in retriever_values:
    print("Module retriever -", i[0],",",i[1],",",i[2])
for i in exclude_values:
    print("Exclude -", i[0],",",i[1],",",i[2])


#Part 3

#Print the user input values in a text file
file=open("Part 3.txt","w")
file.write("Part 3:\n")
for i in progress_values:
    file.write(f"\nProgress - {i[0]},{i[1]},{i[2]}")
for i in trailer_values:
    file.write(f"\nProgress (module trailer) - {i[0]},{i[1]},{i[2]}")
for i in retriever_values:
    file.write(f"\nModule retriever - {i[0]},{i[1]},{i[2]}")
for i in exclude_values:
    file.write(f"\nExclude - {i[0]},{i[1]},{i[2]}")
file.close()


end=input("\n\nPress Enter to finish the program")
print("Thank you.")

    
    
    
    
                  
