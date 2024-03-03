import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as T
from PIL import Image

labels = {
    0: 'Vada Pav',
    1: 'Tandoori Chicken',
    2: 'Idly',
    3: 'Meduvadai',
    4: 'Samosa',
    5: 'Kathi Roll',
    6: 'Halwa',
    7: 'Biriyani',
    8: 'Gulab Jamun',
    9: 'Dosa'
}


test_transforms = T.Compose([
    T.Resize(size=(128,128)),
    T.ToTensor()
])

class FitFuelModel(nn.Module):
    def __init__(self,input_size=3,output_size=len(labels)):
        super().__init__()
        self.conv_blk1 = nn.Sequential(
            nn.Conv2d(in_channels=input_size,out_channels=32,kernel_size=3,stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32,out_channels=16,kernel_size=3,stride=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3,stride=1)
        )
        self.classifier = nn.Sequential(
            nn.Linear(in_features=238144,out_features=32),
            nn.ReLU(),
            nn.Linear(in_features=32,out_features=32),
            nn.ReLU(),
            nn.Linear(in_features=32,out_features=output_size)
        )

    def forward(self,x):
        x = self.conv_blk1(x)
        x = torch.flatten(x,1)
        x = self.classifier(x)
        return x

model = FitFuelModel()
model.load_state_dict(torch.load('pretrained\\prototype(beta_ 7).pth',map_location=torch.device('cpu')))

def prediction(text:str):

    img = Image.open(text)
    transformed = test_transforms(img)
    model.eval()
    with torch.inference_mode():
        logits = model(transformed.unsqueeze(0))
        print(f'logits: {logits}')
        probs = torch.softmax(logits,dim=1)
        print(f'probability: {probs}')
        output = torch.argmax(probs,dim=1)
        index = output.data.item()
        return labels[index]

if __name__ == '__main__':
    text = input('enter the loc of image')
    prediction(text)
