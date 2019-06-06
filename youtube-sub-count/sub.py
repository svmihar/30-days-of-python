import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
from matplotlib import style
import time, psutil, requests

style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i): 
    graph_data = open('contoh.txt','r').read()
    lines = graph_data.split('\n')
    xs,ys = [],[]

    i = 0 
    while True: 
        cpu = psutil.cpu_percent()
        xs.append(cpu)
        ys.append(i)

    ax1.clear()
    ax1.plot(xs, ys)

def main(): 
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def get_subs(username, key): 
    r = requests.get(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={username}&key={key}')
    data = r.json()
    subs = data['items'][0]['statistics']['subscriberCount']
    return int(subs)

def main2(): 
    fig.canvas.draw()
    fig.show()
    i = 0
    x,y = [],[]
    while True: 
        i+=1
        cpu = get_subs('corbuzierprediction','KEY_HERE')

        print(cpu, i)
        y.append(cpu)
        x.append(i)

        ax1.plot(x,y)
        fig.canvas.draw()
        
        time.sleep(1)
        
if __name__ == "__main__":
    main2()