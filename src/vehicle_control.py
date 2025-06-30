# src/vehicle_control.py
def adjust_vehicle_behavior(emotion):
    if emotion == "calm":
        return "Maintain cruise control"
    elif emotion == "stressed":
        return "Activate soothing systems and reduce speed"
