import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import Counter, make_asgi_app

land_counter = Counter("land", "Counter for land")
not_land_counter = Counter("not_land", "Counter for not land")

# chargement de modèle
loan_model = joblib.load("loan_svm.joblib")

# création d'une nouvelle instance FastAPI
app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

#metrics_app = make_asgi_app()
#app.mount("/metrics", metrics_app
    

# Définir le chemin de point terminaison
@app.post("/Space_X")

def prediction(FlightNumber: int, PayloadMass: float , Flights: int , Block: int , ReusedCount: int) :
    data = [FlightNumber, PayloadMass, Flights, Block, ReusedCount]

    prediction = loan_model.predict(pd.DataFrame(data).transpose())
    land = int(prediction)==1
    if land:
        land_counter.inc()
        return " land"
    else:
        not_land_counter.inc()
        return "not land"

    return prediction
    

# We acknowledge that the number of features is 20, and it's significantly difficult to write all of them in the URL. 
# Hence we give this example to run : 
# http://127.0.0.1:9090/reda?checking_account_status=1&duration_months=12&credit_history=1&purpose=2&credit_amount=5000&savings_account=1&employment_duration=2&installment_rate=3&personal_status_sex=1&other_debtors_guarantors=2&residence_duration=4&property=2&age_years=30&other_installment_plans=1&housing=2&existing_credits_at_bank=1&job=3&people_liable_for_maintenance=2&telephone=1&foreign_worker=2


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9090)



