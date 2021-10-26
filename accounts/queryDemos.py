#***(1)Returns all customers from customer table
from accounts.models import Dogs, Owner, Volunteer


customers = Owner.objects.all()

#(2)Returns first customer in table
firstCustomer = Owner.objects.first()

#(3)Returns last customer in table
lastCustomer = Owner.objects.last()

#(4)Returns single customer by name
customerByName = Owner.objects.get(name='Peter Piper')

#***(5)Returns single customer by name
customerById = Owner.objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()