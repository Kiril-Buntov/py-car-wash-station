class Car:

    def __init__(self,comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, Cars_list: list(Car)) -> None:
        for car in Cars_list:
            if car.clean_mark < self.clean_power:
                car.clean_mark =

    def calculate_washing_price(self, Cars_list: list) -> None:

