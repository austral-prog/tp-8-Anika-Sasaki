def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    number = str(coordinate[0])
    letter = str(coordinate[1])
    new_coordinate = (number, letter)
    return new_coordinate


def create_record(azara_record, rui_record):
    coordinate = convert_coordinate(azara_record[1])
    if coordinate == rui_record[1]:
        new_coordinate = azara_record + rui_record
        return new_coordinate
    else:
        return "not a match"
