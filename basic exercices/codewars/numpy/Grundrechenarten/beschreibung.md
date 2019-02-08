Grundrechenarten und numpy Arrays
===
In dieser Aufgabe sollst du einfache mathematische Berechnungen entsprechend den Grundoperatoren ausführen.

Die Code-Vorlage reicht vermutlich als Beschreibung aus, es wird also jeweils ein beliebiges Array als Input gegeben und soll mit einem gegebenen Wert verrechnet werden.

Zwei kurze Beispiele:
```
Addition:
    Input:
        array: [[1,1],[2,2]]
        value: 1
    Return:
        [[2,2],[3,3]]
```

```
Division
    Input:
        array: [[1,1],[3,3]]
        value: 2
    Return: 
        [[0.5, 0.5],[1.5, 1.5]]
```

Die letzte Funktion erhält zwei, **garantiert gleichgroße** Arrays `A` und `B` und erwartet ein Array derselben größe als Rückgabewert.
Das neue Array `C` soll die Summe der beiden Arrays über deren jeweilige Indizes ergeben, also **C<sub>0,0</sub> = A<sub>0,0</sub> + B<sub>0,0</sub>** bzw. **C<sub>i,j</sub> = A<sub>i,j</sub> + B<sub>i,j</sub>**

```
add_array_to_array
    Input:
        a: [[1,1], [1,1]]
        b: [[2,2], [2,2]]
    Return:
        [[3,3], [3,3]]

```
**Tipp: Es gibt einen einfacheren Weg als über jeden Wert zu iterieren.**