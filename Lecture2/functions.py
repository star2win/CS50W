def square(x):
    return x * x

def main():
    for i in range(10):
        print(f"{i} squared is {square(i)}")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    main()