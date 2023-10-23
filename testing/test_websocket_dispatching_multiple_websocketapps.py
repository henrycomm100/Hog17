import websocket, rel

addr = "wss://api.gemini.com/v1/marketdata/%s"
for symbol in ["BTCUSD", "ETHUSD", "ETHBTC"]:
    ws = websocket.WebSocketApp(addr % (symbol,), on_message=lambda w, m : print(m))
    ws.run_forever(dispatcher=rel, reconnect=3)  
rel.signal(2, rel.abort)  # Keyboard Interrupt  
rel.dispatch()  