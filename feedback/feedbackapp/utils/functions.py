import random

def generate_id(length=10):
    id = '11'
    
    for _ in range(length):
        id += str(random.randint(0, 9))
        
    print(id)    
    
    
  
  
if __name__ == '__main__':   
    print("Random ID: ", generate_id())    