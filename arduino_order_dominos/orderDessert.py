import serial 
import sys
from serial import Serial
from pizzapi import *

recv = False 
ardSerial = serial.Serial('/dev/cu.usbmodem14101', 9600)

print(len(sys.argv))
if len(sys.argv) == 2: 
    print("Test run")

print("Awaiting serial input...")


while(recv == False): 
    response = ardSerial.readline().decode("utf-8").strip()
    if response == "1": 
        recv = True 

## Order Pizza 
customer = Customer("Name", "Namington", "me@namenamington.com", "8888888888")
address = Address("Addr", "City", "State", "Zip")

store = address.closest_store()
print("Store address: ")
storeAddr = store.get_details()
print(storeAddr["StreetName"] + " " + storeAddr["City"] + " " + storeAddr["Region"]) 

menu = store.get_menu()

menu.search(Name = "Chocolate");

order = Order(store, customer, address);
order.add_item('B2PCLAVA')
order.add_item('B2PCLAVA')
order.add_item('B2PCLAVA')
order.add_item('B2PCLAVA')

cnm = input('enter card number: ')
exp = input('enter expiry ####: ')
cvv = input('enter cvv: ')
zco = input('enter zip: ')

card = PaymentObject(cnm, exp, cvv, zco)

if len(sys.argv) == 2: 
    print(order.pay_with(card))
else: 
    print(order.place(card))

## Arduino success notification: 
ardSerial.write(b'1')