SIZE=5
queue=[None]*SIZE
front=-1
rear=-1
def isEmpty():
    return front==-1 or front>rear

def isFull():
    return rear==SIZE-1
def enqueue(value):
    global front,rear
    if isFull():
        print ("Queue is Full")
    else:
        if front==-1:
            front=0
        rear+=1
        queue[rear]=value
        print("",value," inserted into the queue")

def dequeue():
    global front,rear
    if isEmpty():
        print ("Queue is Empty")
    else:
        print("",queue[front]," is removed successfully")
        front+=1
        if front>rear:
            front=rear=-1

def Size():
    if isEmpty():
        return 0
    return rear-front+1
def show():
    if isEmpty():
        print("Queue is full")
    else:
        print("Queue elements are:")
        for i in range (front,rear+1):\
            print(queue[i],end="->")
        print()


while True:
    print("Main menu")
    print("1. enqueue")
    print("2. dequeue")
    print("3. display")
    print("4. size")
    print("5. exit")

    ch=input("enter the choice:")
    if ch=='1':
        val=input("enter the value")
        enqueue(val)
    elif ch=='2':
        dequeue()
    elif ch=='3':
        show()
    elif ch=='4':
        print("Size of queue:",Size())
    elif ch=='5':
        print("program ended")
        break

    else:
        print("enter the valid input")