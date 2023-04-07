import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import string 


# Load the chat data from the Excel file
df = pd.read_excel('merged_file.xlsx')

# Group the messages by the sender and count the number of messages per sender
msg_count = df.groupby('Name')['Message'].count()

x = msg_count.pop("Truth or Dare")
y = msg_count.pop("StudyLion")
msg_count.pop("IAM ADHU")
msg_count.pop("Carl-bot")
msg_count.pop("Shivesh")
import matplotlib.pyplot as plt

# Create a list of colors for the pie chart
colors = ['lightcoral', 'gold', 'lightskyblue', 'yellowgreen', 'pink', 'orange']

# Create a figure and axis object
fig, ax = plt.subplots()

# Create a pie chart using the msg_count data
ax.pie(msg_count.values, labels=msg_count.index, colors=colors, autopct='%1.1f%%', startangle=90)

# Set the title of the pie chart
ax.set_title('Message Count by Sender')

# Show the plot
plt.savefig('pie.png')


# Print the number of messages per sender
print(msg_count)

# Create a dictionary to store the words and their frequency for each sender
word_freq = {}

# Loop through each sender's messages and tokenize the words
for sender in df['Name'].unique():
    # Combine all messages from the sender into a single string
    sender_msgs = ' '.join(df.loc[df['Name'] == sender, 'Message'].fillna('').astype(str).tolist())
    # Tokenize the words
    words = sender_msgs.lower().translate(str.maketrans('', '', string.punctuation)).split()
    # Calculate the frequency of each word and store it in the dictionary
    word_freq[sender] = {}
    for word in words:
        if word in word_freq[sender]:
            word_freq[sender][word] += 1
        else:
            word_freq[sender][word] = 1

# Print the top 5 most used words for each sender
word_freq_dict = {}
for sender in word_freq:
    word_freq_dict[sender] = {}
    sorted_words = sorted(word_freq[sender].items(), key=lambda x: x[1], reverse=True)
    for i in range(5):
        if i < len(sorted_words):
            word_freq_dict[sender][sorted_words[i][0]] = sorted_words[i][1]
print(word_freq_dict)
