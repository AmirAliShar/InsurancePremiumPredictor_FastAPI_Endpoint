from pydantic import BaseModel,Field
from typing import Dict

class PredictionResponseModel(BaseModel):
    predicted_category :str = Field(...,
                                    description ='The predicted insurance premium category',example ='High')
    confidence:float =Field(...,description= "model's confidence score for the predicted class ",example = 0.24)

    class_probabilites :Dict[str,float] =Field(...,
                                               description ="Probability distribution across all possible classes",
                                               example ={"Low":0.2,"Medium":0.5,"High":0.3})