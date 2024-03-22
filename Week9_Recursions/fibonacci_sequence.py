'''Method 1'''
def recurFibo(n):
    if n <= 1:  # it will return 1 since we know that the first number in the fibonacci sequence is 1
        return n
    else:
        return recurFibo(n - 1) + recurFibo(n - 2) # returns the next number in the sequence by adding the previous number and the number before the previous


def fibSeries(nterms):
    # Check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Sequence:")
        for i in range(1, nterms + 1): # using a for loop to include all the terms
            print(recurFibo(i)) # printing each number in the sequence based on how many times the for loop is run. Calling the function above each time i increases. Therefore printing each number in the fibonacci sequence


fibSeries(30) # Calls the main function


'''Method 2 Using Loops'''
def fibonacciSeries(num):
    # Check if number of terms is valid
    if num <= 0:
        print("Enter a positive integer.")
    elif num == 1: # return 1 if the terms is 1 since 1 is the start of the fibonacci sequence
        return[1]
    elif num == 2: # if terms is 2 then it will return this because 0 + 1 will be 1
        return [1, 1]
    else:
        fibList = [1, 1] # we need to start off with 2 values in the sequence because we could get an error about "index out of bounds" when we try to do i - 1 and if the list does not have an index of 1 then there will be an error. Fibonacci sequence requires the previous number and the number before the previous.
        for i in range(2, num): # starting from 2 to the target since we already have 2 of the values we dont need to run the for loop when num is 2 only 3 and above.
            fibList.append(fibList[i - 1] + fibList[i - 2]) # adding on to the list for fibonacci sequence by using the indices of the list. 1 before i and 2 before i and added together
        return fibList # it will return the completed list to be printed


print(fibonacciSeries(30))