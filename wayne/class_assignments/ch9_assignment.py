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


print '%s %d' % (high_key, high_value)



