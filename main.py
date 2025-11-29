from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from playwright-demo!")


if __name__ == "__main__":
    main()
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Google API Key: {api_key}")
