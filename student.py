#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 79
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "v": ("Scott Test", self.square),
                "w": ("Forward W/Stop", self.stop2),
                "g": ("Forward W/Spin", self.spin),
                "z": ("travel", self.travel), 
                "y": ("DistanceCheck", self.distance),
                "p": ("scan", self.scan),
                "m": ("maze", self.maze)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your Selection: "
        ))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    
    def maze(self):
      while True: 
        self.fwd()
        if(self.read_distance()<135):
          self.stop()
          self.servo(self.MIDPOINT -400)
          time.sleep(1)
          self.stop()
          if(self.read_distance()<135):
            self.left(primary=80, counter=-80)
            time.sleep(.5)
            self.stop()
            self.servo(self.MIDPOINT)
          elif (self.read_distance() > 135):
            self.right(primary=80, counter=-80)
            time.sleep(.5)
            self.stop()
            self.servo(self.MIDPOINT)

        
        """
        self.servo(self.MIDPOINT)
        forward = self.read_distance()

        if (forward < 350):
          self.stop()
          self.servo(self.MIDPOINT + 400)
          right = self.read_distance()
          self.servo(self.midpoint - 400)
          left = self.read_distance()

          if (right > 350)
          
          
          
          
          #incase of deadend
          if (left < 350, right < 350):
            self.left()
            time.sleep(1.5)
            self.fwd()
          """

          

    def swerveright(self):
              self.right(primary=90, counter=70)
              time.sleep(1)
              self.left(primary=90, counter=45)
              time.sleep(1)
              self.fwd()
    
    def swerveleft(self):
              self.left(primary=90, counter=70)
              time.sleep(1)
              self.right(primary=90, counter=45)
              time.sleep(1)
              self.fwd()

    def scan(self):      
      while True:

          self.fwd()
        
          self.servo(self.MIDPOINT + 400)
          time.sleep(.25)
          libby1 = self.read_distance()


          if(libby1 < 310):
            self.stop()
            self.servo(self.MIDPOINT)
            time.sleep(.25)
            if (self.read_distance() > 310):
              self.swerveright()

            else:
              self.distance()


          
          self.servo(self.MIDPOINT - 400)
          time.sleep(.25)
          libby3 = self.read_distance()

          if(libby3 < 310):
            self.stop()
            self.servo(self.MIDPOINT)
            time.sleep(.25)
            if (self.read_distance() > 310):
              self.swerveleft()

            else:
              self.distance()



    def distance(self):
        if(self.read_distance() > 310):
          self.fwd()
        elif(self.read_distance() < 310):
          self.stop()
          self.servo(self.MIDPOINT)

          first = self.read_distance()
          self.servo(self.MIDPOINT + 400)
          time.sleep(.75)
          self.stop()

          second = self.read_distance()
          self.servo(self.MIDPOINT - 400)
          time.sleep(.75)
          self.stop()
          
          if (first > second):
            self.right()
            time.sleep(1)
            self.stop()
            self.servo(self.MIDPOINT)
            self.fwd()
            
          elif (second > first):
            self.left()
            time.sleep(.75)
            self.stop()
            self.fwd()
            time.sleep(.75)
            self.right()
            self.servo(self.MIDPOINT)
            self.fwd()
        

        

    def travel(self):
      while True:
        if(self.read_distance() > 310):
          self.fwd()
        elif(self.read_distance() < 310):
          self.stop()
          self.servo(self.MIDPOINT)
          time.sleep(.75)
          self.stop()


          first = self.read_distance()
          self.servo(self.MIDPOINT + 400)
          time.sleep(.75)
          self.stop()


         
          second = self.read_distance()
          self.servo(self.MIDPOINT - 400)
          time.sleep(.75)
          self.stop()
          
          if (first > second):
            self.right()
            time.sleep(1)
            self.stop()
            self.servo(self.MIDPOINT)
            self.fwd()
            
          elif (second > first):
            self.left()
            time.sleep(.75)
            self.stop()
            self.fwd()
            time.sleep(.75)
            self.right()
            self.servo(self.MIDPOINT)
            self.fwd()
            
          
          
          else:
            self.back(.5)
            self.read_distance()
            
          





    def spin(self):
      while True:
        if self.read_distance() < 180:
          self.stop()
          self.right(primary = 40, counter = -40)
          time.sleep(.85)
          self.fwd()
        else:
          self.fwd()
      


    def stop2(self):
      while True:
        if self.read_distance() < 90:
          self.stop()
        else:
          self.fwd()

    def square(self):
      for _ in range(4):  
        self.fwd()
        time.sleep(2)
        self.stop()
        self.right(primary = 40, counter = -40)
        time.sleep(2)
        self.stop()



      
    def dance(self):
      self.fwd()
      time.sleep(1)
      self.stop()
      self.back()
      time.sleep(1)
      self.stop()
      self.right(primary = 100, counter = -100)
      time.sleep(5)
      self.stop()

       
        

    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
