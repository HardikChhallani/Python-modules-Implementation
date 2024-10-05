# Implemented using time and os module with id of the session
import os
import time
from datetime import datetime

class Solution:
    def __init__(self):
        now = datetime.now()
        self.hr = now.hour
        self.state = (int(time.time()*1000)^os.getpid()) & 0xFFFFFFFF
    def random(self):
        self.state ^= (self.state<<self.hr) & 0xFFFFFFFF
        self.state ^= (self.state>>24 - self.hr) & 0xFFFFFFFF
        self.state ^= (self.state<<int((self.hr))) & 0xFFFFFFFF
        return (self.state)/(2**32)
    def randint(self,a,b):
        return a+(int(self.random()*(b-a+1)))
    
if __name__=="__main__":
    rng = Solution()
    print("The floating point b/w 0 & 1 is \n",rng.random())
    print("The integer b/w 10 & 100  is \n",rng.randint(10,100))
    print("The integer b/w 1 & 10 is \n",rng.randint(1,10))
