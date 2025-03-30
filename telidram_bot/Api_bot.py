import os
import google.generativeai as genai

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyACd3jcYie92qktM_Gbc78O6ykgwJvPjNU")  # Replace with your API key or use environment variable
if not api_key:
    print("API Key for Google Gemini LLM is missing. Please set it in the .env file.")
else:
    genai.configure(api_key=api_key)

def get_gemini_response(question):
    try:
        # Use the generate_text method to generate a response
        response = genai.generate_text(
            model="text-bison-001",  # Use the appropriate model name
            prompt=f"Provide a structured response to the following question using headings, bullet points, and bold text. Avoid unnecessary symbols. Question: {question}"
        )
        # Extract and return the response text
        return response["candidates"][0]["output"] if response and "candidates" in response else "No response available."
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    question = "What are the symptoms of breast cancer?"
    answer = get_gemini_response(question)
    if answer:
        print("Gemini Response:")
        print(answer)
    else:
        print("Failed to get a response from Gemini.")