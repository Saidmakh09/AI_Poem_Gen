from anthropic import Anthropic
from dotenv import load_dotenv


def get_temperature():
    while True:
        try:
            result = int(input("How random would you like your poem? 1-10: "))
            temp = result / 10
            if 0.0 <= temp <= 1.0:
                return temp
            print("Temperature out of range")
        except ValueError:
            print("Enter number between 0.0 and 1.0")
            #the get_temp function keep looping until it receives a value between the range
            #handles error gracefully, if an int or float isn't received, prompts to except ValueError
def get_maxtoken():
    token = int(input("How many words would you like your poem to have? limit 1000 (pls)"))
    if (token < 1000):
        print("Too many words")
    return token


load_dotenv()
#creates an API client instance to interact with Claude
client = Anthropic()
#loads from the API key from the .env file


def main():
    print("Hello this is an AI, that helps you write poems")
    user_input = input("What would you like you poem to be about? ")
    temp = get_temperature()
    tokens = get_maxtoken()

    if user_input:
        print("Ok loading in now...")
        response = client.messages.create(
            #
            model="claude-3-sonnet-20240229",
            max_tokens=tokens,
            temperature=temp,
            messages=[
                {"role": "user", "content": f"I would like my poem to be about {user_input}?"},
                {"role": "assistant", "content": "Here is a poem about it"}

            ]
        )
        print(response.content[0].text)
        #response.content returns list of content chunks
        #[0] get the first chunk
        #.text extract the actual text content
    else:
        print("no answer provided")


if __name__ == "__main__":
    main()