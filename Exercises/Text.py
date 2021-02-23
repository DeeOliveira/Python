text = "X-DSPAM-Confidence:    0.8475"
text.strip()
ptxt = text.find(':')
final = text[ptxt+1:30]
ffinal = float(final)
print (ffinal)
