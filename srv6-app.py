from cgi import test
import  test_pb2

person =  test_pb2.Person()
person.id = 123
person.name =  "John Doe"
person.email = "john@example.com"
phone  = person.phones.add()
phone.number =  "555-4321"
phone.type = test_pb2.Person.HOME
