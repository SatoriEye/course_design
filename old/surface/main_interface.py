

def load_timeline():
    timeline = TimeLineSurface
    timeline.exec()

class MainWindowSurface(QWidget):
    def __init__(self):
        super(MainWindowSurface, self).__init__()
        self.initUI()



    def initUI(self):
        #界面
        self.win = QMainWindow()
        self.win.setGeometry(200, 200, 1000, 800)
        self.win.setWindowTitle("欢迎使用2022世界杯犯规管理系统！")
        self.win.setObjectName("MainWindow")
        self.win.setStyleSheet("#MainWindow{border-image:url(../icons/background.png);}")

        # 使用说明
        self.label = QLabel(self.win)
        self.label.resize(400, 200)
        self.label.setText(
            "\n使用说明: 本产品可用于\n2022VIVA世界杯数据的可视化查看, \n以及新的赛事数据添加。\n触碰下面的按钮开始操作")
        self.label.setFont(QFont("微软雅黑", 15, QFont.Bold))
        self.label.setStyleSheet("color:darkblue")
        self.label.move(50, 100)

        # 标题图片
        self.title_img = QLabel(self.win)
        self.title_img.resize(900, 100)
        self.title_img.setPixmap(QPixmap('../icons/title.png'))
        self.title_img.move(120, 30)

        # 事件一: 2022VIVA世界杯速览
        self.viva_button = QPushButton(self.win)
        self.viva_button.resize(300, 100)
        self.viva_button.move(100, 350)
        self.viva_button.setText("2022VIVA世界杯速览")

        # 事件二: 调整比赛时间轴
        self.timeline_button = QPushButton(self.win)
        self.timeline_button.resize(300, 100)
        self.timeline_button.move(100, 500)
        self.timeline_button.setText("调整比赛时间轴")
        self.timeline_button.clicked.connect(load_timeline)
        self.win.show()



app = QApplication(sys.argv)
mainsurface = MainWindowSurface()
mainsurface.show()
sys.exit(app.exec_())


