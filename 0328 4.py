#파이썬 피자에 오신것을 환영합니다!
#원하는 피자 사이즈는 S, M , L / 스몰은 만오천원, 중간은 2만원, 큰 피자는 3만원
#페페로니 추가는 2천원
#치즈추가는 3천원
#총 지불하실 금액은?

class PizzaVendingMachine:
    def __init__(self):
        self.menu = {
            "Small": 15,
            "Medium": 20,
            "Large": 30
        }
        self.toppings_price = {
            "Pepperoni": 2,
            "Extar cheese": 3
        }
        self.order = {
            "size": None,
            "toppings": []
        }

    def display_menu(self):
        print("***파이썬 피자에 오신 것을 환영합니다!***")
        print("크기:")
        for size, price in self.menu.items():
            print(f"{size}: ${price}")
        print("\n토핑:")
        for topping, price in self.toppings_price.items():
            print(f"{topping}: ${price}")

    def take_order(self):
        self.display_menu()
        self.order["size"] = input("\n원하는 피자 크기를 선택해주세요: ").capitalize()
        toppings_input = input("추가할 토핑을 선택하세요 (쉼표로 구분): ").split(',')
        self.order["toppings"] = [topping.strip() for topping in toppings_input]

    def calculate_total(self):
        total = self.menu[self.order["size"]]
        for topping in self.order["toppings"]:
            total += self.toppings_price.get(topping, 0)
        return total

    def process_order(self):
        self.take_order()
        total = self.calculate_total()
        print("\n주문 내역:")
        print("크기:", self.order["size"])
        print("토핑:", ', '.join(self.order["toppings"]))
        print("총 금액: $", total)
        print("\n피자가 준비됩니다. 맛있게 드세요!")


if __name__ == "__main__":
    vending_machine = PizzaVendingMachine()
    vending_machine.process_order()