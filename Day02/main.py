# combination: 12 red, 13 green, 14 blue

# track each round with dictionary and append into list

def read(file: str) -> list[list[dict[str, int]]]:
    # example list
    # list = [[{"green": 2, "red": 4}]]
    games = [[]]
    with open(file) as input:
        for line in input:
            _, round = line.split(":")
            rounds = []
            # append game by game, split by ; for each draw
            for round in round.split(";"):
                # example output
                # 20 green, 3 red, 2 blue
                # 9 red, 16 blue, 18 green
                # 6 blue, 19 red, 10 green
                # 12 red, 19 green, 11 blue
                # print(round)
                roundsDict = {}
                for balls in round.split(","):
                    # remove white space and separate each color and amt
                    amt, color = balls.strip().split(" ")
                    roundsDict[color] = int(amt)
                rounds.append(roundsDict)
            games.append(rounds)
    return games


def main():
    games = read("input.txt")
    # criteria
    red, green, blue = 12, 13, 14
    score = 0

    # get which game round and amt fits criteria
    for gameNum, rounds in enumerate(games):
        # loop through all the games to get amt of each color
        for round in rounds:
            # if any of the amt is more than the combination reject it
            if round.get("red", 0) > red or round.get("green", 0) > green or round.get("blue", 0) > blue:
                break
        else:
            score += gameNum
    print("Score is: ", score)


if __name__ == "__main__":
    main()
