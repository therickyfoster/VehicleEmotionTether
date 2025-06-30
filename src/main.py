# src/main.py
from sensors import read_input
from emotion import detect_emotion
from vehicle_control import adjust_vehicle_behavior

def main():
    sensor_input = read_input()
    emotion = detect_emotion(sensor_input)
    action = adjust_vehicle_behavior(emotion)
    print(f"Emotion: {emotion}, Action: {action}")

if __name__ == "__main__":
    main()
