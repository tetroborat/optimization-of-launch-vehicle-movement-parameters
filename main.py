import sys,desi,lag  # sys нужен для передачи argv в QApplication
from PyQt5.QtWidgets import QWidget,QApplication



class App(QWidget, desi.Ui_MainWindow):
    def ras(self):
        desi.clear(self)
        lag.rass(self)
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.commandLinkButton.clicked.connect(self.ras)
def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()








