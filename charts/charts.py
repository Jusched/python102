import matplotlib.pyplot as plt


def generate_pie_chart():
    labels= ["A", "B", "C","D"]
    values= [200, 300, 400, 100]

    fig, ax= plt.subplots()
# It's necessary to confirm that labels=labels, otherwise we will have an error.
    ax.pie(values, labels=labels)
# This stops the program so we can make it into an image to avoid this.
    # plt.show()
    plt.savefig("pie.png")
    plt.close()


