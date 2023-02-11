
import socketserver as socket,http.server
from PIL import  Image 
import tkinter as tk 

PORT = 8000
def wlan_ip():
    import subprocess
    wireless1="wireless"
    wireless2="wireless lan adapter wi-fi"
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if wireless2 in i: scan=1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()
        # print(i)
# print(wlan_ip()) #usually 192.168.0.(DHCP assigned ip)
ip = wlan_ip()
converted_ip = str(ip)

link = "http://"+converted_ip+":"+str(PORT)+"/"

# convert ip address to qrcode
import qrcode
img = qrcode.make(str(link))
x = 'qrcode_test.png'
img.save(x)

# def tki():
#     root=tk.Tk()
#     root.geometry('350x350')
#     x = "qrcode_test.png"
#     img = Image.open(x) 
#     img = img.resize((400, 400), Image.ANTIALIAS) 
#     img = ImageTk.PhotoImage(img) 
#     panel = tk.Label(root, image = img) 
#     panel.image = img
#     # place image in frame
#     frame = tk.Frame(root, bg="#988c89") # create frame to insert selected picture
#     frame.place()
#     frame.pack()
#     label1 = tk.Label(frame, image=img)
#     label1.pack()
#     root.bind("<Escape>", lambda x: root.destroy())
#     root.mainloop()
# tki()

# open image
img = Image.open(x) 
img.show()
print(link)

# create server
Handler = http.server.SimpleHTTPRequestHandler
with socket.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
  
