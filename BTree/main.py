import wx
import MainFrame as mf

class wxStegGraf(wx.App):
    def OnInit(self):
        self.frame = mf.wxMainFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    wxStegGraf = wxStegGraf()
    wxStegGraf.MainLoop()