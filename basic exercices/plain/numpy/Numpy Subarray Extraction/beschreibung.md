Numpy Subarray Extraction
===
Hier sollst du eine Funktion schreiben, die ein 6x6 Array in vier 3x3 Arrays aufteilt.
Die Funktion bekommt also ein (beliebiges) 6x6 Array als Input und soll `ein Array, welches vier 3x3 Arrays` beinhaltet zurückgeben (Eine Liste oder ein Tupel sind als äußeres Array auch akzeptabel)

Das folgende Beispiel veranschaulicht die Aufgabe:

Die folgende Matrix veranschaulicht ein 6x6 Array:
00 01 02 03 04 05  
06 07 08 09 10 11  
12 13 14 15 16 17  
18 19 20 21 22 23  
24 25 26 27 28 29  
30 31 32 33 34 35

Aus diesem Array wollen wir die jetzt gezeigten 4 Sektoren herausbekommen:
<pre>
00  01  02  |  03  04  05  
06  07  08  |  09  10  11  
12  13  14  |  15  16  17  
+++++++++++++++++++++++++    
18  19  20  |  21  22  23  
24  25  26  |  27  28  29  
30  31  32  |  33  34  35
</pre>

Das zurückgegebene Array soll die 4 Sektoren in Reihenfolge entsprechend der Indizes beinhalten:
<pre>
q0 | q1  
+++++  
q2 | q3
</pre>

<details open><summary>Die Lösung zum gezeigten Beispiel siehst du hier:</summary>

<pre>
[
    [[ 0  1  2]
    [ 6  7  8]
    [12 13 14]]

    [[ 3  4  5]
    [ 9 10 11]
    [15 16 17]]
    
    [[18 19 20]
    [24 25 26]
    [30 31 32]]

    [[21 22 23]
    [27 28 29]
    [33 34 35]]
]
</pre>

`Bitte beachte, dass die Werte nur in diesem Beispiel aufsteigend sind und du dich darauf nicht verlassen darfst. (In den Tests werden zufällig generierte Zahlen verwendet).`
</details>