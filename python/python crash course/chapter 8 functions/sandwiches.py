# question 8-12
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheese', 'lettuce', 'honey')
make_sandwich('cheese', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')