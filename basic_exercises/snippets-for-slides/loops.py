"""
Zur folgenden While-Schleife muss man wohl nichts mehr sagen:
"""

grund_studium = True
while grund_studium:
    print("Wo ist die if-Schleifen?")
    print("Noten zählen erst im Hauptstudium")

"""
Eleganter lässt es sich mittels `for i in range` iterieren.
Die abgebildete Schleife benutzt ein iterierbares `range`-Objekt, welches die Werte 0 bis 4 durchläuft:
"""

for i in range(5):
    # 0 to 4 [5 is not included]
    print(i)
"""
In Kombination mit der Länge einer Liste, welche über die globale Funktion `len(list)` erreichbar ist, kann man so über die Elemente einer Liste über deren Indizes iterieren:
"""

for i in range(len(liste)):
    # iterate using the list's length
    do_something(liste[i])
"""
Noch schöner wird es, wenn man direkt über die Elemente der Liste iteriert:
"""
elements = [0, 1, 2, 3, 4]
for element in elements:
    print(element)

"""
Will man zwar über die volle Länge einer Liste iterieren, aber weder deren Indizes noch Inhalte verwenden, soll man die Variable entsprechend den Konventionen `_` nennen.
"""
for _ in range(len(elements)):
    print("iteration")
