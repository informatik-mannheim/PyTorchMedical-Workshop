import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class MyClassifier(nn.Module):
    def __init__(self):
        super(MyClassifier, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool1 = nn.MaxPool2d(4, 4)    
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool2 = nn.MaxPool2d(4, 4)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 70)
        self.fc3 = nn.Linear(70, 5)
    
    def forward(self, x):
        x = self.pool1(self.conv1(x))
        x = self.pool2(self.conv2(x))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x   

def train(net, epochs):    
    trainloader = load_dataset('./pytorch_google_imgs/train')  
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)    
    
     #Eine Epoche entspricht einem kompletten Trainingsdurchlauf (alle Trainingsdaten einmal trainiert)
    for epoch in range(epochs): 
        for i, data in enumerate(trainloader, 0):            
            inputs, labels = data        
        
            #Zunächst den Gradientenbuffer zurücksetzen
            optimizer.zero_grad()
        
            #Anschließend die Ausgabe des Netzes für eine Eingabe bestimmen
            outputs = net(inputs)   
            
            #Daraufhin den Fehler mithilfe der Fehlerfunktion bestimmen
            loss = criterion(outputs, labels)
            loss.backward()
            
            #Sowie abschließend den Fehler durch das Optimierungsverfahren minimieren
            optimizer.step()
            
##############################################################################
# An den untenstehenden Hilfsmethoden müssen Sie keine Anpassungen vornehmen.#
##############################################################################
    
def getAccuracy(net):
    testloader = load_dataset('./pytorch_google_imgs/test')
    correct = 0
    total = 0
    
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    print(str(100 * correct / total)+" % of the 125 test images were classified correct.")
    
def showRandomPredictions(net):
    testloader = load_dataset('./pytorch_google_imgs/test')
    dataiter = iter(testloader)
    images, labels = dataiter.next()
    
    #Zuordnung der Klassen erfolgt durch torch automatisch über den Ordnernamen in dieser Reihenfolge
    classes = ('intestines', 'kidneys', 'liver', 'lungs', 'stomach')
    
    #get predicted results
    outputs = net(images)
    _, predicted = torch.max(outputs, 1)
    
    # print images
    imshow(torchvision.utils.make_grid(images))
    print('Correct classes are:  ', ' '.join('%5s' % classes[labels[j]] for j in range(4)))   
    print('Classifier predicted: ', ' '.join('%5s' % classes[predicted[j]] for j in range(4)))
    

def load_dataset(data_dir):
    transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])        
    dset = torchvision.datasets.ImageFolder(data_dir, transform)     
    return torch.utils.data.DataLoader(dset, batch_size=4, shuffle=True, num_workers=4)

def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))

#In Windows muss aufgrund eines Bugs diese if-Abfrage gesetzt sein
if __name__ == "__main__":
    __spec__ = None
    net = MyClassifier()    
    train(net, 2)
    getAccuracy(net)
    showRandomPredictions(net)