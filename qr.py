import qrcode

data = input("Enter link or text: ")
img = qrcode.make(data)
img.save("qrcode.png")

print("✅ QR created!")