# src/emotion.py
def detect_emotion(sensor_input):
    return "calm" if sensor_input < 0.5 else "stressed"
