import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        distance_name = QLabel("Distance:")
        self.distance_field = QLineEdit()

        time_name = QLabel("Time(hours):")
        self.time_field = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.drop_down_menu = QComboBox()
        self.drop_down_menu.addItems(['Metric (km)', 'Metric (mi)'])

        self.show_field = QLabel("Calculate speed")

        grid.addWidget(distance_name, 0, 0)
        grid.addWidget(self.distance_field, 0, 1)
        grid.addWidget(self.drop_down_menu, 0, 2)
        grid.addWidget(time_name, 1, 0)
        grid.addWidget(self.time_field, 1, 1)
        grid.addWidget(calculate_button, 2, 0)
        grid.addWidget(self.show_field, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = self.distance_field.text()
        time = self.time_field.text()
        distance = int(distance)
        time = int(time)

        if self.drop_down_menu.currentText() == 'Metric (km)':
            self.show_field.setText(f"The speed is {distance / time} km/h")
        if self.drop_down_menu.currentText() == 'Metric (mi)':
            self.show_field.setText(f"The speed is {round((distance / time) / 1.6093440, 3)} mi/h")


app = QApplication(sys.argv)
average_preed_calculator = SpeedCalculator()
average_preed_calculator.show()
sys.exit(app.exec())
