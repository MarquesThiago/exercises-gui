
class Calculator():
   
    def __init__(self, entry):

       self.__result = 0
       self.__temp   = []
       self.__operation = []
       self.__entry  = entry
       


    def click_calc(self, value): 

        if(value in ('+', '-', '/', '*')):
            self._input_operator(value)
        elif(value in (1,2,3,4,5,6,7,8,9,0)):
            self._input_number(value)
        elif(value == "result"):
            self._input_equal()
        elif(value == "del"):
            self._input_clear()
        else: 
            raise Exception('Error invalid parameter', "Message: parameter in function 'click_calc', don't type experied, impossible of the work")


    def _print_screen (self, value):

        actual  = self.__entry.get()
        self._clear()
        self.__entry.insert(0, actual + str(value))
       

    def _input_number(self, value ):
        self._print_screen(value)
        self.__temp.append(value)
        

    def _input_operator(self, value):
        self._print_screen(value)
        self.__operation.append(value)
        
        if (len(self.__operation) == 1):
        
            self.__result = float("".join([str(n) for n in self.__temp]))
        
        elif(len(self.__operation) == 2 ):
        
            self._test_operation()
        
        self.__temp = []
      
       

    def _clear(self):
        self.__entry.delete(0,len(self.__entry.get()))


    def _input_clear(self):
        self.__operation = []
        self.__result = 0
        self.__temp = []
        self._clear()
        

    
    def _input_equal(self):
        self._test_operation()
        self._clear()
        self._print_screen(self.__result)


    def _test_operation(self):
        
        if(self.__operation[0] == "+"):
            
            self.__result = self.__result + float(''.join([str(n) for n in self.__temp]))
            
            self._clear_variates()

        elif(self.__operation[0]== "-"):
        
            self.__result = self.__result - float(''.join([str(n) for n in self.__temp]))
            self._clear_variates()
        
        elif(self.__operation[0]== "*"):
            self.__result = self.__result * float(''.join([str(n) for n in self.__temp]))
            self._clear_variates()
        
        elif(self.__operation[0]== "/"):
            self.__result = self.__result / float(''.join([str(n) for n in self.__temp]))
            self._clear_variates()
        

    def _clear_variates(self):
        self.__operation.remove(self.__operation[0])

    def relatory (self, point):
        print(point)

        print(f"return: {self.__result}",
            f"temp :  {self.__temp}",
            f"operation: {self.__operation}")