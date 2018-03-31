def chess_reward():
    corn = 1
    for chess_square in range(64):
        corn = corn * 2
        if corn >= 1000000:
            corn -= 1
            break
    return chess_square + 1, corn

print(chess_reward())