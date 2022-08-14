from ast import Sub
from classes.ninja import Ninja
from classes.ninja import Kunoichi
from classes.pirate import Pirate
from classes.pirate import Ancient

Sub_Zero = Ninja("Sub Zero")
Kunimitsu = Kunoichi("Kunimitsu")
Jack_Sparrow = Pirate("Jack Sparrow")
Eric_The_Red = Ancient("EricTheRed")
# Game PLay
# chained
# works
Sub_Zero.attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow).attack(Jack_Sparrow)
Jack_Sparrow.show_stats()

works
Jack_Sparrow.attack(Sub_Zero).attack(Sub_Zero).attack(Sub_Zero).attack(Sub_Zero).attack(Sub_Zero).attack(Sub_Zero).attack(Sub_Zero)
Sub_Zero.show_stats()

Kunimitsu.attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red).attack(Eric_The_Red)
Eric_The_Red.show_stats()

Eric_The_Red.attack(Kunimitsu).attack(Kunimitsu).attack(Kunimitsu).attack(Kunimitsu).attack(Kunimitsu).attack(Kunimitsu).attack(Kunimitsu)
Kunimitsu.show_stats()