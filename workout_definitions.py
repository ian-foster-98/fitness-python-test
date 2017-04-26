def increment_by_percentage(weight):
    pass

definitions = {
    "standard_workout_upper": {
        "Dips": {
            "default_weight": 0,
            "increment_function": increment_by_percentage
        },
        "Pull-ups": {
            "default_weight": 0,
            "increment_function": increment_by_percentage
        },
        "Bench Press": {
            "default_weight": 40,
            "increment_function": increment_by_percentage
        },
        "Bent over rows": {
            "default_weight": 40,
            "increment_function": increment_by_percentage
        },
        "Shoulder Press": {
            "default_weight": 20,
            "increment_function": increment_by_percentage
        },
    },
    "standard_workout_lower": {
        "Back Squat": {
            "default_weight": 20,
            "increment_function": increment_by_percentage
        },
        "Deadlift": {
            "default_weight": 20,
            "increment_function": increment_by_percentage
        },
        "Stiff-legged deadlift": {
            "default_weight": 20,
            "increment_function": increment_by_percentage
        },
        "Overhead rows": {
            "default_weight": 20,
            "increment_function": increment_by_percentage
        },
        "Lunges": {
            "default_weight": 20,
            "increment_function": increment_by_percentage
        },
    }
}
