def print_hello(num:int):
    """
    Print hello
    """
    for i in range(num):
        print(f'{i}times hello')
        if i % 2 == 0:
            print(f'hello for {i+1}th times')
if __name__=='__main__':
    print_hello(10)
