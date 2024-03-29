import random
if __name__ == "__main__":
    # Version 1:
    invitations = ["ali", "ahmad", "mahdi"]
    print("***Welcome to invite to our dinner!***")
    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")
    print("----------------------------------------------------------------------")
    # Version 2:
    invitations = ["ali", "ahmad", "mahdi"]
    print("***Welcome to invite to our dinner!***")
    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")

    rand = random.choice(invitations)
    print(f"Hi, I'm {rand.title()}, Sorry I can't make the dinner.")
    for i in range(len(invitations)):
        if invitations[i] == rand:
            invitations[i] = "mohammad"
            break
    print(f"Invitations: {invitations}")
    print("----------------------------------------------------------------------")
    # Version 3: (more guests)
    invitations = ["ali", "ahmad", "mahdi"]
    print("***Welcome to invite to our dinner!***")
    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")

    moreGuests = ["mohammad", "amir", "parsa"]
    for x in moreGuests:
        print(f"Attention! {x.title()} informed that he wants to be invited to dinner.")

    for i in range(len(moreGuests)):
        if i == 0:
            invitations.insert(0, moreGuests[i])
        elif i == 1:
            invitations.insert(1, moreGuests[i])
            # invitations.insert(2, moreGuests[i])
        else:
            invitations.append(moreGuests[i])

    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")

    print("----------------------------------------------------------------------")
    # Version 4: (special guests)
    print("***Welcome to invite to our dinner!***")
    print(invitations)
    print(f"Sorry everyone, I can invite only two people {invitations[1].title()} and {invitations[3].title()} "
          f"for dinner")
    for i in range(len(invitations)):
        if invitations[i] == invitations[1] or invitations[i] == invitations[3]:
            print(f"*Welcome {invitations[i].title()}, you’re still invited to dinner*")
        else:
            print(f"I'm sorry {invitations[i].title()} that I can’t invite you to dinner!")

    print(f"Full invitations = {invitations}")
    invitations.clear()
    print(f"Empty invitations = {invitations}")
