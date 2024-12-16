sent_message = ('Hey there! This is a secret message. \n', 'What can this do?')

with open('sent_message.txt', 'w') as file:
  for i in sent_message:
    file.write(i)

with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  # Move the cursor to the beginning of the file
  file.seek(0)

  # Modify the message to simulate unsending
  unsent_message = 'This message has been unsent.'
  file.write(unsent_message)
  file.truncate(len(unsent_message))

print(original_message)
print(unsent_message)