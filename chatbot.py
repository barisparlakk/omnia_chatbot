class Chatbot:
    def __init__(self, Omnia):
        self.name = Omnia

    def get_input(self):
        user_input = input(" Hello, How can I help you today? ")
        return user_input

    def generate_response(self, user_input):
        if "Hi" in user_input.lower():
            return ("Hi, how can I help you today?")
        elif "how are you" in user_input.lower():
            return "I do not have any emotions because im just a pile of code. How can I help you today?"
        else:
            return "Sorry, I can't help you for this."

    def run(self):
        while True:
            user_input = self.get_input()
            if user_input.lower im ["quit","exit"]:
                print("See you later.")
                break
            response = self.generate_response(user_input)
            print(response)

