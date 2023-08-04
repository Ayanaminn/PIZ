import PIZ_GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem,QWidget,QMessageBox
from PyQt5.QtGui import QColor,QBrush
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QObject, QMutex, QMutexLocker,QTimer
import time
import serial
import serial.tools.list_ports

class MainWindow(QtWidgets.QMainWindow, PIZ_GUI.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.available_ports = []
        self.active_device = None
        self.init_port()
        self.port_comboBox.currentIndexChanged.connect(self.select_port)
        self.port_refresh_button.clicked.connect(self.refresh_port)
        self.port_connect_button.clicked.connect(self.connect_port)
        self.port_disconnect_button.clicked.connect(self.disconnect_port)

        self.state_a.addItems(['ON', 'OFF'])
        self.state_b.addItems(['ON', 'OFF'])

        self.rule_index = 0 # first rule index is 1
        self.rule_list = []

        self.add_rule_button.clicked.connect(self.add_rule)

        heads = ['Step','Channel A','Time(s)', 'Channel B', 'Time(s)']
        self.treeWidget.setHeaderLabels(heads)
        self.treeWidget.setAlternatingRowColors(True)

        self.apply_setting_button.clicked.connect(self.apply_setting)
        self.reset_rule_button.clicked.connect(self.reset)

        self.light_A.setStyleSheet('background-color:white')
        self.light_B.setStyleSheet('background-color:white')
        self.light_loop.setStyleSheet('background-color:white')

        self.light_thread = LightThread()
        self.light_thread.signals.on.connect(self.light_on)
        self.light_thread.signals.off.connect(self.light_off)
        self.light_thread.signals.finish.connect(self.loop_finish)

        self.light_thread_b = LightThreadB()
        self.light_thread_b.signals.b_on.connect(self.light_b_on)
        self.light_thread_b.signals.b_off.connect(self.light_b_off)
        self.light_thread_b.signals.b_finish.connect(self.loop_b_finish)

        self.start_button.clicked.connect(self.start)

    def get_all_items(self):
        i = 0
        item_num = self.treeWidget.topLevelItemCount()
        while i<item_num:
            all_items = self.treeWidget.topLevelItem(i)
            i+=1
            print(all_items)

    def init_port(self):

        self.port_comboBox.addItem('')
        ports = serial.tools.list_ports.comports()

        for p in ports:
            self.available_ports.append([p.description, p.device])
            # print(str(p.description)) # device name + port name
            # print(str(p.device)) # port name

        for info in self.available_ports:
            self.port_comboBox.addItem(info[0])

        print(self.available_ports)

    def select_port(self):
        # 1st empty line
        selected_port_index = self.port_comboBox.currentIndex() -1

        return selected_port_index

    def refresh_port(self):
        self.available_ports.clear()
        self.port_comboBox.clear()
        self.port_comboBox.addItem('')
        ports = serial.tools.list_ports.comports()

        for p in ports:
            self.available_ports.append([p.description, p.device])
            # print(str(p.description)) # device name + port name
            # print(str(p.device)) # port name

        for info in self.available_ports:
            self.port_comboBox.addItem(info[0])

        print(self.available_ports)

    def connect_port(self):

        selected_port_index = self.select_port()
        print(f'selected port index is {selected_port_index}')

        if self.available_ports and selected_port_index != -1:
            try:
                # portOpen = True
                self.active_device = serial.Serial(self.available_ports[selected_port_index][1], 9600, timeout=1)
                print(f'Connected to port {self.available_ports[selected_port_index][1]}!')
                # self.active_device.open()
                time.sleep(0.5)
                # turn off devices
                self.active_device.write(b'0')
                self.active_device.write(b'3')
                print(f'device is open : {self.active_device.isOpen()}')
                self.port_comboBox.setEnabled(False)
                self.port_connect_button.setEnabled(False)
                self.port_refresh_button.setEnabled(False)
                self.port_disconnect_button.setEnabled(True)
                self.add_rule_button.setEnabled(True)
                self.reset_rule_button.setEnabled(True)
                self.apply_setting_button.setEnabled(True)
                # print(f'Connected to port {available_ports[selected_port_index][1]}!')
                # device_control(activeDevice)
            except Exception as e:
                error = str(e)
                self.error_msg = QMessageBox()
                self.error_msg.setWindowTitle('Error')
                self.error_msg.setText('Cannot connect to selected port.')
                self.error_msg.setInformativeText('Please select a valid port')
                self.error_msg.setIcon(QMessageBox.Warning)
                self.error_msg.setDetailedText(error)
                self.error_msg.exec()
                self.refresh_port()

        elif not self.available_ports:
            self.error_msg = QMessageBox()
            self.error_msg.setWindowTitle('Error')
            self.error_msg.setText('Cannot read available port.')
            self.error_msg.setInformativeText('Please try reload port.')
            self.error_msg.setIcon(QMessageBox.Warning)
            self.error_msg.exec()
            self.refresh_port()

        elif selected_port_index == -1:
            self.error_msg = QMessageBox()
            self.error_msg.setWindowTitle('Error')
            self.error_msg.setText('Please select a valid port.')
            self.error_msg.setInformativeText('selected_port_index is empty.')
            self.error_msg.setIcon(QMessageBox.Warning)
            self.error_msg.exec()
            self.refresh_port()

    def disconnect_port(self):
        try:
            # turn off devices
            self.active_device.write(b'0')
            self.active_device.write(b'3')
            self.active_device.close()

        except Exception as e:
            error = str(e)
            self.error_msg = QMessageBox()
            self.error_msg.setWindowTitle('Error')
            self.error_msg.setText('Cannot disconnect from selected port.')
            self.error_msg.setInformativeText('disconnect_port() failed.')
            self.error_msg.setIcon(QMessageBox.Warning)
            self.error_msg.setDetailedText(error)
            self.error_msg.exec()

        if not self.active_device.isOpen():
            print('Connection with port closed')
            print(f'device is open : {self.active_device.isOpen()}')

            self.port_comboBox.setEnabled(True)
            self.port_connect_button.setEnabled(True)
            self.port_disconnect_button.setEnabled(False)
            self.refresh_port()

    def add_rule(self):
        # create a rule from current input and append to rule list
        self.rule_index += 1
        state_a = self.state_a.currentText()
        time_a = self.time_a.value()
        state_b = self.state_b.currentText()
        time_b = self.time_b.value()

        new_rule = Rules(self.rule_index, state_a,time_a,state_b,time_b)

        current_rule_text = []
        for attr, value in new_rule.__dict__.items():
            current_rule_text.append(str(value))

        current_rule_display = QTreeWidgetItem(self.treeWidget, current_rule_text)
        self.treeWidget.addTopLevelItem(current_rule_display)

        self.rule_list.append(new_rule)

    def apply_setting(self):
        self.start_button.setEnabled(True)

        step_time_a = []
        step_state_a = []
        step_time_b = []
        step_state_b = []

        for i in self.rule_list:
            step_time_a.append(i.time_a * 1000) # seconds to milliseconds
            step_time_b.append(i.time_b * 1000)  # seconds to milliseconds
        print(f'step time is {step_time_a}')
        print(f'step time b is {step_time_b}')
        self.light_thread.step_time = step_time_a
        self.light_thread_b.step_time = step_time_b

        for i in self.rule_list:
            if i.state_a == 'ON':
                step_state_a.append(1)
            elif i.state_a == 'OFF':
                step_state_a.append(0)
        print(f'condition list is {step_state_a}')
        self.light_thread.step_state = step_state_a

        for i in self.rule_list:
            if i.state_b == 'ON':
                step_state_b.append(1)
            elif i.state_b == 'OFF':
                step_state_b.append(0)
        print(f'condition list b is {step_state_b}')
        self.light_thread_b.step_state = step_state_b

        self.light_thread.total_steps = self.rule_list[-1].rule_index
        self.light_thread_b.total_steps = self.rule_list[-1].rule_index
        print(f'total steps passed to thread is {self.light_thread.total_steps}')
        print(f'total steps passed to thread b is {self.light_thread_b.total_steps}')

        self.light_thread.cycles = self.total_cycle.value()
        self.light_thread_b.cycles = self.total_cycle.value()

    def start(self):

        self.light_loop.setStyleSheet('background-color:green')
        self.light_thread.run()
        self.light_thread_b.run()

    def reset(self):
        self.rule_list.clear()
        self.rule_index = 0
        self.treeWidget.clear()
        self.start_button.setEnabled(False)

    def light_on(self):
        self.light_A.setStyleSheet('background-color:yellow')
        self.active_device.write(b'1')

    def light_off(self):
        self.light_A.setStyleSheet('background-color:black')
        self.active_device.write(b'0')

    def loop_finish(self):
        self.light_thread.stop()
        self.light_loop.setStyleSheet('background-color:red')

    def light_b_on(self):
        self.light_B.setStyleSheet('background-color:yellow')
        self.active_device.write(b'2')

    def light_b_off(self):
        self.light_B.setStyleSheet('background-color:black')
        self.active_device.write(b'3')

    def loop_b_finish(self):
        self.light_thread_b.stop()
        print('loop b finish')


class Rules(object):
    _registry = []

    def __init__(self, rule_index, state_a, time_a, state_b, time_b):

        self.rule_index = rule_index
        self.state_a = state_a
        self.time_a = time_a
        self.state_b = state_b
        self.time_b = time_b
        self._registry.append(self)


class Signals(QObject):
    on = pyqtSignal(str)
    off = pyqtSignal(str)
    finish = pyqtSignal(str)
    b_on = pyqtSignal(str)
    b_off = pyqtSignal(str)
    b_finish = pyqtSignal(str)


class LightThread(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.signals = Signals()
        self.mutex = QMutex()
        self.stopped = False

        self.step_timer = QTimer() # on/off time for each rule step
        self.current_step = 0 # init
        self.loop_counter = 0  # init
        self.total_steps = 0 # init total
        self.step_time = []
        self.step_state = [] # 0:off, 1: on
        self.cycles = 0

        # self.on_timer = QTimer()
        # self.off_timer = QTimer()
        # self.state = 0
        # self.on_time = 5000 # milliseconds
        # self.off_time = 0
        # self.on_timer.setSingleShot(True)
        # self.on_timer.setInterval(self.on_time)
        # self.on_timer.timeout.connect(self.update_loop)
        # self.off_timer.setSingleShot(True)
        # self.off_timer.setInterval(self.off_time)
        # self.off_timer.timeout.connect(self.update_loop)
        self.step_timer.setSingleShot(True)
        self.step_timer.timeout.connect(self.update_loop)

    def run(self):
        with QMutexLocker(self.mutex):
            self.stopped = False
        try:
            self.update_loop()
        except Exception as e:
            print(e)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped = True

    # def update_light(self):
    #
    #     self.state = 1 - self.state
    #     if self.state == 1:
    #         self.signals.on.emit('1')
    #         self.on_timer.start()
    #     else:
    #         self.signals.off.emit('1')
    #         self.off_timer.start()

    def update_steps(self):

        # within this loop
        if self.current_step < self.total_steps:
            print(f'for step {self.current_step} ')
            # get on/off time for current rule from rule list
            self.step_timer.setInterval(self.step_time[self.current_step])
            print(f'step time {self.step_time[self.current_step]}')
            print(f'step state {self.step_state[self.current_step]}')
            # if state for this step is on
            if self.step_state[self.current_step] == 1:
                self.signals.on.emit('1')
                print(' on emit')
                self.current_step +=1
            # if state for this step is off
            else:
                print(' off emit')
                self.signals.off.emit('1')
                self.current_step += 1
            self.step_timer.start()
        # go back to step 1 and re-execute all steps again
        else:
            self.current_step = 0
            self.loop_counter += 1
            self.update_loop()

    def update_loop(self):
        # if all cycle finsished
        print('update loop')
        if self.loop_counter >= self.cycles: # 2 loop make 1 full cycle
            self.signals.finish.emit('1')
            self.current_step = 0 # reset
        # execute steps within this loop
        else:
            self.update_steps()
        print(f' loop counter is {self.loop_counter}')


class LightThreadB(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.signals = Signals()
        self.mutex = QMutex()
        self.stopped = False

        self.step_timer = QTimer() # on/off time for each rule step
        self.current_step = 0 # init
        self.loop_counter = 0  # init
        self.total_steps = 0 # init total
        self.step_time = []
        self.step_state = [] # 0:off, 1: on
        self.cycles = 0

        self.step_timer.setSingleShot(True)
        self.step_timer.timeout.connect(self.update_loop)

    def run(self):
        with QMutexLocker(self.mutex):
            self.stopped = False
        try:
            print('thread b run')
            self.update_loop()

        except Exception as e:
            print(e)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped = True

    def update_steps(self):
        # within this loop
        if self.current_step < self.total_steps:
            print(f'for step {self.current_step}')
            # get on/off time for current rule from rule list
            self.step_timer.setInterval(self.step_time[self.current_step])
            print(f'step time b {self.step_time[self.current_step]}')
            print(f'step state b {self.step_state[self.current_step]}')
            # if state for this step is on
            if self.step_state[self.current_step] == 1:
                self.signals.b_on.emit('1')
                print(' on emit')
                self.current_step +=1
            # if state for this step is off
            else:
                print(' off emit')
                self.signals.b_off.emit('1')
                self.current_step += 1
            self.step_timer.start()
        # go back to step 1 and re-execute all steps again
        else:
            self.current_step = 0
            self.loop_counter += 1
            self.update_loop()

    def update_loop(self):
        # if all cycle finsished
        print('update loop b')
        if self.loop_counter >= self.cycles:  # 2 loop make 1 full cycle
            self.signals.b_finish.emit('1')
            self.current_step = 0  # reset
        # execute steps within this loop
        else:
            self.update_steps()
        print(f' loop counter b is {self.loop_counter}')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())