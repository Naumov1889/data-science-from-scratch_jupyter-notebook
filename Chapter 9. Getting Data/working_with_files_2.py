from collections import Counter

def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]
# For example, "abdul_rainbolt1@aol.com".split("@")
# abdul_rainbolt1 — [0]  aol.com — [1]
# [-1] — first from the end, which is the same as [1] in this case.

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)
print(domain_counts)
# Output will be smth like this:
# Counter({'aol.com': 61, 'outlook.com': 61, 'hotmail.com': 49, 'yahoo.com': 45})

# If no line.strip(), that is no trimming spaces, then:
# Counter({'aol.com\n': 61, 'outlook.com\n': 61, 'hotmail.com\n': 48, 'yahoo.com\n': 45})