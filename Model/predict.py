import pandas as pd
import pickle
#Import the model
with open("Model/model.pkl","rb") as f:
    model =pickle.load(f)

Model_version ="1.0.0"

# def predict_output(user_input:dict):

#     input_data =pd.DataFrame([user_input])# pass it list otherwise it raise index error

#     output =model.predict(input_data)[0]

#     return output


#Get the class labels from model (important for matching probabilities to class names)
class_labels =model.classes_.tolist()
def predict_output(user_input:dict):

    input_data =pd.DataFrame([user_input])# pass it list otherwise it raise index error

    predicted_class =model.predict(input_data)[0]

    #Get probabilities for all classes
    probabilities =model.predict_proba(input_data)[0]
    confidence =max(probabilities)

    #Create the mapping :{class_name:probabilities}
    class_probs =dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))


    return {
        "predicted_category":predicted_class,
        "confidence":round(confidence,4),
        "class_probabilities":class_probs
    }
