def bird_distance(distance: int, train_speed: int, bird_speed: int) -> float:
    return bird_speed * distance / train_speed


print(bird_distance(10, 1, 2))
