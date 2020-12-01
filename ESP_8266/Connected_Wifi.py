"""

def do_connect():
    import network

    ssid = "Home_Wifi"
    password = "sweethome"

    
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    print('Wifi connection successfully')

      
"""