import sys
import threading
 

from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import dash
import dash_core_components as dcc
import dash_html_components as html
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__()
        self.args = args
        self.kwargs = kwargs

    @Slot()  # QtCore.Slot
    def run(self):
        data = [
     
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        ]
        layout = {
           'title': 'Dash Data Visualization'
        }
        app = dash.Dash()
        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),
            html.Div(children='''
                Dash: A web application framework for Python.
            '''),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': data,
                    'layout': layout
                })
            ])
        app.run_server(debug=False, port=8015, host='127.0.0.1')
    
    def terminate():
        sys.exit()

class MainWindow(QtWidgets.QMainWindow):
     def __init__(self,parent = None):
        super().__init__(parent)
        self.mainWidget= MainWidget()
        self.setCentralWidget(self.mainWidget)
    
    
class MainWidget(QWidget):
    
    def __init__(self,parent = None):
        super().__init__(parent)
        self.threadpool = QThreadPool()
        worker = Worker() # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker) 
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:8015/"))
        # self.setCentralWidget(self.browser)
        self.btn = QPushButton('Button', self)
        self.btn.resize(self.btn.sizeHint())
        self.edit = QLineEdit("Write my name here")
        # self.button = QPushButton("Show Greetings")
        # # Create layout and add widgets
        # layout = QVBoxLayout()
        # layout.addWidget(self.browser)
        
        lay = QVBoxLayout(self)
        lay.addWidget(self.btn)
        lay.addWidget(self.browser)
        lay.addWidget(self.edit)
        
        #self.layout2.addWidget(self.browser)
        # # Set dialog layout
        # self.setLayout(layout)
        # # Add button signal to greetings slot
        self.btn.clicked.connect(self.greetings)

        def closeEvent(self, event):
            # do stuff
            if can_exit:
                worker.terminate()
                event.accept() # let the window close
                sys.exit()
            else:
                event.ignore()
        

    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())
        self.show()

if __name__ == '__main__':

    #threading.Thread(target=run_dash, args=(data, layout), daemon=True).start()
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    app.exec_()
