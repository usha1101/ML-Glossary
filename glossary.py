ML_GLOSSARY = {
    "model": "A representation of a system or process. In ML, a model is the output of a training algorithm that makes predictions.",
    "neural network": "A computing system inspired by the brain's structure, consisting of interconnected nodes (neurons).",
    "deep learning": "A subfield of machine learning based on artificial neural networks with many layers (deep neural networks).",
    "tensorflow": "An open-source library developed by Google for machine learning and artificial intelligence tasks.",
    "classification": "An ML task that involves predicting a category or class label. For example, 'spam' or 'not spam'.",
    "regression": "An ML task that involves predicting a continuous value. For example, predicting the price of a house."
}

def main():
    """Main function to run the glossary lookup tool."""
    print("=" * 30)
    print("  Welcome to the ML Glossary!")
    print("=" * 30)
    print("Available terms: " + ", ".join(ML_GLOSSARY.keys()))
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nEnter a term to look up: ").lower()

        if user_input == 'exit':
            print("Thank you for using the ML Glossary. Goodbye!")
            break

        definition = ML_GLOSSARY.get(user_input, "Sorry, that term was not found. Please try another.")

        print(f"\n---> {user_input.capitalize()}: {definition}")

if __name__ == "__main__":
    main()
