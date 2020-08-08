import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *

write_list = ['write1', 'write2', 'write3', 'write4']

pools_list = ['None', 'Nuke']

submit_in_list = ['Linux', 'Windows']

frame_per_task_list = ['2', '4', '8', '10', '12', '16']


class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        self.master_layout = QVBoxLayout()
        self.hori_lay_buttons = QHBoxLayout()

        grid = QGridLayout()

        self.button1 = QPushButton('ok')
        self.button2 = QPushButton('cancel')
        self.job_paused = QCheckBox('Submit_Paused')
        self.job_paused.setStyleSheet("color: blue")

        self.pool = QComboBox()
        self.pool.addItems(pools_list)
        self.pool.setCurrentIndex(1)

        self.label_for_pool = QLabel('Pool')

        self.label_for_submitin = QLabel('Submit_In')
        self.submit_in = QComboBox()
        self.submit_in.addItems(submit_in_list)

        self.label_for_framepertask = QLabel('Frame_Per_Task')
        self.frames_per_task = QComboBox()
        self.frames_per_task.addItems(frame_per_task_list)

        for node in write_list:
            self.select_writenodes(node)


        grid.addWidget(self.job_paused,0,0)
        grid.addWidget(self.label_for_pool,1,0)
        grid.addWidget(self.pool,1,1)
        grid.addWidget(self.label_for_framepertask, 2, 0)
        grid.addWidget(self.frames_per_task, 2, 1)
        grid.addWidget(self.label_for_submitin, 3, 0)
        grid.addWidget(self.submit_in, 3, 1)
        grid.setColumnStretch(1,1)

        # setting ok and cancel
        self.hori_lay_buttons.addWidget(self.button1)
        self.hori_lay_buttons.addWidget(self.button2)


        self.master_layout.addLayout(grid)
        self.master_layout.addLayout(self.hori_lay_buttons)

        self.setLayout(self.master_layout)
        self.setWindowTitle('CGRU_RENDER')

    def select_writenodes(self, write_name):
        check_box = QCheckBox(write_name)
        line_edit = QTextEdit()
        label_edit = QLabel('Frame_Range')
        label_edit.setStyleSheet("color: orange")
        line_edit.setMaximumHeight(25)

        lay_h = QHBoxLayout()
        lay_h.addWidget(label_edit)
        lay_h.addWidget(line_edit)

        layout_vertical_write = QVBoxLayout()
        layout_vertical_write.addWidget(check_box)
        layout_vertical_write.addLayout(lay_h)

        self.master_layout.addLayout(layout_vertical_write)


app = QApplication(sys.argv)
panel = Panel()
panel.show()
sys.exit(app.exec_())