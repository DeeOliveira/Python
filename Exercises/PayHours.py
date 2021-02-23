def computepay(xh, xr):
    if xh < 40 :
       xp = float(xh) * float(xr)
    else :
       xp = (40 * float(xr)) + ((float(xh)-40) * (float(xr)*1.5))
    return xp

pg = computepay(xh = float(input("Enter Hours: ")), xr = float(input("Enter Rate: ")))

print("Pay ", pg)
