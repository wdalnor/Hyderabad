from string import Template

def Main():

    cart = []
    cart.append(dict(item="cake", price=100, qty=2))
    cart.append(dict(item="milk", price=20, qty=5))
    cart.append(dict(item="bost", price=14, qty=40))

    t = Template("$qty * $item = $price")
    total = 0
    print "Cart:"
    for data in cart:
    	print t.substitute(data)
    	total += data['price']
    print "Total :  " + str(total)

if __name__ == "__main__":
    	Main()



