
from hashlib import new


class Animal:
    def __init__(self, name=None):
        self._name = name
        self._hunger_level = 0

    def set_hunger_level(self, hunger_level):
        # TODO done: make sure hunger level stays between 0 and 10
        if hunger_level > 10:
            hunger_level = 10
        if hunger_level < 0:
            hunger_level = 0

        self._hunger_level = hunger_level

    def get_hunger_level(self):
        return self._hunger_level

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def sleep(self):
        print('sleeping...')
        # TODO done: set hunger level
        self.set_hunger_level(10)

    def roam(self):
        print('moving around...')
        # TODO done: set hunger level
        self.set_hunger_level(self.get_hunger_level()+1)
        
    def make_noise(self):
        raise NotImplementedError('make_noise not implemented')

    def eat(self):
        raise NotImplementedError('eat not implemented')


class Pet:
    def play(self):
        raise NotImplementedError('make_noise not implemented')
    
    def be_friendly(self):
        raise NotImplementedError('make_noise not implemented')


class Canine(Animal):
    def roam(self):
        print('canines like to roam in packs...')
        # TODO done: update hunger level
        self.set_hunger_level(self.get_hunger_level()+1)


class Feline(Animal):
    def roam(self):
        print('felines like to roam alone...')
        # TODO done: update hunger level
        self.set_hunger_level(self.get_hunger_level()+1)


class Wolf(Canine):
    def make_noise(self):
        print('growl...')

    # TODO done: add eat method
    def eat(self):
        print('rip with teeth...')
        self.set_hunger_level(self.get_hunger_level()-2)
        

# TODO done: inherit from Pet class
class Cat(Feline, Pet):
    def make_noise(self):
        print('meow...')

    # TODO done: add eat method
    def eat(self):
        print('pick...')
        self.set_hunger_level(self.get_hunger_level()-3)

    # TODO done: add Pet methods
    def play(self):
        print('frolic...')

    def be_friendly(self):
        print('purr...')

# TODO done: Dog class
# TODO done: inherit from Pet class
class Dog(Canine, Pet):
    def make_noise(self):
        print('bark...')

    def eat(self):
        print('slop...')
        self.set_hunger_level(self.get_hunger_level()-3)

    # TODO done: add Pet methods
    def play(self):
        print('scamper...')
    
    def be_friendly(self):
        print('sniff...')


# TODO done: Lion class
class Lion(Feline):
    def make_noise(self):
        print('roar...')

    def eat(self):
        print('rip with teeth...')
        self.set_hunger_level(self.get_hunger_level()-2)

# TODO done: Hippo class
class Hippo(Animal):
    def make_noise(self):
        print('blub...')

    def eat(self):
        print('slurp...')
        self.set_hunger_level(self.get_hunger_level()-1)

class Zoo:
    
    def __init__(self, name=None):
        self._name = name
        # TODO done: add field that contains the animals
        self._zoo_animals = []

    # TODO done: add the "add animal" method
    def add_animal(self, animal):
        self._zoo_animals.append(animal)
        
    # TODO done: "test animals" method
    def test_animals(self):
        print('zoo name: {}'.format(self._name))
        print('number of animals: {}'.format(len(self._zoo_animals)))
        
        for animal in self._zoo_animals:
            print('name: {}'.format(animal.get_name()))
            animal.sleep()
            animal.make_noise()
            while(animal.get_hunger_level() != 0):
                animal.eat()
            print('hunger_level: {}'.format(animal.get_hunger_level()))
            animal.roam()
            if isinstance(animal, Pet):
                animal.play()
                animal.be_friendly()
            print('-------------------')


# TODO done: main function
def main():
    h = Hippo('hilda the hippo')
    l = Lion('lily the lion')
    d = Dog('dilly the dog')
    c = Cat('kat the cat')
    w = Wolf('willy the wolf')

    z = Zoo('big ole zoo')

    z.add_Animal(h)
    z.add_Animal(l)
    z.add_Animal(d)
    z.add_Animal(c)
    z.add_Animal(w)

    z.test_animals()

if __name__ == '__main__':
    main()