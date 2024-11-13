from pydantic import BaseModel
from datetime import datetime
from typing import Union

class Recipe_Body(BaseModel):
    title:Union[str,None] = None
    making_time:Union[str,None] = None
    serves:Union[str,None] = None
    ingredients:Union[str,None] = None
    cost:Union[int,None] = None
    created_at:str = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    updated_at:str = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    
    
    
    
class Recipe():
    def __init__(self):
        self.recipes:list = []
        
    def data_set(self,res_data:list):
        for datum in res_data:
            self.recipes.append(datum)
            
    @property
    def data(self):
        return {"message":"Recipe details by id","recipe":self.recipes}
    
class Recipes():
    def __init__(self):
        self.recipes:list = []
        
    def data_set(self,res_data:list):
        for datum in res_data:
            self.recipes.append(datum)
            
    @property
    def data(self):
        return {"recipes":self.recipes}