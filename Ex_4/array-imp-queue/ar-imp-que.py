SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1


def isEmpty():
    return front == -1 or front > rear


def isFull():
    return rear == SIZE - 1


def enqueue(value):
    global rear, front
    if isFull():
        print("Queue is FULL!!! Insertion not possible!")
        return
    if front == -1:
        front = 0
    rear += 1
    queue[rear] = value
    print(f"Inserted {value} into queue.")


def dequeue():
    global front, rear
    if isEmpty():
        print("Queue is EMPTY!!!")
        return
    print(f"Deleted element: {queue[front]}")
    front += 1
    if front > rear:
        front = rear = -1
def size():
    if isEmpty():
        return 0
    return rear - front + 1


def show():
    if isEmpty():
        print("Queue is EMPTY!!!")
    else:
        print("Queue elements are:", end=" ")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()


while True:
    print("\n=== Queue Operations ===")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Check if Queue is Empty")
    print("4. Get Queue Size")
    print("5. Show Queue")
    print("6. Exit")
   
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        value = input("Enter the value to insert: ")
        enqueue(value)
    elif choice == '2':
        dequeue()
    elif choice == '3':
        print("Queue is Empty" if isEmpty() else "Queue is NOT Empty")
    elif choice == '4':
        print(f"Queue size = {size()}")
    elif choice == '5':
        show()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter between 1-6.")
