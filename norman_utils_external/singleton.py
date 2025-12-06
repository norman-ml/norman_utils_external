class Singleton(type):
    """
    Metaclass implementing the Singleton design pattern.

    Classes using this metaclass will only ever have one instance.
    Any attempt to instantiate the class again returns the same
    previously created object.

    **Attributes**

    - **_instances** (`dict[type, Any]`)
      The internal cache mapping classes to their singleton instances. Ensures no class whose metadata class is the Singleton class will be instantiated twice.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    