import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication

from Day_49_Build_an_Intelligent_ChatBot_with_ChatGPT_and_PyQt.backend import Chatbot
import threading


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add send button widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        message = self.input_field.text()
        self.chat_area.append(f"<p style = 'color:#333333;'>Me: {message}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(message,))
        thread.start()

    def get_bot_response(self, message):
        response = self.chatbot.get_response(message)
        self.chat_area.append(f"<p style = 'color:#666666;'>Bot: {response}</p>")



app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
