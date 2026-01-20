"""
Cybersecurity Simulation: Generative Virus vs. Predictive Vaccine
Author: [Giancarlo neves]
Description: A technical simulation of an AI-driven "arms race" between a polymorphic
phishing generator and a Machine Learning-based defense system.
"""

import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, classification_report


class PhishingAI:
    """
    The 'Virus' (Generative AI):
    Simulates a polymorphic threat that generates unique phishing emails
    to bypass static signature-based filters.
    """

    def __init__(self):
        self.subjects = [
            "Urgent: Security Alert",
            "Invoice #9921 Payment Overdue",
            "HR: Salary Adjustment",
            "Action Required: Account Verification",
            "New Login Detected from Unknown Device"
        ]

        self.bodies = [
            "We noticed suspicious activity on your account.",
            "Your payment was declined by your bank.",
            "Please update your direct deposit information immediately.",
            "A security breach has been detected in your region.",
            "Your subscription will be suspended within 24 hours."
        ]

        self.actions = [
            "Click here to verify.",
            "Download the attachment now.",
            "Login to secure your account.",
            "Follow this link to resolve the issue.",
            "Contact support via the portal below."
        ]

    def generate_attack(self, n=1):
        attacks = []
        for _ in range(n):
            subject = random.choice(self.subjects)
            body = random.choice(self.bodies)
            action = random.choice(self.actions)
            attacks.append(f"Subject: {subject} | Body: {body} {action}")
        return attacks


def run_simulation():
    # 1. TRAINING DATA (The Vaccine / A Vacina)
    # Teaching the model what is 'MALICIOUS' and what is 'SAFE'
    training_data = [
        ("Urgent: Security Alert suspicious activity", "MALICIOUS"),
        ("Invoice Payment Overdue Download", "MALICIOUS"),
        ("HR: Salary Adjustment Login", "MALICIOUS"),
        ("Action Required: Account Verification Click here", "MALICIOUS"),
        ("New Login Detected from Unknown Device secure your account", "MALICIOUS"),
        ("Meeting reminder for tomorrow at 10am", "SAFE"),
        ("Happy Birthday! Let's celebrate this weekend", "SAFE"),
        ("Project update and weekly report attached", "SAFE"),
        ("Lunch menu for today is pasta", "SAFE"),
        ("Please review the documentation for the new API", "SAFE")
    ]

    X_train = [text for text, label in training_data]
    y_train = [label for text, label in training_data]

    # 2. IMMUNE SYSTEM ARCHITECTURE (Pipeline)
    # Vectorization (DNA Sequencing) + Classification (Antibodies)
    vaccine_model = make_pipeline(CountVectorizer(), MultinomialNB())
    vaccine_model.fit(X_train, y_train)

    # 3. REAL-TIME DEFENSE (The Battle)
    virus_bot = PhishingAI()
    new_attacks = virus_bot.generate_attack(5)

    print("=" * 60)
    print("--- CYBERSECURITY SIMULATION: VACCINE DIAGNOSTIC ---")
    print("=" * 60)

    for attack in new_attacks:
        prediction = vaccine_model.predict([attack])[0]
        confidence = vaccine_model.predict_proba([attack]).max() * 100
        print(f"\n[INCOMING THREAT]: {attack}")
        print(f"[DIAGNOSTIC]: {prediction} ({confidence:.2f}% Confidence)")
        print("-" * 40)

    # 4. EVALUATION (Confusion Matrix Simulation)
    # Let's simulate a larger test set to show metrics
    y_true = ["SAFE"] * 50 + ["MALICIOUS"] * 50
    # Simulating some errors (False Positives and False Negatives)
    y_pred = ["SAFE"] * 45 + ["MALICIOUS"] * 5 + ["MALICIOUS"] * 42 + ["SAFE"] * 8

    print("\n" + "=" * 60)
    print("--- CRITICAL EVALUATION (METRICS) ---")
    print("=" * 60)
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_true, y_pred, labels=["SAFE", "MALICIOUS"])
    print(f"TN: {cm[0][0]} | FP: {cm[0][1]} (False Alarm)")
    print(f"FN: {cm[1][0]} (Infection!) | TP: {cm[1][1]}")

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=["SAFE", "MALICIOUS"]))

    recall_malicious = cm[1][1] / (cm[1][1] + cm[1][0])
    print(f"RECALL (Sensitivity) for Malicious: {recall_malicious:.2%}")
    print("\nNOTE: In Cybersecurity, a False Negative (FN) is much more dangerous than a False Positive (FP).")
    print("Recall is vital because it measures our ability to catch the virus before it spreads.")


if __name__ == "__main__":
    run_simulation()
