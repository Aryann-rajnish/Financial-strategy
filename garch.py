from random import gauss
from random import seed
import matplotlib.pyplot as plt
seed(1)
data = [gauss(0,i*0.01) for i in range(0,100)]
n_test = 10
train, test = data[:-n_test], data[-n_test:]
from arch import arch_model
model = arch_model(train,mean='Zero',vol='ARCH',p=15)
model_fit = model.fit()
yhat = model_fit.forecast(horizon=n_test)
var = [i*0.01 for i in range(0,100)]
plt.plot(var[-n_test:])
# plot forecast variance
plt.plot(yhat.variance.values[-1, :])
plt.show()
