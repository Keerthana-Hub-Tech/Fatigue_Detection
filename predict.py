import pickle
import pandas as pd

# Load trained model
with open("fatigue_model.pkl", "rb") as f:
    model = pickle.load(f)

def main():
    print("Cognitive Fatigue Detection System")
    print("-----------------------------------")

    # Take input from user
    try:
        avg_key_interval = float(input("Enter average key interval (seconds): "))
        typing_speed = float(input("Enter typing speed (WPM): "))
        backspace_rate = float(input("Enter backspace rate (per min): "))
        avg_mouse_speed = float(input("Enter average mouse speed: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Create DataFrame with EXACT same feature names used in training
    data = pd.DataFrame([[avg_key_interval, typing_speed, backspace_rate, avg_mouse_speed]],
                        columns=["avg_key_interval", "typing_speed", "backspace_rate", "avg_mouse_speed"])

    # Predict
    prediction = model.predict(data)

    # Map prediction to labels
    labels = ["Fresh", "Mild", "Fatigue"]
    predicted_label = labels[int(prediction[0])]  # convert numpy int64 to Python int

    print("\nPredicted Cognitive State:", predicted_label)

if __name__ == "__main__":
    main()