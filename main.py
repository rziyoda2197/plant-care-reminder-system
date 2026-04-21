class EventTicket:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_price(self):
        return self.price - (self.price * self.discount / 100)

class EventTicketComparator:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def compare_tickets(self):
        self.tickets.sort(key=lambda x: x.get_price())
        return self.tickets

# Misol:
comparator = EventTicketComparator()

ticket1 = EventTicket("Ticket 1", 100, 10)
ticket2 = EventTicket("Ticket 2", 80, 5)
ticket3 = EventTicket("Ticket 3", 120, 15)

comparator.add_ticket(ticket1)
comparator.add_ticket(ticket2)
comparator.add_ticket(ticket3)

sorted_tickets = comparator.compare_tickets()

for i, ticket in enumerate(sorted_tickets):
    print(f"{i+1}. {ticket.name}: {ticket.get_price()} so'm")
```

Kodda EventTicket klassi yaratilib, unda eventning nomi, narxi va faqatgina discount qiymati saqlanadi. Narxni hisoblash uchun get_price metodidan foydalaniladi. EventTicketComparator klassi yaratilib, unda eventlar ro'yxati saqlanadi. Ro'yxatga event qo'shish uchun add_ticket metodidan foydalaniladi. Eventlar ro'yxatini tartibga solish uchun compare_tickets metodidan foydalaniladi. Misol uchun uchta event yaratilib, ular ro'yxatga qo'shiladi va sozlangan tartibda chiqariladi.
