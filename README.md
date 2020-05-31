# Chinese-poems-generation-based-on-pictures
Generation of five character ancient poetry based on given pictures(基于图片生成五言古诗)

You also need to put the following linked files in the same directory(还需把如下链接的文件放入同一个目录下)：
https://disk.pku.edu.cn:443/link/A54728C8E322E8F1E3F59235F44BDF4A
有效期限：2024-09-11 23:59

# Thanks for zizhizhou and chinch17 's cooperation. (both good teammates)

# Our website: http://poem.boater.cn

# We will introduce the use of each PY
cifar100vgg.py is used to process image files and get related labels. The label will then correspond to key words to generate poems.

data.py is used to handle related poems txt file, generate corresponding words_vocabulary and word_vec_dict and so on.

json_handle.py is a program to select five character quatrain from the data_collection in https://github.com/chinese-poetry/chinese-poetry

parameter.py (just like its name)

rnn_model.py contains a s2s model based on attention mechanism

train.py contains train, generate and api with image

word2vec.py trains the word_vector based on gensim

# Examples
![image](https://github.com/Gold-Sea/Chinese-poems-generation-based-on-pictures/blob/master/readme_pictures/mountain.jpg)

峯然一弭苔，迢迢夜飞来。
曾见树云处，久断岧鹤来。


![image](https://github.com/Gold-Sea/Chinese-poems-generation-based-on-pictures/blob/master/readme_pictures/flower.jpg)

花暗通梅织，花开映此时。
无知酒梅红，却闻香外景。

# You can see details in our ppt

# Next step
We plan to add rhyme function
