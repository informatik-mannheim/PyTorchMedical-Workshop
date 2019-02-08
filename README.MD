Informatik Workshop - PyTorch Medical
===
<details open><summary>German</summary>

Der fünfstündige workshop `Deep Learning-Framework PyTorch Deep Learning-Framework PyTorch und Anwendungen in der Medizin` fängt mit einer Einführung zu PyTorch, gefolgt von Grundlagen zu Python und numpy an.

Der Code in diesem Repo wurde für Aufgaben und Materialien verwendet und ist wiefolgt gegliedert:
- [basic_exercises](./basic_exercises/) enthält Aufgaben zu Python und numpy. `Dafür (inklusive Theorie auf den Folien) sind ca. 20% (~1h) der Workshopzeit vorgesehen`
    - [codewars](./basic_exercises/codewars/): Code für Codewars (copy-paste der einzelnen Dateien entsprechend des Kata-Setups in Codewars)
    - [plain](./basic_exercises/plain/): Da Codewars nicht wirklich für Workshops gedacht ist (und als Fallback während des Workshops), enthält dieser Ordner analog zum Codewars-Ordner dieselben Aufgaben, allerdings Stand-alone ausführbar (also ohne Codewars)
        - "template.py" muss von Teilnehmern bearbeitet & ausgefüllt werden
        - "simple_testcase.py" kann von Teilnehmern als einfacher Test (ohne Lösung) verwendet werden
        - "solution.py" beinhaltet die vorbereitete Lösung zur jeweiligen Aufgabe `Um Schummeln zu verhindern sollten die Lösungen separat/später verteilt werden`
        - "random_testcases.py" kann (`wenn die Lösung verfügbar ist`) als automatisierte und zufällige Testbasis genutzt werden, sodass Teilnehmer nicht nur die Beispieltests ausimplementiert haben.
        - beschreibung.md ...
        - head.py wird benutzt um das Test-Framework von Codewars zu simulieren/zu ersetzen
    - [snippets-for-cheatsheet](./basic_exercises/snippets-for-cheatsheet/) enthält Codefragmente, welche auf einem Cheatsheet stehen könnten
    - [snippets-for-slides](./basic_exercises/snippets-for-slides/) enthält Code, welcher für die Theorie/Beispiel auf den Folien verwendet wurde
- [basic_templates](./basic_templates/) enthält Code, welcher die einige Grundlagen von Python, numpy und PyTorch erklärt (`englische Kommentare`). Einige Teile davon sind dazu gedacht ausgeführt zu werden, um aus dem Console.Out zu lesen, da der Code teilweise eher dafür ausgelegt ist.
- [Hands-on_Neuronale_Netze](./Hands-on_Neuronale_Netze/) enthält Übungen zu neuronalen Netzen und beginnt mit einer Übung zur Aktivierungsfunktion. Am Ende dieser Übungen steht die Fertigstellung eines Netzes zur Klassifizierung von Organen (Bildern von Organen). `Die Übung sollte ca. 50-60% (~3h) der Zeit ausfüllen (inklusive Erklärung der Theorie in den Folien und der Betreuung)`
    - pytorch_google_imgs `muss mit Testdaten gefüllt werden`. Empfohlen sind mindestens 500 gleichgroße Bilder (verteilt auf die verschiedenen Organe)
</details>

<details><summary>English summary</summary>

This five-hour workshop `Deep Learning-Framework PyTorch and its medical application` starts with an introduction to PyTorch followed by basic exercises to python and numpy.

The code in this repository was used for exercies and the structure is explained below:
- [basic_exercises](./basic_exercises/) contains the exercises for the introduction of python and numpy. `It may take about 20% (~1h) of the workshop time`
    - [codewars](./basic_exercises/codewars/): code for codewars (copy-paste it into the respective challenge (called kata)) if you want to use codewars again
        - should be self-explanatory if you look at codewars' setup of challenges/katas
    - [plain](./basic_exercises/plain/): as codewars is not really intended for workshops (and as a fallback), this directory contains the same code-base as the "codewars"-folder, however it will run standalone as the test-framework and a few required adaptions/improvements have been made
        - the file "template.py" has to be filled out by participants
        - the file "simple_testcase.py" can be used to run tests against basic tests
        - the file "solution.py" contains the prepared solution. `Don't deploy the exercises with solutions if you don't want participants to cheat`
        - "random_testcases.py" can be run to execute multiple random generated tests in for-loops with usually 100 iterations
        - beschreibung.md is the german version of the exercise description
        - head.py was used to "simulate" the test-framework used at codewars
    - [snippets-for-cheatsheet](./basic_exercises/snippets-for-cheatsheet/) includes code (with german explanations)
    - [snippets-for-slides](./basic_exercises/snippets-for-slides/) includes code used on the presentation slides
- [basic_templates](./basic_templates/) includes code that explains basics in python, numpy and pytorch (`english explanations`). Some parts of it are better run and looked at in the console.out than the actual code.
- [Hands-on_Neuronale_Netze](./Hands-on_Neuronale_Netze/) contains exercises to neuronal networks starting with basic activation functions (written with numpy only) and ends with working neuronal networks for image classification. `These exercises should make up about 50-60% (~3h) of the workshop time (including theory and introductions)`
    - pytorch_google_imgs `has to be prepared with testdata`. We recommend a minimum-total of 500 same size images images (distributed over the different organs).
</details>