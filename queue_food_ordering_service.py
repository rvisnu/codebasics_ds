"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.


Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
"""

from collections import deque
import threading
import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

class FoodOrderingSystem:
    def __init__(self):
        self.fos = Queue()
    
    def place_order(self, order):
        for item in order:
            time.sleep(0.5)
            print(f"placing order for {item}")
            self.fos.enqueue(item)
    
    def serve_order(self):
        while not self.fos.is_empty():
            print(f"serving {self.fos.dequeue()}")
            time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    my_food_service = FoodOrderingSystem()
    start_time = time.time()
    
    thread_place_order = threading.Thread(target=my_food_service.place_order, args=(orders,))
    thread_serve_order = threading.Thread(target=my_food_service.serve_order, args=())
    
    thread_place_order.start()
    time.sleep(1)
    thread_serve_order.start()
    
    thread_place_order.join()
    thread_serve_order.join()
    end_time = time.time()
    print(end_time-start_time)
 
