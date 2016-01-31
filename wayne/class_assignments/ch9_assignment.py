name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

senders = dict()
high_value = 0
high_key = ''

for line in handle:
    if line.startswith('From:'):
        sender = line.split(':')[1].strip()
        senders[sender] = senders.get(sender, 0) + 1

for keys in senders.keys():
    if senders[keys] > high_value:
        high_key = keys
        high_value = senders[keys]

high_key = sorted(senders.keys(), key=lambda sender: sender[1],reverse=True)[0]
high_value = senders[high_key]

print '%s %d' % (high_key, high_value)



'''
Ignore this
#print '%s %d' % (high_key, high_value)


#my_senders = filter(lambda line: line.startswith('From:'), open(name))

#my_email_dict = {}

#my_split = sorted(my_senders, key=lambda sender : sender.split(':')[1].strip())

#print my_split

#my_sender.split(':')[1] for my_sender in my_senders:
    my_email = my_sender.split(':')[1].strip()
    my_email_dict[my_email] = my_email_dict.get(my_email, 0) + 1

my_high_key = sorted(my_email_dict.keys(), key=lambda sender: sender[1],reverse=True)[0]
my_high_value = my_email_dict[my_high_key]

print '%s %s' % (my_high_key, my_high_value)
'''