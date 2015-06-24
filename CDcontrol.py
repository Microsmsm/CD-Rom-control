import ctypes
#forever looping
while (1 == 1):
    #G is ur CD drive letter
    ctypes.windll.WINMM.mciSendStringW(u"open G: type cdaudio alias d_drive", None, 0, None)
    #order it to open
    ctypes.windll.WINMM.mciSendStringW(u"set d_drive door open", None, 0, None)
    #order it to close
    ctypes.windll.WINMM.mciSendStringW(u"set d_drive door closed", None, 0, None)
