class planet:
  def __init__(self,name,moons,rings, gases=None):
    self.name = name
    self.gases = gases
    self.moons = moons
    self.rings = rings
    def moon_count(self):
      return self.moons
    def rings_count(self):
      return self.rings

Mercury = planet('Mercury',0,'No',[])
Venus   = planet('Venus',0,'No',['Carbon Dioxide','Nitrogen'])
Earth   = planet('Earth',1,'No',['Nitrogen','Oxygen'])
Jupitor  = planet('Jupitor',79,'Yes',['Helium','Hydrogen'])
Saturn   = planet('Saturn',83,'Yes',['Helium','Hydrogen'])
Uranus   = planet('Uranus',27,'Yes',['Helium','Hydrogen','Methane'])

planets = [Mercury,Venus,Earth,Jupitor,Saturn,Uranus]

def moon_count(planets):
    moons = {}
    for planet in planets :
        if planet.rings == 'Yes':
            moons[planet.name] = planet.moons
    return moons
 
plane_moons = moon_count(planets)
print(plane_moons)

def gas_on_planets(planets):
    gases = {}
    
    for planet in planets :
        
        if planet.gases :  
            for gas in planet.gases :
                gases[gas] = gases.get(gas,0) + 1
                
    gases_max = max(gases.values())
    for name,val in gases.items():
        if val == gases_max :
            print(name)
gas_on_planets(planets)
