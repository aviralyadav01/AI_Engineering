from pydantic import BaseModel

#defining rules in class with the class inherting base model class 
class User(BaseModel):
    id : int 
    name : str 
    age : int 
    email : str 
    is_active : bool = True 

user_1 = User( id = '1' , name =  'Avi' , age = 22 ,email = 'avi@gmail.com' , is_active= True)
# here pydantic parsed the "1" string to int 1 ;

print(user_1)