import matplotlib.pyplot as plt

marks_boys = [45, 67, 78, 89, 92, 56, 73, 85, 95, 60, 77, 82, 69]
marks_girls = [55, 72, 88, 91, 65, 80, 84, 69, 89, 79, 96, 75, 100]

data = [marks_boys, marks_girls]
colors = ['b', 'm']
labels = ['Boys', 'Girls']
bins = [40, 60, 80, 100]

plt.xlabel("Total Number of Students")
plt.ylabel("Marks Range")

# Marks range
# 40–60 = Average
# 60–80 = Good
# 80–100 = Excellent

plt.hist(
    data,
    bins=bins,
    rwidth=0.95,
    color=colors,
    label=labels,
    orientation="horizontal"
)

plt.title("Student Marks Distribution Chart")
plt.legend()
plt.show()
