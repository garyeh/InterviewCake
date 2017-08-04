# The stolen breakfast drone

# Given the list of IDs, which contains many duplicate integers and
# one unique integer, find the unique integer.

def find_missing_delivery(deliveries):
    key = 0

    for delivery in deliveries:
        key ^= delivery

    return key
