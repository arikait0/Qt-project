import sys
import os
import pickle
import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc


class MainWindow(Qw.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('project')
    self.setGeometry(100, 50, 640, 440)
    # カレンダー
    calendar = Qw.QCalendarWidget(self)
    calendar.setGridVisible(True)
    calendar.setGeometry(0, 0, 200, 200)
    calendar.move(20, 35)
    calendar.clicked[Qc.QDate].connect(self.showDate)
    self.label = Qw.QLabel(self)
    cal_date = calendar.selectedDate()
    self.label.setText(cal_date.toString())
    self.label.move(130, 5)
    # メモ欄
    self.Tbox = Qw.QLineEdit(self)
    self.Tbox.setGeometry(230, 35, 100, 200)
    self.Tbox.setPlaceholderText('メモ記入欄')
    self.Tbox.setAlignment(Qc.Qt.AlignmentFlag.AlignCenter)
    # 保存ボタン
    self.btn_run = Qw.QPushButton('メモを保存', self)
    self.btn_run.setGeometry(10, 10, 100, 20)
    self.btn_run.clicked.connect(self.btn_run_clicked)
    # メモの本体
    self.tb_memo = Qw.QTextEdit('', self)
    self.tb_memo.setGeometry(340, 35, 250, 200)
    self.tb_memo.setReadOnly(True)
    self.tb_memo.setPlaceholderText('(メモを保存してください)')

    # データの読み込み
    self.data_file = 'main.dat'
    if os.path.isfile(self.data_file):
      with open(self.data_file, 'rb') as file:
        data = pickle.load(file)
        self.tb_memo.setPlainText(data['memo'])
    else:
      pass

  def closeEvent(self, event):
    with open(self.data_file, 'wb') as file:
      data = {}
      data['memo'] = str(self.tb_memo)
      pickle.dump(data, file)
      print('データファイルを更新セーブしました。')
    event.accept()

  def btn_run_clicked(self):
    memo_log = f'({self.label.text()})'
    memo_log += f'({self.Tbox.text()})\n'
    memo_log += self.tb_memo.toPlainText()
    self.tb_memo.setPlainText(memo_log)

  def showDate(self, cal_date):
    self.label.setText(cal_date.toString())

if __name__ == '__main__':
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())
