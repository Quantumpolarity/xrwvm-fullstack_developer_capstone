from .models import CarMake, CarModel


def create_car_makes(car_make_data):
    """
    Create CarMake instances from the provided data.

    Args:
        car_make_data (list): List of dictionaries containing CarMake data.

    Returns:
        list: List of created CarMake instances.
    """
    car_make_instances = []
    for data in car_make_data:
        try:
            # Validate data
            if not data.get("name") or not data.get("description"):
                raise ValueError(
                    "CarMake data must contain 'name' and 'description' fields"
                )
            car_make_instance = CarMake.objects.create(
                name=data["name"],
                description=data["description"]
            )
            car_make_instances.append(car_make_instance)
        except Exception as e:
            print(f"Error creating CarMake: {e}")
    return car_make_instances


def create_car_models(car_model_data, car_make_instances):
    """
    Create CarModel instances from the provided data.

    Args:
        car_model_data (list): List of dictionaries containing CarModel data.
        car_make_instances (list): List of created CarMake instances.

    Returns:
        list: List of created CarModel instances.
    """
    car_model_instances = []
    for data in car_model_data:
        try:
            # Validate data
            if not (
                data.get("name")
                and data.get("type")
                and data.get("year")
                and data.get("car_make")
            ):
                raise ValueError(
                    "CarModel data must contain 'name', 'type', 'year', and "
                    "'car_make' fields"
                )
            car_make_instance = car_make_instances[data["car_make"]]
            car_model_instance = CarModel.objects.create(
                name=data["name"],
                car_make=car_make_instance,
                type=data["type"],
                year=data["year"],
            )
            car_model_instances.append(car_model_instance)
        except Exception as e:
            print(f"Error creating CarModel: {e}")
    return car_model_instances


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": 0},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": 0},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": 0},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": 1},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": 1},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": 1},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": 2},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": 2},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": 2},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": 3},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": 3},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": 3},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": 4},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": 4},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": 4},
        # Add more CarModel instances as needed
    ]

    car_make_instances = create_car_makes(car_make_data)
    create_car_models(car_model_data, car_make_instances)

    # Use bulk_create to optimize database operations
