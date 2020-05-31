from parameter import *
from wordvec import *
import data
import rnn_model
import train
import cifar100vgg as cfvg
import estimate as es


# 记录在运行程序时后面的字符串，默认是default
def defineArgs():
    parser = argparse.ArgumentParser(description="Chinese_poem_generator.")
    parser.add_argument("-m", "--mode", help="select mode by 'train' or test or head",
                        choices=["train", "test", "head"], default="test")
    return parser.parse_args()


if __name__ == "__main__":
    args = defineArgs()
    # 初始化数据的对象
    traindata = data.poems_data(isEvaluate=False)
    # 进行训练或者生成
    if args.mode == "train":
        train.train(traindata)
    else:
        '''l = list('春华秋实')
        for i in range(len(l)):
            l[i] = poem_Data.word_ID[l[i]]
        for j in range(4):
            res = train.generate(poem_Data, l)
            print(res)
        r = 0'''
        print("请输入图片的路径:")
        path = input()
        label = cfvg.pic_to_label(path, show_pictures=False)
        print(label)
        keywords, poems = train.label_poem(label)
        res_poem = es.evaluate(keywords, poems)
        print("最终的版本:\n")
        print(res_poem)
        #print(train.api_html(res_poem))
