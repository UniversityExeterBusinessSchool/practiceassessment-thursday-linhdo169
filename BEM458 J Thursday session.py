#######################################################################################################################################################
# 
# Name: Do Thi Yen Linh
# SID: 740098305
# Exam Date: March 27th 2025
# Module: Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-linhdo169
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
# Initialize an empty list to store (start, end) positions
my_list = []

# Use my Student ID (740098305)
my_student_id = 740098305

# Extract the first and last digits of the student ID
first_digit = int(str(my_student_id)[7])  # First digit of SID
last_digit = int(str(my_student_id)[5])  # Last digit of SID

# Retrieve the words corresponding to the first and last digits
allocated_keys = [first_digit, last_digit]

# Loop through the allocated keys
for key in allocated_keys:
    word = key_comments[key]  # Get the word from the dictionary
    start_pos = customer_feedback.find(word)  # Find the start position of the word
    if start_pos != -1:  # If the word is found
        end_pos = start_pos + len(word)  # Calculate the end position
        my_list.append((start_pos, end_pos))  # Append the tuple to the list

# Print the result
print("Allocated keys:", allocated_keys)
print("Positions of words:", my_list)

#OUTPUT
#Allocated keys: [0, 8]
#Positions of words: [(38, 50), (51, 58)]


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 05

# Write your code for Operating Profit Margin
def operating_profit_margin(revenue, cost):
    profit = revenue - cost
    profit_margin = (profit / revenue) * 100
    return profit_margin

# Write your code for Revenue per Customer
def revenue_per_customer(revenue, customers):
    revenue_per_customer = revenue / customers
    return revenue_per_customer

# Write your code for Customer Churn Rate
def customer_churn_rate(customers_beginning, customers_end):
    churn_rate = ((customers_beginning - customers_end) / customers_beginning) * 100
    return churn_rate

# Write your code for Average Order Value
def average_order_value(revenue, orders):
    avg_order_value = revenue / orders
    return avg_order_value

# Call your designed functions here
print("Operating Profit Margin:", operating_profit_margin(74, 5))
print("Revenue per Customer:", revenue_per_customer(74, 5))
print("Customer Churn Rate:", customer_churn_rate(74, 5))
print("Average Order Value:", average_order_value(74, 5))

#OUTPUT
#Operating Profit Margin: 93.24324324324324
#Revenue per Customer: 14.8
#Customer Churn Rate: 93.24324324324324
#Average Order Value: 14.8

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
#Import the Libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Prepare the data
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1) # Reshape to 2D array
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

#Create and train the model
model = LinearRegression()
model.fit(price, demand)

#Predict the demand at price £52
price_52 = np.array([[52]]) # Reshape to 2D array
demand_52 = model.predict(price_52) # Predict the demand at price £52
print("Demand at price £52:", demand_52[0]) # Display the result

#Calculate the price for maximum revenue
max_demand = demand.max() # Maximum demand
max_demand_index = np.where(demand == max_demand)[0][0] # Index of maximum demand
price_max_revenue = price[max_demand_index] # Price for maximum revenue
print("Price for maximum revenue:", price_max_revenue[0]) # Display the result

#Plot the regression line
plt.scatter(price, demand, color='blue') # Scatter plot of the data points
plt.plot(price, model.predict(price), color='red') # Regression line
plt.title('Price vs Demand') # Title of the plot
plt.xlabel('Price (£)') # X-axis label
plt.ylabel('Demand (Units)') # Y-axis label
plt.show() # Display the plot

#OUTPUT
#Demand at price £52: 158.17272727272726
#Price for maximum revenue: 20
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# After revision of the code, the following errors were found and corrected.
# Generate 100 random numbers between 1 and student id number
max_value = int(input("740098305"))
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Plotting the numbers in a line chart
plt.plot(
    random_numbers,
    marker='o',                  
    markerfacecolor='green',       
    markeredgecolor='red',         
    linestyle='--',              
    label='Random Numbers',        
    color='blue'   
)              
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()


# Debug the code and provide comments on the errors found.
# Error 1: The variable name 'max-value' contains a syntax error. It should be 'max_value'.
# Error 2: The function 'integer' is not defined. It should be 'int'.
# Error 3: The 'markercolor' parameter in the 'plot' function should be 'markerfacecolor'.
# Error 4: The 'lable' parameter in the 'plot' function should be 'label'.
# Error 5: The 'title' function is missing quotation marks around the title string.
# Error 6: The 'xlabel' function should be called with parentheses and an equal sign.
# Error 7: The 'ylabel' function should be called with parentheses and an equal sign.
# Error 8: The 'legend' function should be called with parentheses.


