def func():
    print('This is a message from the function in the imported module.')


print(f'This is a message from {__name__}.')

if __name__ == "__main__": # Make a change here (add a main block)
    print('This should not be printed when this file is imported')

