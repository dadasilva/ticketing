# ticket_system.py
import os
#time requirements
import time

activeOrders = []
finishedOrders = []
shopOpen = True
PRINTBUFFER = "                          "

def clear():
    os.system("clear")

def printActiveOrders():
    for o in activeOrders:
        o.printTicket()

def printFinshedOrders():
    for o in finishedOrders:
        o.printTicket()

class Ticket:
    def __init__(self):
      self.phone = None
      self.name = None
      self.ticketNum = None
      self.start_time = None
      self.end_time = None
      self.elapsed_time = None

    def writeTicket(self, tt):
        self.addticketNumber()
        self.addPhoneNumber()
        self.addName()
        if tt == -1:
            self.currentTime()
        else:
            self.start_time = tt

    def addName(self):
        self.name = input("Name: ")

    def addticketNumber(self):
        self.ticketNum = input("Add order number: ")

    def addPhoneNumber(self):
        self.phone = input("Add phone number: ")

    def currentTime(self):
        self.start_time = time.asctime( time.localtime(time.time()) )

    def endTime(self):
        self.end_time = time.asctime( time.localtime(time.time()) )
        #self.end_time = time.asctime(endTime - currentTime)

    def printTicket(self):
        print("{} ________________________\n".format(PRINTBUFFER))
        print("{}| Order Number: {}".format(PRINTBUFFER, self.ticketNum))
        print("{}| Name: {}".format(PRINTBUFFER, self.name))
        print("{}| Phone Number: {}".format(PRINTBUFFER, self.phone))
        print("{}| Start Time: {}".format(PRINTBUFFER, self.start_time))
        if self.end_time:
            print("{}| End Time: {}".format(PRINTBUFFER, self.end_time))
            #print(" | Elapsed Time: ", self.elapsed_time)
        print("{} ________________________".format(PRINTBUFFER))


def remove(ticket_number):
    index = -1
    #find ticket
    for ticket in activeOrders:
        print(ticket.ticketNum)
        index+=1
        if ticket_number == ticket.ticketNum:
            print("Found {} at {}".format(ticket_number, index))
            ticket.endTime()
            finishedOrders.append(ticket)
            activeOrders.pop(index)
            return 1
    #if ticket is not foundn
    return 0


# --- main --- #

while shopOpen:
    clear()
    printActiveOrders()
    #print(activeOrders)
    print("OPTIONS")
    print(" 0: NEW TICKET")
    print(" 1: EDIT")
    print(" 2: RFP")
    print(" 3: LIST FINISHED TICKETS")
    print("  ________________________")
    print("Total Tickets:", len(activeOrders))

    choice = input()

    if choice == '0':
        myTicket = Ticket()
        myTicket.writeTicket(-1)
        activeOrders.append(myTicket)
    elif choice == '1':
        orderToEdit = input("Which ticket do you want to edit: ")
        pass
    elif choice == '2':
        ticket = input("Enter ticket to remove: ")
        if remove(ticket):
            print("Ticket [{}] removed. Call number for pickup!".format(ticket))
        else:
            print("Ticket [{}] NOT removed. Try again".format(ticket))
    elif choice == '3':
        clear()
        printFinshedOrders()
        os.system("sleep 3")
    else:
        print("Sizzle Sizzle Sizzle")
    #clear()
