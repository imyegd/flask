import torch

# device='cuda:0' if torch.cuda.is_available() else 'cpu'
# print(device)
# print(torch.__version__)
from sentence_transformers import SentenceTransformer, LoggingHandler, losses,models, util
model = SentenceTransformer('bert-base-chinese')
# model = SentenceTransformer('all-MiniLM-L6-v2')
#Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.', 
    'The quick brown fox jumps over the lazy dog.']

# 读取生成的input.txt内容
f1 = open('D:/大四上/毕设/HTML/input.txt') # 读取的数据类型为str
string = f1.read()
# string = 'the lazy dog and a fox are playing'
 
# 执行你要执行的程序（例子为计算平方）
embeddings = model.encode(sentences)

print(embeddings.shape)

cosine_score0 = util.cos_sim(model.encode(string), embeddings)
print(cosine_score0)
 
# 把运行的结果写入result.txt中
f2 = open('D:/大四上/毕设/HTML/result.txt', 'w')
f2.write(str(cosine_score0))
f2.write("\nSthe most similar sentence: {}".format(sentences[torch.argmax(cosine_score0)]))
 
f1.close()
f2.close()

