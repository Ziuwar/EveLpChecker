# wxPython eval

import wx
import wx.grid as gridlib
import mysql.connector
import NewItem


class EveLpApp(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(EveLpApp, self).__init__(*args, **kwargs)

        self.InitUi()
        self.fill_table()
        self.SetSize((1100, 580))
        self.SetTitle('EveLpApp')
        self.Centre()
        self.Show()

    def InitUi(self):

        # Make me a little grid you codeing bitch, thanks.
        LpPanel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(LpPanel)
        self.grid.CreateGrid(25, 9)
        self.grid.EnableEditing(False)
        # Box layout
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(self.grid, 1, wx.EXPAND, 5)
        LpPanel.SetSizer(Sizer)
        # Column config
        self.grid.SetColMinimalAcceptableWidth(110)
        self.grid.SetColLabelValue(0, 'Item Name')
        self.grid.SetColSize(0, 110)
        self.grid.SetColLabelValue(1, 'Price [ISK]')
        self.grid.SetColFormatFloat(1, -1, 2)
        self.grid.SetColSize(1, 110)
        self.grid.SetColLabelValue(2, 'LP Cost [EA]')
        self.grid.SetColFormatNumber(2)
        self.grid.SetColSize(2, 110)
        self.grid.SetColLabelValue(3, 'Mineral Cost [ISK]')
        self.grid.SetColFormatFloat(3, -1, 2)
        self.grid.SetColSize(3, 110)
        self.grid.SetColLabelValue(4, 'Total Cost [ISK]')
        self.grid.SetColFormatFloat(4, -1, 2)
        self.grid.SetColSize(4, 110)
        self.grid.SetColLabelValue(5, 'Sell Price Jita [ISK]')
        self.grid.SetColFormatFloat(5, -1, 2)
        self.grid.SetColSize(5, 110)
        self.grid.SetColLabelValue(6, 'Profit [ISK]')
        self.grid.SetColFormatFloat(6, -1, 2)
        self.grid.SetColSize(6, 110)
        self.grid.SetColLabelValue(7, 'Profit [%]')
        self.grid.SetColFormatFloat(7, -1, 2)
        self.grid.SetColSize(7, 110)
        self.grid.SetColLabelValue(8, 'Efficiency [ISK/LP]')
        self.grid.SetColFormatFloat(8, -1, 2)
        self.grid.SetColSize(8, 110)

        # Create a menu bar
        MenuBar = wx.MenuBar()

        # Create the file menu in the menu bar
        FileMenu = wx.Menu()
        new = wx.MenuItem(FileMenu, wx.ID_NEW, '&New')
        FileMenu.Append(new)
        FileMenu.Append(wx.ID_DELETE, '&Delete')
        update = wx.MenuItem(FileMenu, wx.ID_ANY, '&Update\tAlt+F5')
        FileMenu.Append(update)

        FileMenu.AppendSeparator()
        Qmi = wx.MenuItem(FileMenu, wx.ID_EXIT, '&Quit\tAlt+F4')
        # Qmi.SetBitmap(wx.Bitmap('exit.png'))
        FileMenu.Append(Qmi)

        # Create the help menu in the bar
        HelpMenu = wx.Menu()
        HelpMenu.Append(wx.ID_ABOUT, '&About\tF1')

        # Bound functions in the menu bar
        self.Bind(wx.EVT_MENU, self.on_quit, Qmi)
        self.Bind(wx.EVT_MENU, self.fill_table, update)
        self.Bind(wx.EVT_MENU, self.new_item, new)

        # Append the menus to the bar
        MenuBar.Append(FileMenu, '&File')
        MenuBar.Append(HelpMenu, '&Help')
        self.SetMenuBar(MenuBar)

    # Method for filling the table with data
    def fill_table(self, *args):
        """Data fields are: ItemName,IskPrice,LpPoints,MaterialPrice,ItemTotalPrice,SellPriceJita,Profit,ProfitPercent
           and Efficiency """

        grid_fill = grid_data_get()
        for row in range(0, len(grid_fill), 1):
            for item in range(0, len(grid_fill[row]), 1):
                self.grid.SetCellValue(row, item, str(grid_fill[row][item]))

    # Method for the new item dialog
    def new_item(self, *args):

        self.new_item = NewItem.NewItem(None, wx.ID_ANY, "")
        self.new_item.Show()
        return True

    # Method to close the instance
    def on_quit(self, e):

        self.Close()
        # print('CLOSE')


def grid_data_get():
    """Gets the all items in the evedata.EveItemData table for the user interface grid"""

    sql_command = 'SELECT ItemName,IskPrice,LpPoints,MaterialPrice,ItemTotalPrice,SellPriceJita,Profit,ProfitPercent,' \
                  'Efficiency FROM evecalc.EveItemData ORDER BY Efficiency DESC LIMIT 25;'

    # Open mySQL connection
    evecalc = mysql.connector.connect(user='remote', password='remote00Long', host='h2759962.stratoserver.net', database='evecalc')
    # Create a database cursor
    cursor = evecalc.cursor()

    cursor.execute(sql_command)
    grid_data_fetch = cursor.fetchall()

    # Close the mySQL connection
    cursor.close()
    evecalc.close()

    # Returns a python list like: [('Item1'),('Item2')]
    return grid_data_fetch


def main():

    app = wx.App()
    x = EveLpApp(None, title='EveLpApp')
    # x.grid.SetCellValue(1,0,'FUCK')
    app.MainLoop() 

    # print(x.grid)


if __name__ == '__main__':
    main()
