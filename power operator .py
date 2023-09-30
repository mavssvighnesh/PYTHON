class PowerOperator:
    def __init__(self):
        pass
    
    # Implementing ** (power operation) as method '__pow__' 
    def __pow__(self, x, y=None): 
        if not isinstance(y, int):
            raise TypeError('Exponent must be integer')
        
        result = 1
        while y > 0: 
            if y & 1 == 1: 
                result *= x 
            
                # If exponent becomes odd after right shift by 1 bit  
                # multiply with base again so that next iteration has correct value   
            
            y >>= 1      # Right shifting bits by 1 position from left side    
            x *= x        # Multiplying Base with itself 
        
        return float(result)
    
p_oprtr = PowerOperator() 

# Testing our custom '**' Operator  
assert p_oprtr.__pow__(2, 3)==8 , "Custom Pow Function Failed"  

try : 
   print((p_oprtr).__pow__('a', 6)) 
except Exception as e:
   assert str(e)=="TypeError