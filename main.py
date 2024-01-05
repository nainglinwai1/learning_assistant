import openai

# Set your OpenAI API key
openai.api_key = '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'

def generate_definition(word):
    # OpenAI GPT-3 prompt to generate a definition for a given word
    prompt = f"Define the word '{word}'."
    
    # Make an API call to OpenAI GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=100  # Adjust the length of the generated response
    )
    
    # Extract the generated text from the OpenAI GPT-3 response
    generated_text = response.choices[0].text.strip()
    
    return generated_text

def main():
    # Get a word from the user
    word = input("Enter a word you want to learn: ")
    
    # Generate the definition using OpenAI GPT-3
    definition = generate_definition(word)
    
    # Display the result
    print(f"\nDefinition of '{word}': {definition}")

if __name__ == "__main__":
    main()
