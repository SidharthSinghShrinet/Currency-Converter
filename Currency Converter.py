from currency_converter import CurrencyConverter
Amount=int(input("Enter the amount:"))
Current_Currency=str(input("Fill the current currency in shortform(ALL WORD OF SHORTFORM SHOULD BE IN CAPITAL LETTER):"))
Required_Currency=str(input("Fill the required currency in shortform(ALL WORD OF SHORTFORM SHOULD BE IN CAPITAL LETTER):"))
Converting=CurrencyConverter().convert(Amount,Current_Currency,Required_Currency)
print("YOUR CONVERTED CURRENCY IS",Converting)