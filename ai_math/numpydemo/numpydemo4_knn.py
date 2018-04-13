import numpy as np


data = np.loadtxt('mpgTrainingSet.txt', delimiter='\t',
                  usecols=[0, 1, 2, 3, 4, 5], dtype=float,
                  skiprows=1)

label = data[:, 0].reshape((-1, 1))
feature = data[:, 1:]

fmean = np.mean(feature, axis=0)
fsd = np.std(feature, axis=0)
fnormal = (feature - fmean) / fsd

# x1 = feature - fmean
# x2 = feature - (np.tile(fmean, (feature.shape[0], 1)))
#
# assert(np.all(x1==x2))

# 计算距离

testrow = np.array([8, 307.0, 130.0, 3504, 12.0])
rownormal = (testrow - fmean) / fsd
diff = fnormal - rownormal
distances = np.sum(diff**2, axis=1)
dissort = distances.argsort()

k = 10

topk_labels = {}

for i in range(k):
    l = label[i, 0]
    topk_labels.setdefault(l, 0)
    topk_labels[l] += 1

print(sorted(topk_labels.items(), key=lambda x:x[1], reverse=True)[0])