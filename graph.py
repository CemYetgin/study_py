import matplotlib.pyplot as plt

class Graph:
    def __init__(self, db):
        self.db = db

    def pie_chart(self):
        # Occupation
        data = self.db.fetch_all("SELECT occupation, COUNT(*) FROM employees GROUP BY occupation")
        labels, sizes = zip(*data)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
        # Gender
        data = self.db.fetch_all("SELECT gender, COUNT(*) FROM employees GROUP BY gender")
        labels, sizes = zip(*data)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def histogram(self):
        data = self.db.fetch_all("SELECT salary FROM employees")
        salaries = [row[0] for row in data]
        plt.hist(salaries, bins=10)
        plt.xlabel('Salary')
        plt.ylabel('Number of Employees')
        plt.show()

    def scatter_plot(self):
        data = self.db.fetch_all("SELECT employee_id, salary FROM employees")
        ids, salaries = zip(*data)
        plt.scatter(ids, salaries)
        plt.xlabel('Employee ID')
        plt.ylabel('Salary')
        plt.show()
