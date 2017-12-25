# wxPython eval

import wx
import wx.grid as gridlib

class EveLpApp(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(EveLpApp, self).__init__(*args, **kwargs)

        self.InitUi()
        self.FillTable()
        self.SetSize((1100, 580))
        self.SetTitle('EveLpApp')
        self.Centre()
        self.Show()

    def InitUi(self):

        #Make me a little grid you codeing bitch, thanks.
        LpPanel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(LpPanel)
        self.grid.CreateGrid(25,9)
        self.grid.EnableEditing(False)
        #Box layout
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(self.grid, 1, wx.EXPAND, 5)
        LpPanel.SetSizer(Sizer)
        #Column config
        self.grid.SetColMinimalAcceptableWidth(110)
        self.grid.SetColLabelValue(0, 'Item Name')
        self.grid.SetColSize(0,110)
        self.grid.SetColLabelValue(1, 'Price [ISK]')
        self.grid.SetColFormatFloat(1, -1 , 2)
        self.grid.SetColSize(1,110)
        self.grid.SetColLabelValue(2, 'LP Cost [EA]')
        self.grid.SetColFormatNumber(2)
        self.grid.SetColSize(2,110)
        self.grid.SetColLabelValue(3, 'Mineral Cost [ISK]')
        self.grid.SetColFormatFloat(3, -1 , 2)
        self.grid.SetColSize(3,110)
        self.grid.SetColLabelValue(4, 'Total Cost [ISK]')
        self.grid.SetColFormatFloat(4, -1 , 2)
        self.grid.SetColSize(4,110)
        self.grid.SetColLabelValue(5, 'Sell Price Jita [ISK]')
        self.grid.SetColFormatFloat(5, -1 , 2)
        self.grid.SetColSize(5,110)
        self.grid.SetColLabelValue(6, 'Profit [ISK]')
        self.grid.SetColFormatFloat(6, -1 , 2)
        self.grid.SetColSize(6,110)
        self.grid.SetColLabelValue(7, 'Profit [%]')
        self.grid.SetColFormatFloat(7, -1 , 2)
        self.grid.SetColSize(7,110)
        self.grid.SetColLabelValue(8, 'Efficiency [ISK/LP]')
        self.grid.SetColFormatFloat(8, -1 , 2)
        self.grid.SetColSize(8,110)

        #Create a menu bar
        MenuBar = wx.MenuBar()

        #Create the file menu in the menu bar
        FileMenu = wx.Menu()
        FileMenu.Append(wx.ID_NEW, '&New')
        FileMenu.Append(wx.ID_DELETE, '&Delete')
        FileMenu.Append(wx.ID_ANY, '&Update\tAlt+F5')
        FileMenu.AppendSeparator()
        Qmi = wx.MenuItem(FileMenu, wx.ID_EXIT, '&Quit\tAlt+F4')
        #Qmi.SetBitmap(wx.Bitmap('exit.png'))
        FileMenu.Append(Qmi)

        #Create the help menu in the bar
        HelpMenu = wx.Menu()
        HelpMenu.Append(wx.ID_ABOUT, '&About\tF1')

        #Bound functions in the menu bar
        self.Bind(wx.EVT_MENU, self.OnQuit, Qmi)

        #Append the menus to the bar
        MenuBar.Append(FileMenu, '&File')
        MenuBar.Append(HelpMenu, '&Help')
        self.SetMenuBar(MenuBar)

    #Method for filling the table with data
    def FillTable(self):
        GridFill = ('Astero', 15000000.00, 30000, 387669.41, 15387669.41, 62300000.00, 46912330.59, 404.87 , 1563.74)
        for i in range(0,len(GridFill),1):
            Value = str(GridFill[i])
            self.grid.SetCellValue(0,i,Value)

    #Method to close the instance
    def OnQuit(self, e):
        self.Close()

def Main():
    app = wx.App()
    x = EveLpApp(None, title='EveLpApp')
    #x.grid.SetCellValue(1,0,'FUCK')
    app.MainLoop() 

    #print(x.grid)

if __name__ == '__main__':
    Main()

    