xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
fxh = float(xh)
if fxh < 40 :
   xp = float(xh) * float(xr)
else :
   xp = (40 * float(xr)) + ((float(xh)-40) * (float(xr)*1.5))
print(xp)
