def feedDog(hungry_boi, biscuts):
    dogs_fed = 0
    biscuts.sort()                  #O(nlogn)
    good_boi_counter = 0
    for treat in range(len(biscuts)):
        if good_boi_counter >= len(hungry_boi):
            return good_boi_counter
        if biscuts[treat] >= hungry_boi[good_boi_counter]:
            good_boi_counter += 1
    return good_boi_counter
