entityTypes = ['NPC', 'Enemy', 'Animal']
hostilityTypes = ['Peaceful', 'Neutral', 'Hostile', 'Aggressive']
class Entity:
    def __init__(self, name: str, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        self.name = name
        self.health = health
        self.defense = defense
        self.entityType = entityType
        self.hostility = hostility
        self.drops = drops # 
        
        if not isinstance(name, str):  
            raise TypeError("Entity Name must be a string value")
        if not isinstance(health, int):
            raise TypeError("Entity Health must be an integer value")
        if not isinstance(defense, int):
            raise TypeError("Entity Defense must be an integer value")
        if not isinstance(entityType, str):
            raise TypeError("Entity Type must be a string value")
        if not isinstance(hostility, str):
            raise TypeError("Entity Hostility must be a string value")
        self.checkEntityType()

    def checkEntityType(self):
        if self.entityType.upper() not in entityTypes: # is it valid?
            raise invalidEntityType # if not, raise exception

    def checkEntityHostility(self):
        if self.hostility.upper() not in hostilityTypes:
            raise invalidHostilityType

    def entityInfo(self):
        return f"Entity Info\n-----------\nName: {self.name}\nHealth: {self.health}\nDefense: {self.defense}\nEntity Type: {self.entityType}\nHostility: {self.hostility}\nDrops: {self.drops}"

# could hostilies be classes?

# inherited classes
class NPC(Entity):
    def __init__(self, name: str, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        super().__init__(name, health, defense, entityType, hostility, drops)

    def entityInfo(self):
        return f"{super().entityInfo()}\nidk man i'll add more attributes later"
    
class Enemy(Entity):
    def __init__(self, name: str, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        super().__init__(name, health, defense, entityType, hostility, drops)
    
    def entityInfo(self):
        return f"{super().entityInfo()}"

class Animal(Entity):
    def __init__(self, name: str, health: int, defense: int, entityType: str, hostility: str, drops: list = []):
        super().__init__(name, health, defense, entityType, hostility, drops)
    
    def entityInfo(self):
        return f"{super().entityInfo()}"

# custom exceptions
class invalidEntityType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid entity type, you sure you have the correct entity type?"

class invalidHostilityType(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid entity hostility. Please check your spelling!! Because i cant spell hositlity for the life of me!!!"
