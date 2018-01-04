# Popup window to insert a new item into the evedata database

import wx
import mysql.connector


class NewItem(wx.Frame):
    """Popup for the new item dialog"""
    def __init__(self, *args, **kwargs):
        super(NewItem, self).__init__(*args, **kwargs)

        self.SetSize((600, 300))
        self.SetTitle('New Item')

        self.init()

    def init(self):
        new_panel = wx.Panel(self, wx.ID_ANY)

        top_p = wx.Panel(new_panel, wx.ID_ANY)
        middle_p = wx.Panel(new_panel, wx.ID_ANY)
        bottom_p = wx.Panel(new_panel, wx.ID_ANY)

        # Box layout
        #g_sizer = wx.GridSizer(rows=2, cols=2, hgap=5, vgap=5)

        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        v_sizer = wx.BoxSizer(wx.VERTICAL)

        new_panel.SetSizer(h_sizer)

        self.insert_b = wx.Button(new_panel, -1, "Insert")
        self.query_uid_b = wx.Button(new_panel, -1, "Get UID")
        self.close_b = wx.Button(new_panel, -1, "Close")

        h_sizer.Add(self.insert_b, 0)
        h_sizer.Add(self.close_b, 0)



        # g_sizer.Add()
        # g_sizer.Add(self.insert_b, 0)
        # g_sizer.Add(self.close_b, 0)

        self.Center()
        self.Show(True)


app = wx.App(False)
frame = NewItem(None, title='New Item')
app.MainLoop()
