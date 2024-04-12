import os
# # get current working directory
# print(os.getcwd())
# # change to a different directory
# os.chdir("C:\\Users\\aua16\\OneDrive - University of Pittsburgh\\Spring 24\\Fundamentals_of_Programming")
# print(os.getcwd())

# LIst all the files at the current location
print(os.listdir())

# mkdir --> Used to make a single directory
# mkdirs --> Used to create a hierarchy of directories
# os.mkdir("Test_Dir")
# os.makedirs("Test_Dir1\\sub1\\sub2")
# os.rmdir("Test_Dir")
os.removedirs("Test_Dir1\\sub1\\sub2")