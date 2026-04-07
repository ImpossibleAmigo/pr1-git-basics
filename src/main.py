def uah_to_usd(uah_amount, rate=39.5):
    return uah_amount / rate

print("Hello, World! Це моя перша практична робота з Git.")

amount = 1000
usd_result = uah_to_usd(amount)
print(f"{amount} ГРН - це приблизно {usd_result:.2f} USD")
