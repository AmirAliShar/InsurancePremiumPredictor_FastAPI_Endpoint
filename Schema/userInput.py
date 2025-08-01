from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal,Annotated
from Config.city_tier import tier_1_cities,tier_2_cities


#pydantic model to validate incoming data
class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt =0,lt =120,description ='Age of the user')]
    weight:Annotated[float,Field(...,gt =0,description ='weight of the user')]
    height:Annotated[float,Field(...,gt =0,lt =2.5,description ='Height of the user')]
    income_lpa:Annotated[float,Field(...,gt =0,description ='Annual salary of the user in the lpa')]
    smoker:Annotated[bool,Field(...,description ='Is the user smoker')]
    city:Annotated[str,Field(...,description ='The City of the user')]
    occupation:Annotated[Literal["retired","freelancer","student",
                                 "Govt_Job","Business_owner","private_Job","Unemployed"],Field(...,description ='Occupation of the user')]
    


    #Apply the field validator on the city to convert the input into Title case
    @field_validator("city")
    @classmethod
    def city_title(cls,valid:str) -> str:
        valid = valid.strip().title()
        return valid
    
    #Computed field
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight /(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi >30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return 'medium'
        else:
            return 'low'
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age <45:
            return 'adult'
        elif self.age <60:
            return 'middle_aged'
        else:
            return 'senior'
    @computed_field
    @property
    def city_tier(self)-> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3