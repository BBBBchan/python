import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6), dpi=80)			#创建画布，设置长宽，dot per inch 
ax = plt.subplot(111)
ax.xaxis.set_ticks_position('bottom')				#设置横坐标位置
ax.spines['bottom'].set_position(('data',0))		#设置x轴位置
ax.yaxis.set_ticks_position('left')					#设置纵坐标位置
ax.spines['left'].set_position(('data',0))			#设置y轴位置

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)

C, S = np.cos(X*2), np.sin(X*2)
t = 2*np.pi/3

plt.plot(X, C, color='blue', linewidth=0.5, linestyle='-', label='cosine')		#改变线的颜色,粗细，线型,图例
plt.plot(X, S, color='red', linewidth=0.5, linestyle='-', label='sine')
plt.legend(loc='upper left', frameon=True)				#设置图例属性，frameon决定图例有没有框

plt.plot([t,t], [0,np.cos(t)], color='black', linewidth=1.5, linestyle='--')	#虚线
plt.scatter([t,],[np.cos(t),], 50, color ='black')								#标点
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',						#箭头标识
             xy=(t, np.cos(t)),  xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.xlim(X.min()*1.1, X.max()*1.1)			#设置x的取值范围
plt.ylim(C.min()*1.1, C.max()*1.1)			#设置y的取值范围

plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
			,[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi/2$'])		#逐个设置横坐标，第一行是数值，第二行是显示
plt.yticks( [-1, 0, +1]
			,[r'$-1$', r'$0$', r'$+1$'])								#逐个设置纵坐标

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')






plt.show()