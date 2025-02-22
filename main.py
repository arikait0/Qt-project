import side

if __name__ == '__main__':
  app = side.Qw.QApplication(side.sys.argv)
  main_window = side.MainWindow()
  main_window.show()
  side.sys.exit(app.exec())
