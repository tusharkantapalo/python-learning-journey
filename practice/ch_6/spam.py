cmt = input("Enter your comment: ");

if ("make a lot of money" in cmt.lower() or "buy this" in cmt.lower() or "subscribe this" in cmt.lower() or "click this" in cmt.lower()):
    print("Spamming")
else:
    print("Not spamming")