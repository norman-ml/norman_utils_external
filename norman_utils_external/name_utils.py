import base64
import random
import uuid

from norman_utils_external.singleton import Singleton


class NameUtils(metaclass=Singleton):
    adjectives = [
        "Red", "Blue", "Green", "Orange", "Purple", "Pink", "Black", "White", "Brown",
        "Golden", "Silver", "Bright", "Dark", "Light", "Shiny", "Glossy", "Matte", "Soft", "Hard",
        "Smooth", "Rough", "Sharp", "Blunt", "Small", "Large", "Tiny", "Huge", "Slim", "Fat",
        "Tall", "Short", "Wide", "Narrow", "Heavy", "Light", "Warm", "Cold", "Hot", "Cool",
        "Quiet", "Loud", "Silent", "Noisy", "Gentle", "Fierce", "Brave", "Timid", "Fast", "Slow",
        "Agile", "Lazy", "Sleepy", "Energetic", "Hungry", "Thirsty", "Curious", "Clever", "Wise",
        "Friendly", "Mean", "Kind", "Strong", "Weak", "Clean", "Dirty", "Elegant", "Fancy",
        "Simple", "Rich", "Poor", "Proud", "Humble", "Happy", "Sad", "Angry", "Calm", "Nervous",
        "Excited", "Tired", "Cheerful", "Colorful", "Pale", "Bold", "Dull", "Sparkling", "Rusty",
        "Frosty", "Clear", "Cloudy", "Misty", "Rainy", "Stormy", "Sunny", "Breezy", "Windy",
        "Chilly", "Humid"
    ]

    nouns = [
        "Lion", "Tiger", "Elephant", "Bear", "Wolf", "Fox", "Eagle", "Shark", "Panda", "Cheetah",
        "Dragon", "Falcon", "Owl", "Dolphin", "Zebra", "Cat", "Frog", "Penguin", "Kangaroo", "Turtle",
        "Rabbit", "Horse", "Whale", "Camel", "Peacock", "Bee", "Butterfly", "Spider", "Octopus",
        "Starfish", "Jellyfish", "Snail", "Squirrel", "Monkey", "Giraffe", "Duck", "Rooster", "Pigeon",
        "Sparrow", "Antelope", "Buffalo", "Moose", "Lobster", "Crab", "Flamingo", "Hedgehog", "Raccoon",
        "Seahorse", "Salamander", "Iguana", "Lemur", "Chameleon", "Bat", "Raven", "Toucan", "Armadillo",
        "Platypus", "Lynx", "Porcupine", "Walrus", "Opossum", "Parrot", "Stingray", "Manta",
        "Pelican", "Woodpecker", "Hamster", "GuineaPig", "Coyote", "Jackal", "Elk", "Panther", "Gazelle",
        "Leopard", "Llama", "Alpaca", "Tapir", "Vulture", "Hyena", "Gibbon", "Orangutan", "Gorilla",
        "Grizzly", "Catfish", "Swordfish", "Mongoose", "Crocodile", "Alligator", "Sloth", "Wombat",
        "Koala", "Otter", "Seal", "Puffin", "Orca", "Narwhal"
    ]

    @classmethod
    def generate_account_name(cls):
        adjective = random.choice(cls.adjectives)
        noun = random.choice(cls.nouns)

        generated_uuid = uuid.uuid1()
        uuid_time = generated_uuid.time
        time_bytes = uuid_time.to_bytes(8, byteorder="big")
        time_base64 = base64.urlsafe_b64encode(time_bytes).decode("utf-8").rstrip("=")

        return f"{adjective}{noun}{time_base64}"
