esoph
# Data darstellen lassen
data("esoph")

summary(esoph)

tapply(esoph$ncases, esoph$agegp, FUN = sum)
#Anhand dieser Daten kann man feststellen, dass die Altersgruppen 25-34 und 35-44, unabhängig vom Alkohol-
#und/oder Tabakkonsum, wenig bis gar nicht gefährdet sind.

esoph_45_54<-subset(esoph, (agegp == "45-54"))
print(esoph_45_54)

tapply(esoph_45_54$ncases, esoph_45_54$alcgp, FUN = sum)
barplot(tapply(esoph_45_54$ncases, esoph_45_54$alcgp, FUN = sum), col = "red", main="Erkrankte in der Altersgruppe 45-54 nach ihrem Alkoholkonsum")
##In der Altersgruppe 45-54 sind die Wenigtrinker am wenigsten gefährdet.
tapply(esoph_45_54$ncases, esoph_45_54$tobgp, FUN = sum)
barplot(tapply(esoph_45_54$ncases, esoph_45_54$tobgp, FUN = sum), col = "yellow", main="Erkrankte in der Altersgruppe 45-54 nach ihrem Tabakkonsum")
summary(esoph_45_54)
#In der Altersgruppe 45-54 sind die Wenigraucher am meisten gefährdet.

esoph_55_64<-subset(esoph, (agegp == "55-64"))
print(esoph_55_64)

tapply(esoph_55_64$ncases, esoph_55_64$alcgp, FUN = sum)
barplot(tapply(esoph_55_64$ncases, esoph_55_64$alcgp, FUN = sum), col = "red", main="Erkrankte in der Altersgruppe 55-64 nach ihrem Alkoholkonsum")
#In der Altersgruppe 55-64 ist die Verteilung relativ gleichmäßig.
tapply(esoph_55_64$ncases, esoph_55_64$tobgp, FUN = sum)
barplot(tapply(esoph_55_64$ncases, esoph_55_64$tobgp, FUN = sum), col = "yellow", main="Erkrankte in der Altersgruppe 55-64 nach ihrem Tabakkonsum")
summary(esoph_55_64)
#In der Altersgruppe 55-64 ist die Verteilung relativ gleichmäßig.


esoph_65_74<-subset(esoph, (agegp == "65-74"))
print(esoph_65_74)

tapply(esoph_65_74$ncases, esoph_65_74$alcgp, FUN = sum)
barplot(tapply(esoph_65_74$ncases, esoph_65_74$alcgp, FUN = sum), col = "red", main="Erkrankte in der Altersgruppe 65-74 nach ihrem Alkoholkonsum")
#In der Altersgruppe 65-74 sind diejenige am wenigsten gefährdet, die 40-79g Alkohol am Tag trinken.
tapply(esoph_65_74$ncases, esoph_65_74$tobgp, FUN = sum)
barplot(tapply(esoph_65_74$ncases, esoph_65_74$tobgp, FUN = sum), col = "yellow", main="Erkrankte in der Altersgruppe 65-74 nach ihrem Tabakkonsum")
summary(esoph_65_74)
#In der Altersgruppe 65-74 sind die Vielraucher am wenigsten gefährdet.

esoph_75<-subset(esoph, (agegp == "65-74"))
print(esoph_75)

tapply(esoph_75$ncases, esoph_75$alcgp, FUN = sum)
barplot(tapply(esoph_75$ncases, esoph_75$alcgp, FUN = sum), col = "red", main="Erkrankte in der Altersgruppe 75+ nach ihrem Alkoholkonsum")
#In der Altersgruppe 75+ sind diejenige am wenigsten gefährdet, die 40-79g Alkohol am Tag trinken.
tapply(esoph_75$ncases, esoph_75$tobgp, FUN = sum)
barplot(tapply(esoph_75$ncases, esoph_75$tobgp, FUN = sum), col = "yellow", main="Erkrankte in der Altersgruppe 75+ nach ihrem Tabakkonsum")
summary(esoph_75)
#In der Altersgruppe 75+ sind die Vielraucher am wenigsten gefährdet.


esoph_ncases<-subset(esoph,(ncases>=5))
print(esoph_ncases)
#Wir werden nun die Kombinationen von Alkohol- und Tabakkonsum betrachten, bei welcher
#5 oder mehr Probanten an Krebs erkrankt sind

tapply(esoph_ncases$ncases, esoph_ncases$agegp, FUN = sum)
tapply(esoph_ncases$ncases, esoph_ncases$alcgp, FUN = sum)
tapply(esoph_ncases$ncases, esoph_ncases$tobgp, FUN = sum)