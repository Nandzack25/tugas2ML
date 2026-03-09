
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")

plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')

plt.scatter(data['day'], data['tip'])

plt.show()



gender_counts = data['sex'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(gender_counts, 
        labels=gender_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['skyblue', 'pink'])

plt.title("Persentase Pemberi Tip Berdasarkan Jenis Kelamin")

plt.show()