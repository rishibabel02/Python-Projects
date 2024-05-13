import segno

s = "www.google.com"
qr = segno.make_qr(s)
qr.save("4.png",
        scale = 10,
        border = 2,
        light = "white",
        dark = "black",
        quiet_zone = "Lightgreen",
        # data_dark = "red"
)
