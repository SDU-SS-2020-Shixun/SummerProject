sys.path.append('../')

import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision
import cnn_model_v1
from training_set_gen import gen_config

LR = 0.01
BATCH_SIZE = 100
EPOCHS = 25
TRAINING_SET_PATH=gen_config.TRAIN_DATASET_PATH
TEST_SET_PATH=gen_config.TEST_DATASET_PATHe
MODEL_PATH='cnn_model_v1.pkl'

net = CNN_v1()
net.train()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=LR)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, patience=5, verbose=True)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# net.load_state_dict(torch.load(MODEL_PATH))

net.to(device)

for epc in range(EPOCHS):
    running_loss = 0.
    cnt = 0
    for i, data in enumerate(torch.utils.data.DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2), 0):
        inputs, labels = data
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        _,outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        cnt += 1
        running_loss += loss.item()
        print('[%d, %5d] loss: %.4f' %
              (epc + 1, (i+1)*BATCH_SIZE, running_loss/cnt))

    scheduler.step(running_loss)

print('Finished Training')

torch.save(net.state_dict(), MODEL_PATH)
net.eval()

correct, total = 0, 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        images, labels = images.to(device), labels.to(device)
        _, outputs = net(images)
        _, predicted = torch.max(outputs, dim=1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))


class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))
with torch.no_grad():
    for data in testloader:
        images, labels = data
        images, labels = images.to(device), labels.to(device)
        _,outputs = net(images)
        # print('*', outputs)
        _, predicted = torch.max(outputs, 1)
        c = (predicted == labels).squeeze()
        for i in range(BATCH_SIZE):
            label = labels[i]
            class_correct[label] += c[i].item()
            class_total[label] += 1


for i in range(10):
    print('Accuracy of %5s : %2d %%' % (
        classes[i], 100 * class_correct[i] / class_total[i]))