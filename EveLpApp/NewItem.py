#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b1 on Thu Jan  4 16:38:25 2018
#

import wx
import requests
import json


class NewItem(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: NewItem.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.item_name_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.item_uid_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.query_b = wx.Button(self, wx.ID_ANY, "Query  UID")
        self.tritanium_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.pyerite_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.mexallon_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.isogen_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.nocxium_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.zydrine_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.megacyte_t = wx.TextCtrl(self, wx.ID_ANY, "")
        self.insert_b = wx.Button(self, wx.ID_ANY, "Insert")
        self.close_b = wx.Button(self, wx.ID_ANY, "Close")
        self.__set_properties()
        self.__do_layout()
        self.set_bind()
        self.Centre()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("New Item")
        self.SetBackgroundColour(wx.Colour(159, 159, 95))
        self.query_b.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.query_b.SetForegroundColour(wx.Colour(255, 0, 0))
        self.query_b.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def set_bind(self):
        self.Bind(wx.EVT_BUTTON, self.on_quit, self.close_b)
        self.Bind(wx.EVT_BUTTON, self.item_uid, self.query_b)

    def item_uid(self, *args):
        """Gets the uid for the give item names, item_name is expected as list like: ['Tritanium']"""

        uid_url = 'https://www.fuzzwork.co.uk/api/typeid.php?typename='  # TypeID
        item_name = self.item_name_t.GetValue()

        final_url = uid_url + item_name
        page_request = requests.get(final_url)

        # Check if the HTML message is 200, has to be reworked for error handling
        if page_request.status_code != 200:
            print("!!An HTML error occurred!!")

        # Convert json to python list
        json_page_output = page_request.text
        www_item_uid = json.loads(json_page_output)
        # Comes as dict {'typeID': 0, 'typeName': 'bad item'} for bad input
        # and {'typeID': 34, 'typeName': 'Tritanium'} for a valid item

        self.item_uid_t.Clear()
        self.item_uid_t.WriteText(str(www_item_uid['typeID']))

    # End of item_uid method

    # Method to close the instance
    def on_quit(self, e):
        self.Close()
        # print('CLOSE')

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(0, 7, 5, 5)
        item_name = wx.StaticText(self, wx.ID_ANY, "Item Name")
        item_name.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        grid_sizer_1.Add(item_name, 0, 0)
        uid_l = wx.StaticText(self, wx.ID_ANY, "UID")
        uid_l.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        grid_sizer_1.Add(uid_l, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.item_name_t, 0, 0, 0)
        grid_sizer_1.Add(self.item_uid_t, 0, 0, 0)
        grid_sizer_1.Add(self.query_b, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        mineral_l = wx.StaticText(self, wx.ID_ANY, "Minerals")
        mineral_l.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        grid_sizer_1.Add(mineral_l, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        tritanium_l = wx.StaticText(self, wx.ID_ANY, "Tritanium")
        grid_sizer_1.Add(tritanium_l, 0, 0, 0)
        pyerite_l = wx.StaticText(self, wx.ID_ANY, "Pyerite")
        grid_sizer_1.Add(pyerite_l, 0, 0, 0)
        mexallon_l = wx.StaticText(self, wx.ID_ANY, "Mexallon")
        grid_sizer_1.Add(mexallon_l, 0, 0, 0)
        isogen_l = wx.StaticText(self, wx.ID_ANY, "Isogen")
        grid_sizer_1.Add(isogen_l, 0, 0, 0)
        nocxium_l = wx.StaticText(self, wx.ID_ANY, "Nocxium")
        grid_sizer_1.Add(nocxium_l, 0, 0, 0)
        zydrine_l = wx.StaticText(self, wx.ID_ANY, "Zydrine")
        grid_sizer_1.Add(zydrine_l, 0, 0, 0)
        megacyte_l = wx.StaticText(self, wx.ID_ANY, "Megacyte")
        grid_sizer_1.Add(megacyte_l, 0, 0, 0)
        grid_sizer_1.Add(self.tritanium_t, 0, 0, 0)
        grid_sizer_1.Add(self.pyerite_t, 0, 0, 0)
        grid_sizer_1.Add(self.mexallon_t, 0, 0, 0)
        grid_sizer_1.Add(self.isogen_t, 0, 0, 0)
        grid_sizer_1.Add(self.nocxium_t, 0, 0, 0)
        grid_sizer_1.Add(self.zydrine_t, 0, 0, 0)
        grid_sizer_1.Add(self.megacyte_t, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.insert_b, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.close_b, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        self.SetSize((830, 260))
        # end wxGlade

# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        self.new_item = NewItem(None, wx.ID_ANY, "")
        self.SetTopWindow(self.new_item)
        self.new_item.Show()
        return True

# end of class MyApp


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()