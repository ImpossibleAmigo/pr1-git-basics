def print_hi(name):
    # Ця функція виводить привітання, як вимагає завдання
    print(f'Hi, {name}')

def uah_to_usd(uah_amount, rate=39.5):
    return uah_amount / rate

if __name__ == '__main__':
    # ОСНОВНА ЧАСТИНА ЗАВДАННЯ:
    print_hi('Олексій Чеберяко')

    print("Hello, World! Це моя перша практична робота з Git.")

    amount = 1000
    usd_result = uah_to_usd(amount)
    print(f"{amount} ГРН - це приблизно {usd_result:.2f} USD")