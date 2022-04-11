import argparse
import torch

from PIL import Image
from torchvision import transforms
import os
from model import Model

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--checkpoint', default='./logs\\model-116000.pth', type=str,
                    help='path to checkpoint, e.g. ./logs/model-100.pth')  # mathod 확인
parser.add_argument('--ad', default='C:\\Users\\ST200423\\Desktop\\svhn\\dataset', type=str)  # mathod 확인


def _infer(path_to_checkpoint_file, path_to_input_image):
    model = Model()
    model.restore(path_to_checkpoint_file)
    model.cuda()

    with torch.no_grad():
        transform = transforms.Compose([
            transforms.Resize([64, 64]),
            #transforms.CenterCrop([54, 54]),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

        image = Image.open(path_to_input_image)
        image = image.convert('RGB')
        image = transform(image)
        images = image.unsqueeze(dim=0).cuda()

        length_logits, digit1_logits, digit2_logits, digit3_logits, digit4_logits, digit5_logits = model.eval()(images)

        length_prediction = length_logits.max(1)[1]
        digit1_prediction = digit1_logits.max(1)[1]
        digit2_prediction = digit2_logits.max(1)[1]
        digit3_prediction = digit3_logits.max(1)[1]
        digit4_prediction = digit4_logits.max(1)[1]
        digit5_prediction = digit5_logits.max(1)[1]

        print('length:', length_prediction.item())
        print('predict:', digit1_prediction.item(), digit2_prediction.item(), digit3_prediction.item(),
              digit4_prediction.item(), digit5_prediction.item())

    return digit1_prediction.item(), digit2_prediction.item(), digit3_prediction.item(), digit4_prediction.item(), digit5_prediction.item(), length_prediction.item()



def main(args):
    path_to_checkpoint_file = args.checkpoint
    false = 0
    imlist = []
    sub_ad = sorted(os.listdir(args.ad))

    print(sub_ad)
    for i in range(len(sub_ad)):
        if sub_ad[i].endswith('.png'):
            imlist.append(os.path.join(args.ad,sub_ad[i]))
    #     for j in range(len(imname)):
    #         imlist.append(args.ad + '/' + sub_ad[i] + '/' + imname[j])

    for i in range(len(imlist)):
        path_to_input_image = imlist[i]
        print('-'*20)
        digit_1, digit_2, digit_3, digit_4, digit_5, lenghth = _infer(path_to_checkpoint_file, path_to_input_image)
        digit = [digit_1, digit_2, digit_3, digit_4, digit_5]
        predict = []

        path_to_image_file = path_to_input_image.split('\\')[-1]
        label = path_to_image_file.split('\\')[-1].split('.')[0].split('_')[0]
        #print(label)
        num = []
        # print(len(label))
        # print(lenghth)
        for i in range(len(label)):
            num.append(int(label[i]))
            predict.append(int(digit[i]))
        print('label =', label, ':', path_to_image_file)

        for i in range(len(label)):
            if lenghth != len(label) or digit[i] != num[i]:
                false += 1
                break
    accuracy = (len(imlist) - false) / len(imlist)
    print(accuracy, 'total score')
    print((len(imlist) - false), 'true score')
    print(len(imlist), "total num")
    # print(f'true/total: {len(imlist)-false}/{len(imlist)}')



if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
