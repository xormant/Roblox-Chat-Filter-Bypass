import sys
import requests
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QFont, QGuiApplication, QPalette, QBrush, QColor, QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer, QTime

emoji_map = {
    'a': '🅰', 'b': '🅱', 'c': '🅲', 'd': '🅳', 'e': '🅴', 'f': '🅵', 'g': '🅶',
    'h': '🅷', 'i': '🅸', 'j': '🅹', 'k': '🅺', 'l': '🅻', 'm': '🅼', 'n': '🅽',
    'o': '🅾', 'p': '🅿', 'q': '🆀', 'r': '🆁', 's': '🆂', 't': '🆃', 'u': '🆄',
    'v': '🆅', 'w': '🆆', 'x': '🆇', 'y': '🆈', 'z': '🆉',
    '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣', '5': '5️⃣',
    '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣', ' ': '⬛'
}

def map_text_to_emoji(text):
    return ''.join(emoji_map.get(char.lower(), char) for char in text)

def retrieve_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = response.content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        return pixmap
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
        return None

class EmojiApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("[ Roblox Chat Filter Bypass ]")
        self.setGeometry(100, 100, 450, 200)

        image_url = "https://i.ibb.co/fqDxmBm/icon.png"
        icon_pixmap = retrieve_image_from_url(image_url)
        if icon_pixmap and not icon_pixmap.isNull():
            self.setWindowIcon(QIcon(icon_pixmap))
        else:
            print("Failed to load icon")

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QColor("#2c2f33")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.setStyleSheet("""
            background-color: #2c2f33; 
            color: white;
            border-radius: 15px;
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        self.spinner_label = QLabel("[ | ]", self)
        self.spinner_label.setFont(QFont("Arial", 12))
        self.spinner_label.setStyleSheet("color: white;")
        header_layout.addWidget(self.spinner_label)

        self.title_label = QLabel("FUD Chat Filter Bypass V2.0  (GUI Variant)", self)
        self.title_label.setFont(QFont("Arial", 14))
        self.title_label.setStyleSheet("color: white;")
        header_layout.addWidget(self.title_label)

        self.box_slider_label = QLabel("> ----- <", self)
        self.box_slider_label.setFont(QFont("Arial", 12))
        self.box_slider_label.setStyleSheet("color: white;")
        header_layout.addWidget(self.box_slider_label)

        header_layout.addStretch(1)
        header_layout.addStretch(1)

        main_layout.addLayout(header_layout)

        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setStyleSheet("""
            background-color: #23272a; 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            background-image: linear-gradient(45deg, #3e4247 25%, transparent 25%), 
                              linear-gradient(135deg, #3e4247 25%, transparent 25%);
            background-position: 10px 0, 0 0;
        """)
        self.input_field.textChanged.connect(self.update_text_output)
        main_layout.addWidget(self.input_field)

        self.output_label = QLabel(self)
        self.output_label.setFont(QFont("Arial", 14))
        self.output_label.setStyleSheet("""
            padding: 10px;
            color: white;
            background-color: #23272a;
            border-radius: 5px;
        """)
        main_layout.addWidget(self.output_label)
        button_layout = QHBoxLayout()

        self.copy_button = QPushButton("Copy", self)
        self.copy_button.setFont(QFont("Arial", 12))
        self.copy_button.setStyleSheet("""
            background-color: #1c1f24;
            color: white; 
            padding: 10px; 
            border: 1px solid white;
        """)
        self.copy_button.clicked.connect(self.copy_text_to_clipboard)
        button_layout.addWidget(self.copy_button)

        self.developer_label = QLabel("Developed by xormant", self)
        self.developer_label.setFont(QFont("Arial", 8))
        self.developer_label.setStyleSheet("""
            color: #99aab5;
            margin-top: 0px;
            margin-bottom: 0px;
            text-align: right;
        """)
        button_layout.addWidget(self.developer_label, alignment=Qt.AlignRight)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_animations)
        self.animation_timer.start(100)

        self.spinner_index = 0
        self.spinner_states = ["[ | ]", "[ / ]", "[ - ]", "[ \\ ]"]
        self.box_slider_pos = 0
        self.box_slider_dir = 1

    def update_text_output(self):
        input_text = self.input_field.text()
        emoji_text = map_text_to_emoji(input_text)
        self.output_label.setText(emoji_text)

    def copy_text_to_clipboard(self):
        emoji_text = self.output_label.text()
        if not emoji_text:
            QMessageBox.warning(self, "Warning", "There is no text to copy...")
        else:
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(emoji_text)

    def update_animations(self):
        self.spinner_label.setText(self.spinner_states[self.spinner_index])
        self.spinner_index = (self.spinner_index + 1) % len(self.spinner_states)

        slider_text = "> " + "-" * (self.box_slider_pos) + " " + "<"
        self.box_slider_label.setText(slider_text)
        self.box_slider_pos += self.box_slider_dir
        if self.box_slider_pos == 5 or self.box_slider_pos == 0:
            self.box_slider_dir *= -1

def main():
    app = QApplication(sys.argv)
    app_instance = EmojiApp()
    app_instance.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
