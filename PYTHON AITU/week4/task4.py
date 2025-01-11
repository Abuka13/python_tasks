import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
plt.title("My Timetable", fontsize=16)
plt.pie([10, 20, 20, 30, 20], labels=['Video Games', 'Alem', 'Phone', 'University', 'Family & Friends'], autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], explode=(0, 0.1, 0, 0, 0), shadow=True)
plt.axis('equal')
plt.show()
