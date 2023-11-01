list1=[] # creating an empty list
list2=[1,2.4,'abc',(1,2),[6,78,9]] # creating a list of different values
print("The type of",list1,"is:",type(list1))
print("The type of",list2,"is:",type(list2))

list_1=[1,3,5.6,'a',"PythonGeeks",0.4]
print(list_1[3]) # accessing the 4th element
print(list_1) # accessing the whole list
print(list_1[-2]) # printing the last 2nd element

list_1=[1,3,5.6,'a',"PythonGeeks",0.4]
print("list_1[2:5] =",list_1[2:5]) # slicing 3rd to 5th element
print("list_1[:] =",list_1[:]) # getting entire list
print("list_1[-5:-2] =",list_1[-5:-2]) # slicing last 5th to 3rd element
print("list_1[3:] =",list_1[3:]) # slicing all elements after 3rd one
print("list_1[-3:] =",list_1[-3:]) # slicing all elements after last 3rd one
print("list_1[:2] =",list_1[:2]) # slicing all elements till 2nd one
print("list_1[:-2] =",list_1[:-2])# slicing all elements till last 2nd one

# Create a list
my_list = [1, 2, 3, 4, 5]

# Modify an element using indexing
my_list[2] = 10
print("After modifying using indexing:", my_list)  # Output: [1, 2, 10, 4, 5]

# Modify a range of elements using slicing
my_list[1:4] = [20, 30, 40]
print("After modifying using slicing:", my_list)  # Output: [1, 20, 30, 40, 5]

# Delete an element using indexing
del my_list[2]
print("After deleting using indexing:", my_list)  # Output: [1, 20, 40, 5]

# Delete a range of elements using slicing
my_list[1:4] = []
print("After deleting using slicing:", my_list)  # Output: [1, 5]

# Delete the entire list
del my_list
# Now, my_list is no longer defined

# Create a sample list
my_list = [1, 2, 3, 4, 5]

# Method 1: Loop through the list and print each element
for item in my_list:
    print(item)

# Method 2: Loop through the list with index using enumerate()
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

# Method 3: Loop through the list in reverse order
for item in reversed(my_list):
    print(item)

# Sample 1:
list1=[1,-2,3,-4,5]
list2=[x**2 for x in list1]
print(list2)

# Sample 2 (with condition):
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

emp_info=['Python',5,'Developer']

#List unpacking
skill,exp,role=emp_info
print (skill)	#Output:Python
print (exp)	#Output:5
print (role)	#Output:Developer

# Initialize an empty stack to represent the browser history
browser_history = []

# Simulate user browsing by pushing visited pages onto the stack
browser_history.append("Homepage")
browser_history.append("About Us")
browser_history.append("Products")
browser_history.append("Contact Us")

# User clicks the back button
if len(browser_history) > 0:
    current_page = browser_history.pop()
    print("User clicked the back button. Navigating to:", current_page)

# User continues browsing and adds more pages to the history
browser_history.append("FAQs")
browser_history.append("Blog")

# User clicks the back button again
if len(browser_history) > 0:
    current_page = browser_history.pop()
    print("User clicked the back button. Navigating to:", current_page)

# At this point, the browser history would contain ["Homepage", "About Us", "Products", "Contact Us", "FAQs"].

queue = ['Person 1','Person 2'] 
  
# Adding elements to the queue 
queue.append('Person 3') 
  
print("\nQueue before:") 
print(queue) 
  
# Removing elements from the queue 
print("\nElements dequeued from queue : ", queue.pop(0)) 
  
print("\nQueue after:") 
print(queue)

tup=(9,6,'g','Python',7.4)
print(len(tup))
print(tup.index('g'))

print(tup.count('a'))

# Create a tuple using round brackets
t1 = (1, 2, 3, 4)

# Create a tuple from a list the tuple() constructor
t2 = tuple([1, 2, 3, 4, 5])

# Create a tuple using the tuple() constructor
t3 = tuple([1, 2, 3, 4, 5, 6])

# Print out tuples
print(f"Tuple t1: {t1}")
print(f"Tuple t2: {t2}")
print(f"Tuple t3: {t3}")

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is NOT VALID for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);

tup = ('physics', 'chemistry', 1997, 2000);
print (tup);
del tup;
print ("After deleting tup : ");
print (tup);	# an exception raised, because after del tup tuple does not exist anymore

tup=(1,2,3,4,5)

list1=list(tup)
list1[4]=6

tup=tuple(list1)
tup

tup=1,2,3 #packing
print("The type of ",tup,"is:",type(tup))

a,b,c=tup #unpacking
print(a)
print(b)


