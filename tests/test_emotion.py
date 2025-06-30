def test_emotion_detection():
    from emotion import detect_emotion
    assert detect_emotion(0.4) == "calm"
    assert detect_emotion(0.6) == "stressed"
