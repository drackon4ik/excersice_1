owners_car = {}


def user_info(name, model, mark):
    return name, model, mark


def creating_user_dict(name, model, mark):
    owners_car[name] = {"name"}
    owners_car[model] = {"model"}
    owners_car[mark] = {"mark"}


def returning_info(name, model, mark):
    return f"{name} is owner {model}. {model} is car`s model of {mark}"


print(returning_info("max", "jaguar", "nissan"))