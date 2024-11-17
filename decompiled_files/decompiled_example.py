# Source Generated with Decompyle++
# File: example.cpython-39.pyc (Python 3.9)


def greet(name):
    return f'''Hello, {name}!'''

if __name__ == '__main__':
    user_name = input('Enter your name: ')
    greeting = greet(user_name)
    print(greeting)
