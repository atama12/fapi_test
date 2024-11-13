from fastapi import FastAPI,Response,status
from dotenv import load_dotenv
from supabase import create_client, Client
from classes import Recipes,Recipe,Recipe_Body
from datetime import datetime
load_dotenv()
import os

app = FastAPI()

url:str = os.getenv('SUPABASE_URL')
key:str = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(url, key)

@app.get("/recipes",status_code=200)
def recipes(response:Response):
    
    try:
        res = supabase.schema("FastAPI_Test").table("recipes").select("id,title,making_time,serves,ingredients,cost").execute()
        if res.data == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message":"data is not found"}
        
        else:
            
            recipes = Recipes()
            
            recipes.data_set(res.data)
            
            return recipes.data
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"database error"}

@app.get("/recipes/{id}",status_code=200)
def recipes_id(id:int,response:Response):
    try:
        res = supabase.schema("FastAPI_Test").table("recipes").select("id,title,making_time,serves,ingredients,cost").eq("id",id).execute()
        
        if res.data == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message":"data is not found"}
        
        else:
            recipes = Recipe()
            
            recipes.data_set(res.data)
            
            return recipes.data
        
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"database error"}

@app.post("/recipes",status_code=200)
def recipe_post(body:Recipe_Body,response:Response):
    
    try:
        res= supabase.schema("FastAPI_Test").table("recipes").insert(body.model_dump()).execute()
    
        return {
            "message": "Recipe successfully created!",
             "recipe": [{"id":res.data[0]["id"],"title":body.title,"making_time":body.making_time,"serves":body.serves,"ingredients":body.ingredients,"cost":str(body.cost),"created_at":body.created_at,"updated_at":body.updated_at}]
        }
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": "Recipe creation failed!",
            "required": "title, making_time, serves, ingredients, cost"
        }
        
@app.patch("/recipes/{id}",status_code=200)
def recipe_patch(id:int,body:Recipe_Body,response:Response):
    
    try:
        body.updated_at = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
        res= supabase.schema("FastAPI_Test").table("recipes").update(body.model_dump(exclude_unset=True)).eq("id",id).execute()
    
        print(res.data)
        return {
            "message": "Recipe successfully updated!",
            "recipe": [body.model_dump(exclude_unset=True)]
        }
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": "Recipe update failed!"
        }
        
@app.delete("/recipes/{id}",status_code=200)
def recipe_patch(id:int,response:Response):
    
    try:
        res= supabase.schema("FastAPI_Test").table("recipes").delete().eq("id",id).execute()
    
        if res.data == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message":"no Recipe found"}
        else:
            return {
                "message": "Recipe successfully removed!"
            }
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": "no Recipe found"
        }