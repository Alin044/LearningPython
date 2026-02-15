#Match case(switch)

def day_of_week(day):
    match day:
        case 1:
            return "It's monday"
        case 2:
            return "It's tuesday"
        case 3:
            return "It's wednesday"
        case 4:
            return "It's thursday"
        case 5:
            return "It's friday"
        case 6:
            return "It's saturday"
        case 7:
            return "It's sunday"
        case _:
            return "Invalid day!"

print(day_of_week(2))
