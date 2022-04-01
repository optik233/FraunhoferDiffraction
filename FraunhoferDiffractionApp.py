from PyQt5.QtWidgets import QApplication, QMainWindow
# QApplication 包含窗口系统和其他来源处理过和发送过的主事件循环，也处理应用程序初始化和收尾。管理对话
# QMainWindow  QMainWindow()可以创建一个应用程序的窗口。MainWindow的结构分为五个部分：菜单栏（Menu Bar）工具栏（Toolbars）、
# 停靠窗口（Dock Widgets）、状态栏（Status Bar）和中央窗口（Central Widget） 中央窗口可以使用任何形式的widget来填充
# 总结来说 QApplication 是控制模块，负责载入QT架构；； QMainWindow 是显示模块，负责把自己的UI显示出来
from PyQt5.QtCore import pyqtSlot  # 槽函数命令
from QtUI import Ui_MainWindow  # 把QT创建的UI界面导进来
from numpy import pi, linspace, meshgrid, sin
import matplotlib.cm as cm

# 创建我自己的UI类，继承于QT自创的Ui_MainWindow
class FraunhoferDiffractionApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  # 主窗口初始化在自己的APP窗口上
        self.setupUi(self)  # QT生成的setupUI的函数，是UI_MainWindow里面的方法 在刚生成的主窗口上面进行我们的初始化
        self.fig1() # 建立一个图像

    def fig1(self):
        lamda = self.Slider_lambda.value() * 1e-9
        k = (2 * pi) / lamda
        b = self.Slider_b.value() * 1e-5
        h = self.Slider_h.value() * 1e-5
        f2 = self.Slider_f2.value()
        a = self.Slider_a.value() * 1e-2
        X_Mmax = a / 2
        X_Mmin = -a / 2
        Y_Mmax = X_Mmax
        Y_Mmin = -X_Mmin
        N = 400
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X
        B = (k * b * X) / (2 * f2)
        H = (k * h * Y) / (2 * f2)
        BB, HH = meshgrid(B, H)
        I = ((sin(BB) / BB) ** 2) * ((sin(HH) / HH) ** 2)
        mpl = self.mplwidget.canvas # 在小部件的画布上作图，创建一个小部件对象 部件名称self.mplwidget
        mpl.ax.clear()
        mpl.ax.imshow(I, cmap=cm.gray, interpolation='bilinear', origin='lower', vmin=0, vmax=0.01)
        mpl.ax.set_xlabel(u'$X(m)$', fontsize=12, fontweight='bold')
        mpl.ax.set_ylabel(u'$Y(m)$', fontsize=12, fontweight='bold')
        mpl.ax.set_xticks(linspace(0, N, 5))
        mpl.ax.set_xticklabels(linspace(X_Mmin, X_Mmax, 5), color='r')
        mpl.ax.set_yticks(linspace(0, N, 5))
        mpl.ax.set_yticklabels(linspace(Y_Mmin, Y_Mmax, 5), color='r')
        mpl.figure.suptitle('Fraunhofer Diffraction by rectangular aperture', fontsize=10, fontweight='bold')
        mpl.ax.set_title(r'$\lambda = %s, b = %s, h = %s, f2 = %s$' % (lamda, b, h, f2), fontsize=10)
        mpl.draw()

    @pyqtSlot('double')
    def on_SpinBox_lambda_valueChanged(self, value):
        self.Slider_lambda.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_b_valueChanged(self, value):
        self.Slider_b.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_h_valueChanged(self, value):
        self.Slider_h.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.Slider_a.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):
        self.Slider_f2.setValue(value)

    @pyqtSlot("int")
    def on_Slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_Slider_b_valueChanged(self, value):
        self.SpinBox_b.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_Slider_h_valueChanged(self, value):
        self.SpinBox_h.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_Slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_Slider_f2_valueChanged(self, value):
        self.SpinBox_f2.setValue(value)
        self.fig1()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    FraunhoferDiffraction = FraunhoferDiffractionApp()
    FraunhoferDiffraction.show()  # Show the form
    sys.exit(app.exec_())  # Execute the app
