# Math functions in Python for the evecalc project

def MineralPriceCalc(MineralPrice, MineralNeed):
    "Calculation of the total mineral price of a given item from the database"
    MineralPriceTotal = 0
    # Iterates trough the needed minerals 
    for x in MineralNeed:
        MineralPriceTotal = MineralPriceTotal + MineralNeed[x] * MineralPrice[x]
    return MineralPriceTotal

def TotalPrice (LpStoreItemPrice, MineralPriceTotal):
    "Calculation of the total item price, thats the mineral price + the LP store price"
    ItemTotalPrice = LpStoreItemPrice + MineralPriceTotal
    return ItemTotalPrice

def ItemProfit (SellPriceJita, PriceTotal):
    "Calculation of the profit in ISK and in percent"
    ProfitCombined = {'ISK' : 0, 'Percent' : 0}
    # Profit in ISK
    ProfitCombined['ISK'] = SellPriceJita - PriceTotal
    # Profit in %
    ProfitCombined['Percent'] = SellPriceJita / PriceTotal * 100
    return ProfitCombined

def LpEfficiency(ProfitIsk, LoyaltyPoints):
    "Calculates the profit/LP, also called the efficiency"
    ProfitPerLp = ProfitIsk / LoyaltyPoints
    return ProfitPerLp 
