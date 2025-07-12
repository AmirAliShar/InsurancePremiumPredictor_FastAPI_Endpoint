from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.userInput import UserInput
from Schema.prediction_responseModel import PredictionResponseModel
from Model.predict import predict_output,model,Model_version
app =FastAPI()

#Add the home URL 
#Human readable
@app.get("/")
def home():
    return {'message':"Insurance premium predictor API"} 

#Health check (it is help in hosting)
#Machine readable
@app.get('/health')
def health_check():
    return {
        "status":'ok',
        "model_loaded": model is not None,
        "version":Model_version
    }

@app.post("/predict",response_model =PredictionResponseModel)
def predict_premium(data:UserInput):
    user_input ={
        "bmi":data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        "income_lpa":data.income_lpa,
        "occupation":data.occupation
    }
    try:
        prediction =predict_output(user_input)

        return JSONResponse (status_code =200 ,content ={"response":prediction})
    except Exception as e:
        return JSONResponse (status_code=500,content=str(e))



