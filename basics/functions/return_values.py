def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    total_avg_weight = sum_weights(beep_weight, bop_weight) / 2
    return total_avg_weight

def run():
    print("beep weight?")
    beep_weight = float(input())

    print("bop weight?")
    bop_weight = float(input())

    print("sum or avarage?")
    action = input()
    if (action == "sum"):
      answer = sum_weights(beep_weight, bop_weight)
      print("The sum of Beep and Bop's weight is {:.2f}.".format(answer))
    elif (action == "avarage"):
      answer = calc_avg_weight(beep_weight, bop_weight)
      print("The avarage of Beep and Bop's weight is {:.2f}.".format(answer))
    else:
      print("I am not sure what would you like to do!")

run()