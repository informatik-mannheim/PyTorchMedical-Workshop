import torch

# Tensoren werden genau wie Arrays initialisiert:
shape = (2, 2)
# zeros, full, arange(..).reshape(shape)
x = torch.ones(shape)

# Operationen auf/mit Tensoren:
torch.argmax(x)
x.max()  # x.min(), x.mean(), x.sum(), s.shape

### Autograd ###
torch.ones(shape, requires_grad=True)  # mit autograd
y = torch.ones(shape)                  # ohne autograd
y.requires_grad_(True)                 # nachträgliches autograd

# ... some operations:
z = y * 2
final = z.mean()
# Um das Backtracking nach y zu starten:
final.backward()
y.grad  # enthält das Ergebnis der automatischen Differenzierung
