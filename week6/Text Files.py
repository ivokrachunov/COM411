'''
def main():
    f = open("guru99.txt", "w+")
    # f=open("guru99.txt","a+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.close()
    # Open the file back and read the contents
    # f=open("guru99.txt", "r")
    #   if f.mode == 'r':
    #     contents =f.read()
    #     print contents
    # or, readlines reads the individual line into a list
    # fl =f.readlines()
    # for x in fl:
    # print x
'''
'''
if __name__ == "__main__":
    main()
'''
'''
    def main():
        f = open("guru99.txt", "w+")
        # f=open("guru99.txt","a+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))
        f.close()
        # Open the file back and read the contents
        # f=open("guru99.txt", "r")
        # if f.mode == 'r':
        #   contents =f.read()
        #    print (contents)
        # or, readlines reads the individual line into a list
        # fl =f.readlines()
        # for x in fl:
        # print(x)


    if __name__ == "__main__":
        main()
         '''
'''
#This program shows how to write data in a text file.

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

# i assigned ["This is Lagos \n","This is Python \n","This is Fcc \n"] to #variable L, you can use any letter or word of your choice.
# Variable are containers in which values can be stored.
# The \n is placed to indicate the end of the line.

file.write("Hello There \n")
file.writelines(L)
file.close()

# Use the close() to change file access modes
'''

