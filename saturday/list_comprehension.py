
# Simple
data = [i for i in range(100)]


members = [
            {'age': 43, 'name': 'Denis'},
            {'age': 1, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'Spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'Claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'Homer'}
        ]


# simple example
members_age = [member['age'] for member in members]
members_name = [member['name'] for member in members]
members_full = [member for member in members]
members_something_important = [len(member) for member in members]


# Example with if
members_with_age_older_than_40 = [member for member in members if member['age']]


# Example if and else
members_filter = [member if member['age'] > 40 else None for member in members]

print("members_age", members_age)
print("members_name", members_name)
print("members_full", members_full)
print("members_something_important", members_something_important)


print("\n")

print("members_with_age_older_than_40", members_with_age_older_than_40)

print("\n")
print("members_filter ", members_filter)
