import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import Counter, make_asgi_app
from pydantic import BaseModel

#land_counter = Counter("land", "Counter for land")
#not_land_counter = Counter("not_land", "Counter for not land")

# chargement de modèle
loan_model = joblib.load("loan_tree.joblib")

# création d'une nouvelle instance FastAPI
app = FastAPI()

#metrics_app = make_asgi_app()
#app.mount("/metrics", metrics_app)


class request_body(BaseModel):
     
     FlightNumber: int
     PayloadMass: float
     Flights: int
     Block: int
     ReusedCount: int
     Orbit_ES_L1: int
     Orbit_GEO: int
     Orbit_GTO: int
     Orbit_HEO: int
     Orbit_ISS: int
     Orbit_LEO: int
     Orbit_MEO: int
     Orbit_PO: int
     Orbit_SO: int
     Orbit_SSO: int
     Orbit_VLEO: int
     LaunchSite_CCAFS_SLC_40: int
     LaunchSite_KSC_LC_39A: int
     LaunchSite_VAFB_SL_4E: int
     LandingPad_5e9e3032383ecb267a34e7c7: int
     LandingPad_5e9e3032383ecb554034e7c9: int
     LandingPad_5e9e3032383ecb6bb234e7ca: int
     LandingPad_5e9e3032383ecb761634e7cb: int
     LandingPad_5e9e3033383ecbb9e534e7cc: int
     Serial_B0003: int
     Serial_B0005:int
     Serial_B0007: int
     Serial_B1003: int
     Serial_B1004: int
     Serial_B1005: int
     Serial_B100: int
     Serial_B1007: int
     Serial_B1008: int
     Serial_B1010 : int
     Serial_B1011: int
     Serial_B1012 : int
     Serial_B1013: int
     Serial_B1015: int
     Serial_B1016: int
     Serial_B1017: int
     Serial_B1018: int
     Serial_B1019: int
     Serial_B1020: int
     Serial_B1021: int
     Serial_B1022 : int
     Serial_B1023: int
     Serial_B1025: int
     Serial_B1026: int
     Serial_B1028: int
     Serial_B1029: int
     Serial_B1030: int
     Serial_B1031: int
     Serial_B1032: int
     Serial_B1034: int
     Serial_B1035: int
     Serial_B1036: int
     Serial_B1037: int
     Serial_B1038: int
     Serial_B103: int
     Serial_B1040: int
     Serial_B1041: int
     Serial_B1042: int
     Serial_B1043: int
     Serial_B1044: int
     Serial_B1045: int
     Serial_B1046: int
     Serial_B1047: int
     Serial_B1048: int
     Serial_B1049: int
     Serial_B1050: int
     Serial_B1051: int
     Serial_B1054: int
     Serial_B1056: int
     Serial_B1058: int
     Serial_B1059: int
     Serial_B1060: int
     Serial_B1062: int
     GridFins_False: int
     GridFins_True: int
     Reused_False: int
     Reused_True: int
     Legs_False: int
     Legs_True: int

# Définir le chemin de point terminaison
@app.get("/Space_X")

def prediction(data : request_body) :
    new_data =[[
        data.FlightNumber,
        data.PayloadMass,
        data.Flights,
        data.Block,
        data.ReusedCount,
        data.Orbit_ES_L1,
        data.Orbit_GEO,
        data.Orbit_GTO,
        data.Orbit_HEO,
        data.Orbit_ISS,
        data.Orbit_LEO,
        data.Orbit_MEO,
        data.Orbit_PO,
        data.Orbit_SO,
        data.Orbit_SSO,
        data.Orbit_VLEO,
        data.LaunchSite_CCAFS_SLC_40,
        data.LaunchSite_KSC_LC_39A,
        data.LaunchSite_VAFB_SL_4E,
        data.LandingPad_5e9e3032383ecb267a34e7c7,
        data.LandingPad_5e9e3032383ecb554034e7c9,
        data.LandingPad_5e9e3032383ecb6bb234e7ca,
        data.LandingPad_5e9e3032383ecb761634e7cb,
        data.LandingPad_5e9e3033383ecbb9e534e7cc,
        data.Serial_B0003,
        data.Serial_B0005,
        data.Serial_B0007,
        data.Serial_B1003,
        data.Serial_B1004,
        data.Serial_B1005,
        data.Serial_B100,
        data.Serial_B1007,
        data.Serial_B1008,
        data.Serial_B1010,
        data.Serial_B1011,
        data.Serial_B1012,
        data.Serial_B1013,
        data.Serial_B1015,
        data.Serial_B1016,
        data.Serial_B1017,
        data.Serial_B1018,
        data.Serial_B1019,
        data.Serial_B1020,
        data.Serial_B1021,
        data.Serial_B1022,
        data.Serial_B1023,
        data.Serial_B1025,
        data.Serial_B1026,
        data.Serial_B1028,
        data.Serial_B1029,
        data.Serial_B1030,
        data.Serial_B1031,
        data.Serial_B1032,
        data.Serial_B1034,
        data.Serial_B1035,
        data.Serial_B1036,
        data.Serial_B1037,
        data.Serial_B1038,
        data.Serial_B103,
        data.Serial_B1040,
        data.Serial_B1041,
        data.Serial_B1042,
        data.Serial_B1043,
        data.Serial_B1044,
        data.Serial_B1045,
        data.Serial_B1046,
        data.Serial_B1047,
        data.Serial_B1048,
        data.Serial_B1049,
        data.Serial_B1050,
        data.Serial_B1051,
        data.Serial_B1054,
        data.Serial_B1056,
        data.Serial_B1058,
        data.Serial_B1059,
        data.Serial_B1060,
        data.Serial_B1062,
        data.GridFins_False,
        data.GridFins_True,
        data.Reused_False,
        data.Reused_True,
        data.Legs_False,
        data.Legs_True
    ]]

    prediction = loan_model.predict(new_data)[0]
    eligible = int(prediction) == 1
    return eligible
    
   

# We acknowledge that the number of features is 20, and it's significantly difficult to write all of them in the URL. 
# Hence we give this example to run : 
# http://127.0.0.1:9090/reda?checking_account_status=1&duration_months=12&credit_history=1&purpose=2&credit_amount=5000&savings_account=1&employment_duration=2&installment_rate=3&personal_status_sex=1&other_debtors_guarantors=2&residence_duration=4&property=2&age_years=30&other_installment_plans=1&housing=2&existing_credits_at_bank=1&job=3&people_liable_for_maintenance=2&telephone=1&foreign_worker=2


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9090)
