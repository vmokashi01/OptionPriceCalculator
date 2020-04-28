import json

class Option():
    def __init__(self, con_type = "Call", S = 0, K = 0, r = 0, sigma = 0, T = 1):
        self.con_type = con_type
        self.stock_price = S
        self.strike_price = K
        self.risk_free_rate = r
        self.volatility = sigma
        self.time = T

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    
