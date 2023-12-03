# from openai import OpenAI
# api_key = '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'
# client = OpenAI(api_key=api_key)

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "explain oops in C++"},
#     {"role": "user", "content": ""}
#   ]
# )

# print(completion.choices[0].message)
# response = client.images.generate(
#   prompt="A spider man on the top of building driking water",
#   n=2,
#   size="1024x1024"
# )

# print(response)

import tkinter as tk
from tkinter import scrolledtext
import openai

openai.api_key = "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"  # Replace with your actual API key

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("CodeGPT- Your Coding Assistant")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Entry(master, width=30)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def send_message(self):
        user_input = self.user_input.get()
        self.update_chat_history(f"You: {user_input}\n")

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are going to Assist in software development by providing code snippets or suggesting solutions for a given programming problem. & Identify and explain errors in provided code, offering clear explanations and potential fixes.Offer guidance on best practices, coding conventions, and optimization techniques to improve overall code quality."},
                {"role": "user", "content": user_input}
            ]
        )

        response = completion['choices'][0]['message']['content']
        self.update_chat_history(f"ChatGPT: {response}\n")

        # Clear the user input
        self.user_input.delete(0, tk.END)

    def update_chat_history(self, message):
        self.chat_history.insert(tk.END, message)
        self.chat_history.yview(tk.END)  # Auto-scroll to the bottom

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
