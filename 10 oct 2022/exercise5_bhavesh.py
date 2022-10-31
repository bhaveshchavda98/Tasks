garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1]
print(message)

message1 = list(filter(lambda i: i !='X', message))
print(message1)
# print("".join(message))
print(message[::2])
