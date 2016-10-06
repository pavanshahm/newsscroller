import win32api, win32con, win32gui, win32ui

class displayStream(object):
    """produces banner of all the information over the windows screen"""


    def __init__(self):
        self.hInstance = win32api.GetModuleHandle()
        self.className = 'MyWindowClassName'

        self.wndClass                = win32gui.WNDCLASS()
        self.wndClass.style          = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        self.wndClass.lpfnWndProc    = wndProc
        self.wndClass.hInstance      = self.hInstance
        self.wndClass.hCursor        = win32gui.LoadCursor(None, win32con.IDC_ARROW)
        self.wndClass.hbrBackground  = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        self.wndClass.lpszClassName  = self.className
        # win32gui does not support RegisterClassEx
        self.wndClassAtom = win32gui.RegisterClass(self.wndClass)

        self.exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
        self.style = win32con.WS_DISABLED | win32con.WS_POPUP | win32con.WS_VISIBLE
        self.hWindow = win32gui.CreateWindowEx(
            self.exStyle,
            self.wndClassAtom,
            None, # WindowName
            self.style,
            0, # x
            0, # y
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN), # width
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN), # height
            None, # hWndParent
            None, # hMenu
            self.hInstance,
            None # lpParam
        )

        win32gui.SetLayeredWindowAttributes(self.hWindow, 0x00ffffff, 255, win32con.LWA_COLORKEY | win32con.LWA_ALPHA)
        win32gui.SetWindowPos(self.hWindow, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        win32gui.PumpMessages()


def wndProc(hWnd, message, wParam, lParam):
    if message == win32con.WM_PAINT:
        hdc, paintStruct = win32gui.BeginPaint(hWnd)

        dpiScale = win32ui.GetDeviceCaps(hdc, win32con.LOGPIXELSX) / 60.0
        fontSize = 80

        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
        lf = win32gui.LOGFONT()
        lf.lfFaceName = "Times New Roman"
        lf.lfHeight = int(round(dpiScale * fontSize))
        #lf.lfWeight = 150
        # Use nonantialiased to remove the white edges around the text.
        # lf.lfQuality = win32con.NONANTIALIASED_QUALITY
        hf = win32gui.CreateFontIndirect(lf)
        win32gui.SelectObject(hdc, hf)

        rect = win32gui.GetClientRect(hWnd)
        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd162498(v=vs.85).aspx
        win32gui.DrawText(
            hdc,
            'Text on the screen',
            -1,
            rect,
            win32con.DT_CENTER | win32con.DT_NOCLIP | win32con.DT_SINGLELINE | win32con.DT_VCENTER
        )
        win32gui.EndPaint(hWnd, paintStruct)
        return 0

    elif message == win32con.WM_DESTROY:
        print('Closing the window.')
        win32gui.PostQuitMessage(0)
        return 0

    else:
        return win32gui.DefWindowProc(hWnd, message, wParam, lParam)