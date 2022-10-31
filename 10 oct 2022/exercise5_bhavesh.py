'''
The string
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"`
is garbled in two ways:
• First, our message is backwards;
• Second, the letter we want is every other letter.
Use lambda and filter to extract the message and save it to a variable called message. Use list
slicing to extract the message and save it to a variable called message.
'''
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1]
print(message)

message1 = list(filter(lambda i: i !='X', message))
print(message1)
# print("".join(message))
print(message[::2])
