Informatik Workshop - PyTorch Medical
===
<details><summary>English summary</summary>

This five-hour workshop `Deep Learning-Framework PyTorch and its medical application` started with an introduction to PyTorch followed by basic exercises to python and numpy.

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
</details>