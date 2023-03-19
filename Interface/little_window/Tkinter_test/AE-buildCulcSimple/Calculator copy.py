
class Calculator():
   
    def __init__(self, entry):

       self.__result = 0
       self.__temp   = []
       self.__operation = []
       self.__number1 = 0
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
        print(value)
        self.relatory(point = "input numero antes dp aénder e de execução de operação")
        self.__temp.append(value)
        self._execute_operation(value)
        self.relatory(point = "depois ")

    def _input_operator(self, value):
        
        self._print_screen(value)
        if len(self.__temp) >= 2:
            self.__number1 = float("".join([str(n) for n in self.__temp]))
        elif len(self.__temp) == 1:
            self.__number1 = self.__temp[0] 
        self.__operation.append(value)
        self.relatory(point = "depois do operador ")
       

    def _clear(self):
        self.__entry.delete(0,len(self.__entry.get()))


    def _input_clear(self):
        self.__operation = []
        self.__result = 0
        self.__temp = []
        self._clear()
        

    
    def _input_equal(self):
        self._execute_operation(0, equal = True)
        self._clear()
        self._print_screen(self.__result)


    def _execute_operation(self, value, equal = False):
        self.relatory(point = "inicio da execução ")
        if (len (self.__operation) == 2):
            self._test_operation(value)
            self._clear_variates()
        elif(len(self.__operation) == 1 ):
            self.__temp = []
        elif (len(self.__operation) >= 1 and equal):
            self._test_operation(value)
        else:
           print("fora")
    
        self.relatory(point = "depois da execução ")

    def _test_operation(self,  value):
        if(self.__operation[0] == "+"):
            self.__result = self.__number1 + value
            self._clear_variates()
        elif(self.__operation[0]== "-"):
            self.__result = self.__number1 - value
            self._clear_variates()
        elif(self.__operation[0]== "*"):
            self.__result = self.__number1 * value
            self._clear_variates()
        elif(self.__operation[0]== "/"):
            self.__result = self.__number1 / value
            self._clear_variates()
        
        self.relatory(point = "depois do teste dos operadores")

    def _clear_variates(self):
        self.__operation.remove(self.__operation[0])
        self.__temp = []    


    def relatory (self, point):
        print(point)

        print(f"return: {self.__result}",
            f"temp :  {self.__temp}",
            f"number: { self.__number1}",
            f"operation: {self.__operation}")