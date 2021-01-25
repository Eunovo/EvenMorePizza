class Problem:
    def __init__(self, teams, pizzas):
        self.teams = teams
        self.pizzas = pizzas

    @staticmethod
    def from_file(file_path):
        with open(file_path, "r") as file:
            params = file.readline().strip("\n").split(" ")
            n_pizzas = int(params[0])
            n_teams_two = int(params[1])
            n_teams_three = int(params[2])
            n_teams_four = int(params[3])

            pizzas = []

            for i in range(n_pizzas):
                pizza_line = file.readline().strip("\n").split(" ")
                n_ingredients = int(pizza_line[0])
                ingredients = []
                
                for x in range(1, len(pizza_line)):
                    ingredients.append(pizza_line[x])
                
                if (n_ingredients != len(ingredients)):
                    raise ValueError(
                        "Number of ingredients did not match number of extracted ingredients")

                pizzas.append(ingredients)

            if (n_pizzas != len(pizzas)):
                raise ValueError(
                    "Number of pizzas did not match number of extracted pizzas")

            return Problem({
                2: n_teams_two,
                3: n_teams_three,
                4: n_teams_four
            }, pizzas)
