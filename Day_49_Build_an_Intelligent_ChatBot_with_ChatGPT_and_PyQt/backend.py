import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            tempereture=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    print(chatbot.get_response("What is your name?"))


