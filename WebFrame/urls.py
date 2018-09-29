#所有可以被访问的URL列表

from views import*

url = [
    ('/time',show_time),
    ('/hello',say_hello),
    ('/bye',say_bye)
]