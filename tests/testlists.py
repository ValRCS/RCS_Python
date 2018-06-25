import random

class ListTester:
    '''
    List comprehensions tester
    Usage:
    create new instance with q = ListTester()
    q.check(mylistanswer) - check your list against answer, must be list
    ie. mylist = [x*2 for x in range(20)]
    q.check(mylist)
    q.hint - get hint of increasing length
    q.newProb - generate new problem
    q.guesses - how many guesses made in current problem
    q.solved - how many problems you've solved in this session
    '''
    def __init__(self, maxlist=100, maxstep=5):
        self._regenProb(maxlist, maxstep)
        self.solved = 0


    def _regenProb(self, maxlist=100, maxstep=5):
        self._beg = random.randint(1,maxlist)
        self._step = random.randint(1, maxstep)
        self._end = random.randint(self._beg+10*self._step, self._beg+maxlist)
        self._mult = random.randint(1,10)
        self._mmod= random.randint(1,7+1)
        self._hintlen = 3 # for showing partial lists
        self.guesses = 0
        if self._mmod > 1:
            if self._step == self._mmod: #possible to have an empty list then
                self._mmod += 1
            self._compreh = f'[(x, x*{self._mult}) for x in range({self._beg},{self._end},{self._step}) if x % {self._mmod}]'     
            # print(f'making filter with {mmod}')
        else:
            self._compreh = f'[(x, x*{self._mult}) for x in range({self._beg},{self._end},{self._step})]'
        self._list=eval(self._compreh)
        print(f'New List Problem for a list with {len(self._list)} elements')
        print('Use myvar.hint() to get hints, and myvar.check(mynewlist) to check answers')
        self._printHint()


    def _printHint(self):
        print(f'First {self._hintlen} elements', self._list[:self._hintlen])
        print(f'Last {self._hintlen} elements', self._list[-self._hintlen:])

    def hint(self):
        if self._hintlen < len(self._list):
            self._hintlen += 1
            self._printHint()
        else:
            print("Hints exhausted! Answer is:", self._compreh)
    
    def check(self, tlist):
        self.guesses += 1
        if (type(tlist) != list):
            print("Sorry that's not a list that you gave me!")
            return
        if tlist == self._list:
            print(f"Nicely done in {self.guesses} trie(s)! Is your list comprehension similar to ours?", self._compreh)
            self.solved += 1
            print(f"You've solved {self.solved} problem(s) so far. Sweet!")
        else:
            print("Your list does not match ours. Try again or perhaps try a new hint? Could always try a new prob as well...")
            print(f"Remember your list must be {len(self._list)} long")
            print(f'Guesses used {self.guesses}')
    
    def newProb(self):
        self._regenProb()


