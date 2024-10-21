from archer import Archer
from fort import Fort


if __name__ == "__main__":

    archer = Archer(1, "Archer", 10, 20, 100, 15)  

   
    fort = Fort(2, "Fort", 15, 25, True, 50)  

  
    archer.attack(fort)

   
    fort.attack(archer)

   
    archer.move(12, 22)
    print(f"{archer.get_name()}'s HP: {archer.hp}")
