# _*_ codiong: utf-8 -*-

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):

    resolution = 0

    def __int__(self, width, height):
        self._width = width
        self._height = height

    def getwidth(self):
        return self._width

    def getheight(self):
        return self._height

    def setwidth(self, value):
        self._width = value

    def setheight(self, value):
        self._height = value

    def setresolution(self):
        return self._height*self._widht

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value


    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

    pass


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')