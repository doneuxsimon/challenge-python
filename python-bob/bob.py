def hey(ask):
    answer = ""
    ask = ask.strip()
    if len(ask) == 0:
        answer = "Fine. Be that way!"
    elif ask.isupper():
        answer = "Whoa, chill out!"
    elif ask[len(ask) - 1] == "?":
        answer = "Sure."
    else:
        answer = "Whatever."
    print(answer)
    return answer