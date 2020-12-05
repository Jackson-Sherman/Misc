class Stack:
    def __init__(self):
        self.data = []
        self.length = 0
        
    def empty(self):
        """
        returns a boolean. True if Stack is empty, False otherwise
        """
        return bool(self.length == 0)

    def push(self, value):
        self.data = [value] + self.data
        self.length += 1
        return self
    
    def pop(self):
        if not self.empty():
            output = self.data[0]
            self.data = self.data[1:]
            self.length -= 1
            return output

    def __str__(self):
        return "⦗" + str(self.data)[1:-1] + "⦘"

class Queue:
    def __init__(self):
        self.data = []
        self.length = 0
        
    def empty(self):
        """
        returns a boolean. True if Stack is empty, False otherwise
        """
        return bool(self.length == 0)

    def push(self, value):
        self.data += [value]
        self.length += 1
        return self
    
    def pop(self):
        if not self.empty():
            output = self.data[0]
            self.data = self.data[1:]
            self.length -= 1
            return output

    def __str__(self):
        return "⦗" + str(self.data)[1:-1] + "⦘"
# It works!
# if __name__ == "__main__":
#     print("\n"+"="*8+"\n")
#     x = Stack()
#     print(x)
#     print("\n"+"="*8+"\n")
#     print("push(5)")
#     x.push(5)
#     print(x)
#     print("\n"+"="*8+"\n")
#     print("push(3)")
#     x.push(3)
#     print(x)
#     print("\n"+"="*8+"\n")
#     print("pop()")
#     print(x.pop())
#     print(x)
#     print("\n"+"="*8+"\n")
#     print("pop()")
#     print(x.pop())
#     print(x)
#     print("\n"+"="*8+"\n")