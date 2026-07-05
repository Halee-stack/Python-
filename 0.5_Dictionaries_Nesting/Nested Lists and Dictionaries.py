# A nested list is a list that contains one or more lists as its elements. Instead of storing only individual values (such as numbers or strings), a nested list stores other lists, creating a hierarchical or multi-level data structure.

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#travel_log = {
    #"France": ["Paris", "Lille", "Dijon"],
    #"Germany": ["Berlin", "Stuttgart"],
#}
#print Lille
#print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])


travel_log = {
    "France": {
        "total_visites": 8,
        "cities_visited":["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "total_visits": 12,
        "cities_visits": ["Berlin", "Hamburg", "Stuttgart"],
    },
}
print(travel_log["Germany"]["cities_visits"][2])